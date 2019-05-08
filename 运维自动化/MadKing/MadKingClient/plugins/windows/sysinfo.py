# _*_coding:utf-8_*_
__author__ = 'Alex Li'

import platform
import win32com
import wmi
import os


def collect():
    data = {
        'os_type': platform.system(),
        'os_release': "%s %s  %s " % (platform.release(), platform.architecture()[0], platform.version()),
        'os_distribution': 'Microsoft',
        'asset_type': 'server'
    }
    win32obj = Win32Info()
    data.update(win32obj.get_cpu_info())
    data.update(win32obj.get_ram_info())
    data.update(win32obj.get_server_info())
    data.update(win32obj.get_disk_info())
    data.update(win32obj.get_nic_info())

    # for k,v in data.items():
    #    print k,v
    return data


class Win32Info(object):
    def __init__(self):
        self.wmi_obj = wmi.WMI()
        self.wmi_service_obj = win32com.client.Dispatch("WbemScripting.SWbemLocator")
        self.wmi_service_connector = self.wmi_service_obj.ConnectServer(".", r"root\cimv2")

    def get_cpu_info(self):
        data = {}
        cpu_lists = self.wmi_obj.Win32_Processor()
        cpu_core_count = 0

        for cpu in cpu_lists:
            cpu_core_count += cpu.NumberOfCores
            cpu_model = cpu.Name
        data["cpu_count"] = len(cpu_lists)
        data["cpu_model"] = cpu_model
        data["cpu_core_count"] = cpu_core_count
        return data

    def get_ram_info(self):
        data = []
        ram_collections = self.wmi_service_connector.ExecQuery("Select * from Win32_PhysicalMemory")
        for item in ram_collections:
            item_data = {}
            # print item
            mb = int(1024 * 1024)
            ram_size = int(item.Capacity) / mb
            item_data = {
                "slot": item.DeviceLocator.strip(),  # 槽位
                "capacity": ram_size,  # 容量
                "model": item.Caption,
                "manufactory": item.Manufacturer,  # 生产商
                "sn": item.SerialNumber,
            }
            data.append(item_data)
        # for i in data:
        #    print i
        return {"ram": data}

    def get_server_info(self):
        computer_info = self.wmi_obj.Win32_ComputerSystem()[0]
        system_info = self.wmi_obj.Win32_OperatingSystem()[0]
        data = dict()
        data['manufactory'] = computer_info.Manufacturer
        data['model'] = computer_info.Model
        data['wake_up_type'] = computer_info.WakeUpType
        data['sn'] = system_info.SerialNumber
        # print data
        return data

    def get_disk_info(self):
        data = []
        for disk in self.wmi_obj.Win32_DiskDrive():
            # print(disk.Model,disk.Size,disk.DeviceID,disk.Name,disk.Index,disk.SerialNumber,disk.SystemName,disk.Description)
            item_data = {}
            iface_choices = ["SAS", "SCSI", "SATA", "SSD"]
            for iface in iface_choices:
                if iface in disk.Model:
                    item_data['iface_type'] = iface
                    break
            else:
                item_data['iface_type'] = 'unknown'
            item_data['slot'] = disk.Index
            item_data['sn'] = disk.SerialNumber
            item_data['model'] = disk.Model
            item_data['manufactory'] = disk.Manufacturer
            item_data['capacity'] = int(disk.Size) / (1024 * 1024 * 1024)
            data.append(item_data)
        return {'physical_disk_driver': data}

    def get_nic_info(self):
        data = []
        for nic in self.wmi_obj.Win32_NetworkAdapterConfiguration():
            if nic.MACAddress is not None:
                item_data = {}
                item_data['macaddress'] = nic.MACAddress
                item_data['model'] = nic.Caption
                item_data['name'] = nic.Index
                if nic.IPAddress is not None:
                    item_data['ipaddress'] = nic.IPAddress[0]
                    item_data['netmask'] = nic.IPSubnet
                else:
                    item_data['ipaddress'] = ''
                    item_data['netmask'] = ''
                bonding = 0
                # print nic.MACAddress ,nic.IPAddress,nic.ServiceName,nic.Caption,nic.IPSubnet
                # print item_data
                data.append(item_data)
        return {'nic': data}


if __name__ == "__main__":
    print(collect())
"""
demo = {
    'os_type': 'Windows',
    'os_release': '10 64bit  10.0.17763 ',
    'os_distribution': 'Microsoft',
    'asset_type': 'server',
    'cpu_count': 1,
    'cpu_model': 'Intel(R) Core(TM) i7-5500U CPU @ 2.40GHz',
    'cpu_core_count': 2,
    'ram': [
        {
            'slot': 'ChannelA-DIMM0',
            'capacity': 4096.0,
            'model': '物理内存',
            'manufactory': 'Micron',
            'sn': '00000000'
        },
        {
            'slot': 'ChannelB-DIMM0',
            'capacity': 8192.0,
            'model': '物理内存',
            'manufactory': 'Kingston',
            'sn': '122B977C'
        }
    ],
    'manufactory': 'ASUSTeK COMPUTER INC.',
    'model': 'X555LB',
    'wake_up_type': 6,
    'sn': '00330-80000-00000-AA199',
    'physical_disk_driver': [
        {
            'iface_type': 'unknown', 'slot': 1,
            'sn': 'S32XJ9EG612232', 'model': 'ST1000LM024 HN-M101MBB',
            'manufactory': '(标准磁盘驱动器)',
            'capacity': 931.510956287384
        },
        {
            'iface_type': 'SSD',
            'slot': 0,
            'sn': '174623803967',
            'model': 'SanDisk SDSSDH3250G',
            'manufactory': '(标准磁盘驱动器)',
            'capacity': 232.8834843635559
        }
    ],
    'nic': [
        {
            'macaddress': '28:C2:DD:68:C9:ED',
            'model': '[00000001] Qualcomm Atheros AR956x Wireless Network Adapter',
            'name': 1,
            'ipaddress': '',
            'netmask': ''
        },
        {
            'macaddress': '30:5A:3A:BD:DB:68',
            'model': '[00000002] Realtek PCIe GbE Family Controller',
            'name': 2,
            'ipaddress': '10.92.3.47',
            'netmask': ('255.255.255.0', '64')
        },
        {
            'macaddress': '8C:E2:20:52:41:53',
            'model': '[00000012] WAN Miniport (IP)',
            'name': 12,
            'ipaddress': '',
            'netmask': ''
        },
        {
            'macaddress': '90:60:20:52:41:53',
            'model': '[00000013] WAN Miniport (IPv6)',
            'name': 13,
            'ipaddress': '',
            'netmask': ''
        },
        {
            'macaddress': '94:CD:20:52:41:53',
            'model': '[00000014] WAN Miniport (Network Monitor)', 'name': 14,
            'ipaddress': '', 'netmask': ''},

    ]
}
"""