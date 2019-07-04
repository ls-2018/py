"""
@Time: 2019/7/4 10:03 
@Author: liushuo
@File: CouldWatch-03.py 
@Desc: 
@Software: PyCharm
"""
import boto3
import json
from datetime import datetime, timedelta


def get_name(obj_list):
    """
    从obj_list中返回Name
    :param obj_list: [
        {
            "Key": "Name",
            "Value": "kinesis-test"
        },
        {
            "Key": "Email",
            "Value": "jinjianqiang@light2cloud.com"
        },
        {
            "Key": "FCDEMO",
            "Value": "test"
        }
    ]
    :return:
    """
    for demo in obj_list:
        if demo.get('Key') == 'Name':
            return demo.get('Value')


def get_data(client, instance_id, target_data):
    """
    根据ec2实例ID ，返回需要的数据。
    :param client:
    :param instance_id:
    :param target_data:
    :return:
    """

    _dict = {}
    for target in target_data:
        response = client.get_metric_data(
            MetricDataQueries=[
                {
                    'Id': 'm1',  # 随便写，小写字母开头，唯一
                    'MetricStat': {
                        'Metric': {
                            'Namespace': 'AWS/EC2',
                            # 'MetricName': 'CPUCreditUsage',
                            'MetricName': target,  # 指标
                            'Dimensions': [
                                {
                                    'Name': 'InstanceId',  # 指标的参数
                                    'Value': instance_id
                                },
                            ]
                        },
                        'Period': 60 * 60,  # * 24,  # 1 天
                        'Stat': 'Average',
                        # 'Unit': 'Seconds',
                    },
                    # 'Expression': 'string',
                    # 'Label': 'string',
                    'ReturnData': True
                },
            ],
            StartTime=datetime.now() - timedelta(days=30),
            EndTime=datetime.now(),
            # NextToken='string',
            # ScanBy='TimestampDescending',
            # MaxDatapoints=123
        )
        _sum = sum(response['MetricDataResults'][0]['Values']) / 30
        _dict[target] = _sum
    return _dict


def run():
    ec2 = boto3.client('ec2')
    client = boto3.client('cloudwatch')
    instances = ec2.describe_instances()
    finally_dict = []
    for attr in instances['Reservations']:
        instance_id = attr['Instances'][0]['InstanceId']
        temp = {
            'Service': 'ec2',
            'Name': get_name(attr['Instances'][0]['Tags']),
            'IP': attr['Instances'][0]['PrivateIpAddress'],
            'InstanceId': attr['Instances'][0]['InstanceId'],
            'Type': attr['Instances'][0]['InstanceType'],
            'OS': attr['Instances'][0].get('Platform'),
            'target': {}
        }
        # -------以 InstanceId 为基准，获取30天内最大值得均值
        # 获取CPU数据
        cpu_target_data = ['CPUUtilization', 'CPUCreditBalance', 'CPUCreditUsage', 'CPUSurplusCreditsCharged',
                           'CPUSurplusCreditBalance']
        temp['target'].update(get_data(client, instance_id, cpu_target_data))
        # 获取内存数据

        # 获取   disk
        cpu_target_data = ['DiskReadOps', 'DiskWriteOps', 'DiskReadBytes', 'DiskWriteBytes']
        temp['target'].update(get_data(client, instance_id, cpu_target_data))
        finally_dict.append(temp)
        print(temp)
    return finally_dict


if __name__ == '__main__':
    data = run()
    with open('监测数据.json', 'w', encoding='utf8') as f:
        f.write(json.dumps(data, indent=4, ensure_ascii=False))
