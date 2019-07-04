# encoding=utf-8
"""
@Time: 2019/7/4 11:56 
@Author: liushuo
@File: testx.py 
@Desc: 
@Software: PyCharm
"""
import boto3
from datetime import datetime

client = boto3.client('cloudwatch')
response = client.get_metric_data(
    MetricDataQueries=[
        {
            'Id': 'm1',  # 随便写，小写字母开头，唯一
            'MetricStat': {
                'Metric': {
                    'Namespace': 'AWS/EC2',
                    # 'MetricName': 'CPUCreditUsage',
                    'MetricName': 'DiskReadOps',  # 指标
                    'Dimensions': [
                        {
                            'Name': 'InstanceId',  # 指标的参数
                            'Value': 'i-03821c70f8b32025e'
                        },
                    ]
                },
                'Period': 60 * 60 * 24,
                'Stat': 'Average',
                # 'Unit': 'Seconds',
            },
            # 'Expression': 'string',
            # 'Label': 'string',
            'ReturnData': True
        },
    ],
    StartTime=datetime(2019, 6, 1),
    EndTime=datetime(2019, 7, 4),
    # NextToken='string',
    # ScanBy='TimestampDescending',
    # MaxDatapoints=123
)
print(response)
