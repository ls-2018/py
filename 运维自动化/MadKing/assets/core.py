# _*_coding:utf-8_*_

import json
from django.core.exceptions import ObjectDoesNotExist
from assets import models
from django.utils import timezone


class Asset(object):
    def __init__(self, request):
        self.request = request
        self.mandatory_fields = ['sn', 'asset_id', 'asset_type']  # must contains 'sn' , 'asset_id' and 'asset_type'
        self.field_sets = {
            'asset': ['manufactory'],
            'server': ['model', 'cpu_count', 'cpu_core_count', 'cpu_model', 'raid_type', 'os_type', 'os_distribution',
                       'os_release'],
            'networkdevice': []
        }
        self.response = {
            'error': [],
            'info': [],
            'warning': []
        }
        self.clean_data = {}
        self.asset_obj = None

    def response_msg(self, msg_type, key, msg):
        if msg_type in self.response:
            self.response[msg_type].append({key: msg})
        else:
            raise ValueError

    def mandatory_check(self, data, only_check_sn=False):
        """
        :param data:
        :param only_check_sn: 根据  asset_id 或 sn  有无,判断资产表记录是否存在
        :return:
        """
        for field in self.mandatory_fields:
            if field not in data:
                self.response_msg('error', 'MandatoryCheckFailed',
                                  "The field [%s] is mandatory and not provided in your reporting data" % field
                                  )
        else:
            # 一次性返回多个错误
            # 在for循环完整完成后才执行else；如果中途从break跳出，则连else一起跳出。
            if self.response['error']:
                return False
        try:
            # 是否传过来了资产SN号
            if not only_check_sn:
                self.asset_obj = models.Asset.objects.get(id=int(data['asset_id']), sn=data['sn'])
            else:
                self.asset_obj = models.Asset.objects.get(sn=data['sn'])
            return True
        except ObjectDoesNotExist as e:
            self.response_msg('error', 'AssetDataInvalid',
                              "Cannot find asset object in DB by using asset id [%s] and SN [%s] " % (
                                  data['asset_id'], data['sn']))
            self.waiting_approval = True  # 待审批资产
        return False

    def get_asset_id_by_sn(self):
        """
         上传待审批的资产数据
        """
        data = self.request.POST.get("asset_data")
        if data:
            try:
                data = json.loads(data)
                if self.mandatory_check(data, only_check_sn=True):
                    # 根据sn判断资产存在
                    response = {'asset_id': self.asset_obj.id}
                else:
                    if hasattr(self, 'waiting_approval'):
                        response = {
                            'needs_aproval': "this is a new asset,needs IT admin's approval to create the new asset id."}
                        self.clean_data = data
                        self.save_new_asset_to_approval_zone()
                        print(response)
                    else:
                        response = self.response
            except ValueError as e:
                self.response_msg('error', 'AssetDataInvalid', str(e))
                response = self.response

        else:
            self.response_msg('error', 'AssetDataInvalid', "The reported asset data is not valid or provided")
            response = self.response
        return response

    def save_new_asset_to_approval_zone(self):
        """
        在 资产待审批表  中插入一条记录
        """
        asset_sn = self.clean_data.get('sn')
        models.NewAssetApprovalZone.objects.get_or_create(sn=asset_sn,
                                                          data=json.dumps(self.clean_data),
                                                          manufactory=self.clean_data.get('manufactory'),
                                                          model=self.clean_data.get('model'),
                                                          asset_type=self.clean_data.get('asset_type'),
                                                          ram_size=self.clean_data.get('ram_size'),
                                                          cpu_model=self.clean_data.get('cpu_model'),
                                                          cpu_count=self.clean_data.get('cpu_count'),
                                                          cpu_core_count=self.clean_data.get('cpu_core_count'),
                                                          os_distribution=self.clean_data.get('os_distribution'),
                                                          os_release=self.clean_data.get('os_release'),
                                                          os_type=self.clean_data.get('os_type'),
                                                          )
        return True

    def data_is_valid(self):
        data = self.request.POST.get("asset_data")
        if data:
            try:
                data = json.loads(data)
                self.mandatory_check(data)
                self.clean_data = data
                if not self.response['error']:
                    return True
            except ValueError as e:
                self.response_msg('error', 'AssetDataInvalid', str(e))
        else:
            self.response_msg('error', 'AssetDataInvalid', "The reported asset data is not valid or provided")

    def __is_new_asset(self):
        """
        资产记录  有没有被  设备 关联
        :return:
        """
        if not hasattr(self.asset_obj, self.clean_data['asset_type']):
            return True
        else:
            return False

    def data_inject(self):
        """
        将资产待审批记录   ----->   资产表
        """
        if self.__is_new_asset():
            # 没有 设备 关联 资产记录
            print('\033[32;1m---new asset,going to create----\033[0m')
            self.create_asset()
        else:  # asset already already exist , just update it
            print('\033[33;1m---asset already exist ,going to update----\033[0m')
            self.update_asset()

    def data_is_valid_without_id(self):
        """
        在资产表中， 根据sn，判断是否记录
        :return: True 表示没有资产记录
        """
        data = self.request.POST.get("asset_data")
        if data:
            try:
                data = json.loads(data)
                asset_obj = models.Asset.objects.get_or_create(sn=data.get('sn'), name=data.get('sn'))
                data['asset_id'] = asset_obj[0].id
                self.mandatory_check(data)  # 根据asset_id，判断资产记录是否存在
                self.clean_data = data
                if not self.response['error']:
                    return True
            except ValueError as e:
                self.response_msg('error', 'AssetDataInvalid', str(e))
        else:
            self.response_msg('error', 'AssetDataInvalid', "The reported asset data is not valid or provided")

    def reformat_components(self, identify_field, data_set):
        '''This function is used as workround for some components's data structor is big dict ,yet
        the standard structor is list,e.g:
        standard: [{
            "slot": "1I:1:1",
            "capacity": 300,
            "sn": "",
            "model": "",
            "enclosure": "0",
            "iface_type": "SAS"
        },
        {
            "slot": "1I:1:2",
            "capacity": 300,
            "sn": "",
            "model": "",
            "enclosure": "0",
            "iface_type": "SAS"
        }]
        but for some components such as ram:
        {"PROC 2 DIMM 1": {
            "model": "<OUT OF SPEC>",
            "capacity": 0,
            "sn": "Not Specified",
            "manufactory": "UNKNOWN"
        },}

        it uses key as identified field, the key is actually equals slot field in db model field, this unstandard
        data source should be dprecated in the future, now I will just reformat it as workround
        '''
        for k, data in data_set.items():
            data[identify_field] = k

    def __verify_field(self, data_set, field_key, data_type, required=True):
        field_val = data_set.get(field_key)
        if field_val is not None:
            try:
                data_set[field_key] = data_type(field_val)
            except ValueError as e:
                self.response_msg('error', 'InvalidField',
                                  "The field [%s]'s data type is invalid, the correct data type should be [%s] " % (
                                      field_key, data_type))

        elif required is True:
            self.response_msg('error', 'LackOfField',
                              "The field [%s] has no value provided in your reporting data [%s]" % (
                                  field_key, data_set))

    def create_asset(self):
        """
        根据待审批数据中 资产类型 调用 不同的资产 创建函数
        :return:
        """
        func = getattr(self, '_create_%s' % self.clean_data['asset_type'])
        create_obj = func()

    def update_asset(self):
        func = getattr(self, '_update_%s' % self.clean_data['asset_type'])
        create_obj = func()

    def _update_server(self):
        # nic
        self.__update_asset_component(
            data_source=self.clean_data['nic'],
            fk='nic_set',
            update_fields=['name', 'sn', 'model', 'macaddress', 'ipaddress', 'netmask', 'bonding'],
            identify_field='macaddress'
        )
        # disk
        self.__update_asset_component(
            data_source=self.clean_data['physical_disk_driver'],
            fk='disk_set',
            update_fields=['slot', 'sn', 'model', 'manufactory', 'capacity', 'iface_type'],
            identify_field='slot'
        )
        # ram
        self.__update_asset_component(
            data_source=self.clean_data['ram'],
            fk='ram_set',
            update_fields=['slot', 'sn', 'model', 'capacity'],
            identify_field='slot'
        )

        self.__update_cpu_component()
        self.__update_manufactory_component()
        self.__update_server_component()

    def _create_server(self):
        self.__create_server_info()
        self.__create_or_update_manufactory()
        self.__create_cpu_component()
        # 多条记录
        self.__create_disk_component()
        self.__create_nic_component()
        self.__create_ram_component()

        log_msg = "Asset [<a href='/admin/assets/asset/%s/' target='_blank'>%s</a>] has been created!" % (
            self.asset_obj.id, self.asset_obj)
        self.response_msg('info', 'NewAssetOnline', log_msg)

    def __create_server_info(self, ignore_errs=False):
        try:
            self.__verify_field(self.clean_data, 'model', str)
            # 按照 思路来讲 ，这里是不会产生错误的
            if not len(self.response['error']) or ignore_errs is True:
                # 没有错误、或者可以忽略错误
                data_set = {
                    'asset_id': self.asset_obj.id,
                    'raid_type': self.clean_data.get('raid_type'),
                    'model': self.clean_data.get('model'),
                    'os_type': self.clean_data.get('os_type'),
                    'os_distribution': self.clean_data.get('os_distribution'),
                    'os_release': self.clean_data.get('os_release'),
                }

                # 常见server记录
                obj = models.Server(**data_set)
                # 更新资产表数据
                # obj.asset.model = self.clean_data.get('model')
                obj.save()
                return obj
        except Exception as e:
            self.response_msg('error', 'ObjectCreationException', 'Object [server] %s' % str(e))

    def __create_or_update_manufactory(self, ignore_errs=False):
        try:
            self.__verify_field(self.clean_data, 'manufactory', str)
            if not len(self.response['error']) or ignore_errs is True:
                manufactory = self.clean_data.get('manufactory')
                obj_exist = models.Manufactory.objects.filter(manufactory=manufactory)
                if obj_exist:
                    obj = obj_exist[0]
                else:  # create a new one
                    obj = models.Manufactory(manufactory=manufactory)
                    obj.save()
                self.asset_obj.manufactory = obj
                self.asset_obj.save()
        except Exception as e:
            self.response_msg('error', 'ObjectCreationException', 'Object [manufactory] %s' % str(e))

    def __create_cpu_component(self, ignore_errs=False):
        try:
            self.__verify_field(self.clean_data, 'model', str)
            self.__verify_field(self.clean_data, 'cpu_count', int)
            self.__verify_field(self.clean_data, 'cpu_core_count', int)
            if not len(self.response['error']) or ignore_errs is True:
                data_set = {
                    'asset_id': self.asset_obj.id,
                    'cpu_model': self.clean_data.get('cpu_model'),
                    'cpu_count': self.clean_data.get('cpu_count'),
                    'cpu_core_count': self.clean_data.get('cpu_core_count'),
                }

                obj = models.CPU(**data_set)
                obj.save()
                log_msg = "Asset[%s] --> has added new [cpu] component with data [%s]" % (self.asset_obj, data_set)
                self.response_msg('info', 'NewComponentAdded', log_msg)
                return obj
        except Exception as e:
            self.response_msg('error', 'ObjectCreationException', 'Object [cpu] %s' % str(e))

    def __create_disk_component(self):
        disk_info = self.clean_data.get('physical_disk_driver')
        if disk_info:
            for disk_item in disk_info:
                try:
                    self.__verify_field(disk_item, 'slot', str)  # 有的是数字，有的是字符串
                    self.__verify_field(disk_item, 'capacity', float)
                    self.__verify_field(disk_item, 'iface_type', str)
                    self.__verify_field(disk_item, 'model', str)
                    if not len(self.response['error']):
                        # no processing when there's no error happend
                        data_set = {
                            'asset_id': self.asset_obj.id,
                            'sn': disk_item.get('sn'),
                            'slot': disk_item.get('slot'),
                            'capacity': disk_item.get('capacity'),
                            'model': disk_item.get('model'),
                            'iface_type': disk_item.get('iface_type'),
                            'manufactory': disk_item.get('manufactory'),
                        }

                        obj = models.Disk(**data_set)
                        obj.save()

                except Exception as e:
                    self.response_msg('error', 'ObjectCreationException', 'Object [disk] %s' % str(e))
        else:
            self.response_msg('error', 'LackOfData', 'Disk info is not provied in your reporting data')

    def __create_nic_component(self):
        nic_info = self.clean_data.get('nic')
        if nic_info:
            for nic_item in nic_info:
                try:
                    self.__verify_field(nic_item, 'macaddress', str)
                    if not len(self.response['error']):
                        # no processing when there's no error happend
                        data_set = {
                            'asset_id': self.asset_obj.id,
                            'name': nic_item.get('name'),
                            'sn': nic_item.get('sn'),
                            'macaddress': nic_item.get('macaddress'),
                            'ipaddress': nic_item.get('ipaddress'),
                            'bonding': nic_item.get('bonding'),
                            'model': nic_item.get('model'),
                            'netmask': nic_item.get('netmask'),
                        }

                        obj = models.NIC(**data_set)
                        obj.save()

                except Exception as e:
                    self.response_msg('error', 'ObjectCreationException', 'Object [nic] %s' % str(e))
        else:
            self.response_msg('error', 'LackOfData', 'NIC info is not provied in your reporting data')

    def __create_ram_component(self):
        ram_info = self.clean_data.get('ram')
        if ram_info:
            for ram_item in ram_info:
                try:
                    self.__verify_field(ram_item, 'capacity', int)
                    if not len(self.response['error']):
                        # no processing when there's no error happend
                        data_set = {
                            'asset_id': self.asset_obj.id,
                            'slot': ram_item.get("slot"),
                            'sn': ram_item.get('sn'),
                            'capacity': ram_item.get('capacity'),
                            'model': ram_item.get('model'),
                        }

                        obj = models.RAM(**data_set)
                        obj.save()

                except Exception as e:
                    self.response_msg('error', 'ObjectCreationException', 'Object [ram] %s' % str(e))
        else:
            self.response_msg('error', 'LackOfData', 'RAM info is not provied in your reporting data')

    def __update_server_component(self):
        update_fields = ['model', 'raid_type', 'os_type', 'os_distribution', 'os_release']
        if hasattr(self.asset_obj, 'server'):
            self.__compare_component(model_obj=self.asset_obj.server,
                                     fields_from_db=update_fields,
                                     data_source=self.clean_data)
        else:
            self.__create_server_info(ignore_errs=True)

    def __update_manufactory_component(self):
        self.__create_or_update_manufactory(ignore_errs=True)

    def __update_cpu_component(self):
        update_fields = ['cpu_model', 'cpu_count', 'cpu_core_count']
        if hasattr(self.asset_obj, 'cpu'):
            self.__compare_component(model_obj=self.asset_obj.cpu,
                                     fields_from_db=update_fields,
                                     data_source=self.clean_data)
        else:
            self.__create_cpu_component(ignore_errs=True)

    def __update_asset_component(self, data_source, fk, update_fields, identify_field=None):
        """
        :param data_source: 从客户端提交的数据
        :param fk: 由资产记录根据fk ---> 设备信息的记录 ---> 设备组件的记录
        :param update_fields: 哪些字段需要比较
        :param identify_field:设备组件表中的 唯一 的 组件 标识  ，如果没有用asset_id标识(结果可能有多个)
        :return:
        """
        try:
            component_obj = getattr(self.asset_obj, fk)
            if hasattr(component_obj, 'select_related'):  # this component is reverse m2m relation with Asset model
                objects_from_db = component_obj.select_related()
                for obj in objects_from_db:
                    key_field_data = getattr(obj, identify_field)
                    # use this key_field_data to find the relative data source from reporting data
                    if type(data_source) is list:
                        for source_data_item in data_source:

                            key_field_data_from_source_data = source_data_item.get(identify_field)
                            # 客户端数据是否有该设备所必须拥有的唯一标识
                            if key_field_data_from_source_data:  # 匹配了对应网卡
                                if key_field_data == key_field_data_from_source_data:
                                    # 客户端的数据与数据库的数据匹配上（根据数据表唯一标识），进行下一步更新
                                    self.__compare_component(model_obj=obj, fields_from_db=update_fields,
                                                             data_source=source_data_item)
                                    break
                            else:
                                self.response_msg('warning', 'AssetUpdateWarning',
                                                  "组件 [%s]'s -- [%s] 没有提供唯一标识 " % (fk, identify_field))

                        else:
                            # 汇报的数据不全，---> 资产移除，
                            print('\033[33;1mError:组件 [%s],没有上报数据!\033[0m' % key_field_data)
                            self.response_msg("error", "AssetUpdateWarning", "组件 [%s],没有上报数据!" % key_field_data)

                    # 和以前客户端做兼容
                    elif type(data_source) is dict:  # deprecated
                        for key, source_data_item in data_source.items():
                            key_field_data_from_source_data = source_data_item.get(identify_field)
                            if key_field_data_from_source_data:
                                if key_field_data == key_field_data_from_source_data:
                                    self.__compare_component(model_obj=obj, fields_from_db=update_fields,
                                                             data_source=source_data_item)
                                    break
                            else:  # key field data from source data cannot be none
                                self.response_msg(
                                    'warning', 'AssetUpdateWarning',
                                    "Asset component [%s]'s key field [%s] is not provided in reporting data " % (
                                        fk, identify_field))

                        else:  # couldn't find any matches, the asset component must be broken or changed manually
                            print(
                                '\033[33;1mWarning:cannot find any matches in source data by using key field val [%s],component data is missing in reporting data!\033[0m' % (
                                    key_field_data))
                    else:
                        print('\033[31;1mMust be sth wrong,logic should goes to here at all.\033[0m')
                # compare all the components from DB with the data source from reporting data
                self.__filter_add_or_deleted_components(model_obj_name=component_obj.model._meta.object_name,
                                                        data_from_db=objects_from_db, data_source=data_source,
                                                        identify_field=identify_field)

            else:  # this component is reverse fk relation with Asset model
                pass
        except ValueError as e:
            print('\033[41;1m%s\033[0m' % str(e))

    def __filter_add_or_deleted_components(self, model_obj_name, data_from_db, data_source, identify_field):
        '''This function is filter out all  component data in db but missing in reporting data, and all the data in reporting data but not in DB'''
        data_source_key_list = []  # save all the identified keys from client data,e.g: [macaddress1,macaddress2]
        if type(data_source) is list:
            for data in data_source:
                data_source_key_list.append(data.get(identify_field))

        elif type(data_source) is dict:  # dprecated
            for key, data in data_source.items():
                if data.get(identify_field):
                    data_source_key_list.append(data.get(identify_field))
                else:  # workround for some component uses key as identified field e.g: ram
                    data_source_key_list.append(key)
        data_source_key_list = set(data_source_key_list)
        data_identify_val_from_db = set([getattr(obj, identify_field) for obj in data_from_db])
        data_only_in_db = data_identify_val_from_db - data_source_key_list  # delete all this from db
        data_only_in_data_source = data_source_key_list - data_identify_val_from_db  # add into db
        print('\033[31;1mdata_only_in_db:\033[0m', data_only_in_db)
        print('\033[31;1mdata_only_in_data source:\033[0m', data_only_in_data_source)
        self.__delete_components(all_components=data_from_db, delete_list=data_only_in_db,
                                 identify_field=identify_field)
        if data_only_in_data_source:
            self.__add_components(model_obj_name=model_obj_name, all_components=data_source,
                                  add_list=data_only_in_data_source, identify_field=identify_field)

    def __add_components(self, model_obj_name, all_components, add_list, identify_field):
        model_class = getattr(models, model_obj_name)
        will_be_creating_list = []
        print('--add component list:', add_list)
        if type(all_components) is list:
            for data in all_components:
                if data[identify_field] in add_list:
                    # print data
                    will_be_creating_list.append(data)
        elif type(all_components) is dict:  # deprecated
            for k, data in all_components.items():
                # workround for some components uses key as identified field ,e.g ram
                if data.get(identify_field):
                    if data[identify_field] in add_list:
                        # print k,data
                        will_be_creating_list.append(data)
                else:  # if the identified field cannot be found from data set,then try to compare the dict key
                    if k in add_list:
                        data[
                            identify_field] = k  # add this key into dict , because this dict will be used to create new component item in DB
                        will_be_creating_list.append(data)

        # creating components
        try:
            for component in will_be_creating_list:
                data_set = {}
                for field in model_class.auto_create_fields:
                    data_set[field] = component.get(field)
                data_set['asset_id'] = self.asset_obj.id
                obj = model_class(**data_set)
                obj.save()
                print('\033[32;1mCreated component with data:\033[0m', data_set)
                log_msg = "Asset[%s] --> component[%s] has justed added a new item [%s]" % (
                    self.asset_obj, model_obj_name, data_set)
                self.response_msg('info', 'NewComponentAdded', log_msg)
                log_handler(self.asset_obj, 'NewComponentAdded', self.request.user, log_msg, model_obj_name)

        except Exception as e:
            print("\033[31;1m %s \033[0m" % e)
            log_msg = "Asset[%s] --> component[%s] has error: %s" % (self.asset_obj, model_obj_name, str(e))
            self.response_msg('error', "AddingComponentException", log_msg)

    def __delete_components(self, all_components, delete_list, identify_field):
        '''All the objects in delete list will be deleted from DB'''
        deleting_obj_list = []
        print('--deleting components', delete_list, identify_field)
        for obj in all_components:
            val = getattr(obj, identify_field)
            if val in delete_list:
                deleting_obj_list.append(obj)

        for i in deleting_obj_list:
            log_msg = "Asset[%s] --> component[%s] --> is lacking from reporting source data, assume it has been removed or replaced,will also delete it from DB" % (
                self.asset_obj, i)
            self.response_msg('info', 'HardwareChanges', log_msg)
            log_handler(self.asset_obj, 'HardwareChanges', self.request.user, log_msg, i)
            i.delete()

    def __compare_component(self, model_obj, fields_from_db, data_source):
        """
        :param model_obj: 组件对象
        :param fields_from_db: 需要匹配的字段
        :param data_source: 客户端数据
        :return:
        """
        for field in fields_from_db:
            val_from_db = getattr(model_obj, field)
            val_from_data_source = data_source.get(field)
            if val_from_data_source:
                if type(val_from_db) is int:
                    val_from_data_source = int(val_from_data_source)
                elif type(val_from_db) is float:
                    val_from_data_source = float(val_from_data_source)
                elif type(val_from_db) is str:
                    val_from_data_source = str(val_from_data_source).strip()

                if val_from_db == val_from_data_source:  # not change
                    pass
                else:
                    print('\033[34;1m val_from_db[%s]  != val_from_data_source[%s]\033[0m' % (
                        val_from_db, val_from_data_source), type(val_from_db), type(val_from_data_source), field)

                    setattr(model_obj, field, val_from_data_source)
                    model_obj.update_date = timezone.now()
                    log_msg = "资产[%s] --> 组件[%s] --> 字段[%s] 由 [%s] 更改为 [%s]" % (
                        self.asset_obj, model_obj, field, val_from_db, val_from_data_source
                    )
                    self.response_msg('info', 'FieldChanged', log_msg)
                    log_handler(self.asset_obj, 'FieldChanged', self.request.user, log_msg, model_obj)
            else:
                self.response_msg('warning', 'AssetUpdateWarning', "组件 [%s]'的字段 [%s] 没有上报" % (model_obj, field))

        model_obj.save()


def log_handler(asset_obj, event_name, user, detail, component=None):
    """
        (1,u'硬件变更'),
        (2,u'新增配件'),
        (3,u'设备下线'),
        (4,u'设备上线'),
    """
    log_category = {
        1: ['FieldChanged', 'HardwareChanges'],
        2: ['NewComponentAdded'],
    }
    if not user.id:
        user = models.UserProfile.objects.filter(is_superuser=True).last()
    event_type = None
    for k, v in log_category.items():
        if event_name in v:
            event_type = k
            break
    log_obj = models.EventLog(
        name=event_name,
        event_type=event_type,
        asset_id=asset_obj.id,
        component=component,
        detail=detail,
        user_id=user.id
    )

    log_obj.save()
