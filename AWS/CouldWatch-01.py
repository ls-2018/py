"""
@Time: 2019/7/2 12:46 
@Author: liushuo
@File: CouldWatch-01.py 
@Desc: 
@Software: PyCharm
"""
import boto3

client = boto3.client('cloudwatch')
# aws cloudwatch list-metrics --namespace AWS/EC2       指定 AWS/EC2 命名空间以查看 Amazon EC2 的所有指标
# List alarms of insufficient data through the pagination interface
# 检查是否可以对操作进行分页
demo = [
    'delete_alarms',
    'delete_dashboards',
    'describe_alarm_history',
    'describe_alarms',
    'describe_alarms_for_metric',
    'disable_alarm_actions',
    'enable_alarm_actions',
    'get_dashboard',
    'get_metric_data',
    'get_metric_statistics',
    'get_metric_widget_image',
    'list_dashboards',
    'list_metrics',
    'list_tags_for_resource',
    'put_dashboard',
    'put_metric_alarm',
    'put_metric_data',
    'set_alarm_state',
    'tag_resource',
    'untag_resource']
throw_err = ['generate_presigned_url',
             'get_paginator',
             'get_waiter']
# print(dir(client))

# ###################################   can_paginate    #############################################
# for i in demo:
#     try:
#         print(i, client.can_paginate(i))
#     except Exception as e:
#         print(e)
""" 
describe_alarm_history True
describe_alarms True 
get_metric_data True 
list_dashboards True
list_metrics True 


CloudWatch.Paginator.DescribeAlarmHistory
CloudWatch.Paginator.DescribeAlarms
CloudWatch.Paginator.GetMetricData
CloudWatch.Paginator.ListDashboards
CloudWatch.Paginator.ListMetrics
"""
# ###################################   delete_alarms    #############################################

# client.delete_alarms(
#     AlarmNames=['cpu-mon', ]
# )

# ###################################   delete_dashboards    #############################################
# demo = client.delete_dashboards(
#     DashboardNames=[
#         'test',
#     ])
# print(demo)
"""
{
    'ResponseMetadata': {
        'RequestId': 'b5222ce2-9cb5-11e9-b67b-112d4243e83d',
        'HTTPStatusCode': 200,
        'HTTPHeaders': {
            'x-amzn-requestid': 'b5222ce2-9cb5-11e9-b67b-112d4243e83d',
            'content-type': 'text/xml',
            'content-length': '246',
            'date': 'Tue, 02 Jul 2019 10:39:44 GMT'
        },
        'RetryAttempts': 0
    }
}
"""

# ###################################   describe_alarm_history     #################################
# 检索指定警报的历史记录

# response = client.describe_alarm_history(
#     AlarmName='Default_Test_Alarm3',
#     HistoryItemType='ConfigurationUpdate',
#     StartDate=datetime(2015, 1, 1),
#     EndDate=datetime(2019, 7, 2),
#     MaxRecords=50,  # 小于等于100
#     # NextToken=None
# )
# #  'ConfigurationUpdate' | 'StateUpdate' | 'Action',
# print(response)
"""
{
    'AlarmHistoryItems': [],
    'ResponseMetadata': {
        'RequestId': '9a2d94f2-9cb6-11e9-b5ef-09bc043668d6',
        'HTTPStatusCode': 200,
        'HTTPHeaders': {
            'x-amzn-requestid': '9a2d94f2-9cb6-11e9-b5ef-09bc043668d6',
            'content-type': 'text/xml',
            'content-length': '314',
            'date': 'Tue, 02 Jul 2019 10:46:09 GMT'
        },
        'RetryAttempts': 0
    }
}
"""

# ###################################   describe_alarms     #############################################
# 检索指定的警报。如果未指定警报，则返回所有警报。
# response = client.describe_alarms(
#     # AlarmNames=['Default_Test_Alarm3', ],
#     # AlarmNamePrefix='TargetTracking-table',
#     StateValue='ALARM',
#     ActionPrefix='TargetTracking-table',
#     MaxRecords=100,
#     # NextToken='string'
# )  # 'OK' | 'ALARM' | 'INSUFFICIENT_DATA',
# print(response)


# ###################################   describe_alarms_for_metric    #########################################
# 检索指定度量标准的警报
# response = client.describe_alarms_for_metric(
#     MetricName='ConsumedWriteCapacityUnits',
#     Namespace='AWS/DynamoDB',
#     Statistic='Sum',
#     # ExtendedStatistic='string',
#     Dimensions=[
#         {
#             'Name': 'TableName',
#             'Value': 'mytodo'
#         },
#     ],
#     Period=60,
#     # Unit='Percent',
# )
# import json
#
# print(response)
# print(json.dumps(response, indent=4))
#     Statistic='SampleCount'|'Average'|'Sum'|'Minimum'|'Maximum',
#     Unit='Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|
#     'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'
#     |'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'
#     |'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None'

# ###################################   disable_alarm_actions    #############################################
# 禁用指定警报的操作,当警报的操作被禁用时，警报状态发生变化时不会执行警报操作
# response = client.disable_alarm_actions(
#     AlarmNames=[
#         'Default_Test',
#     ]
# )
# print(response)

# ###################################   enable_alarm_actions    #############################################
# 启用指定警报的操作。
# response = client.enable_alarm_actions(
#     AlarmNames=[
#         'Default_Test',
#         'TargetTracking-table/mytodo-AlarmLow-89650795-ecfc-4bfd-bd3c-3fb64312c588'
#     ]
# )
# print(response)

# ###################################   generate_presigned_url  失败   #############################################
# 给定客户端，方法和参数，生成预签名URL
# response = client.generate_presigned_url(
#     'HEAD',
#     # region_name="cn-north-1",
# )
# print(response)

# ###################################   get_dashboard    #############################################
# 显示您指定的仪表板的详细信息。
# response = client.get_dashboard(
#     DashboardName='test'
# )
# print(response)
# AttributeError: 'CloudWatch' object has no attribute 'get_dashboard'


# ###################################   get_metric_data     #############################################
# response = client.get_metric_data(
#     MetricDataQueries=[
#         {
#             'Id': 'm1',  # 随便写，小写字母开头，唯一
#             'MetricStat': {
#                 'Metric': {
#                     'Namespace': 'AWS/EC2',
#                     'MetricName': 'StatusCheckFailed_Instance',  # 指标
#                     'Dimensions': [
#                         {
#                             'Name': 'InstanceId',  # 指标的参数
#                             'Value': 'i-088f1053834c3805c'
#                         },
#                     ]
#                 },
#                 'Period': 60 * 60 * 24,
#                 'Stat': 'Average',
#                 # 'Unit': 'Seconds',
#             },
#             # 'Expression': 'string',
#             # 'Label': 'string',
#             'ReturnData': True
#         },
#     ],
#     StartTime=datetime(2019, 6, 1),
#     EndTime=datetime(2019, 7, 1),
#     # NextToken='string',
#     # ScanBy='TimestampDescending',
#     # MaxDatapoints=123
# )
# print(response)
"""
{
    'MetricDataResults': [
        {
            'Id': 'm1',
            'Label': 'StatusCheckFailed_Instance',
            'Timestamps': [
                datetime.datetime(2019, 6, 28, 0, 0, tzinfo=tzutc()),
                datetime.datetime(2019, 6, 27, 0, 0, tzinfo=tzutc()),
                datetime.datetime(2019, 6, 26, 0, 0, tzinfo=tzutc())
            ],
            'Values': [0.0, 0.0, 0.0],
            'StatusCode': 'Complete'
        }
    ],
    'Messages': [],
    'ResponseMetadata': {
        'RequestId': 'bed566af-9d58-11e9-9c17-8b08f77a2c0b',
        'HTTPStatusCode': 200,
        'HTTPHeaders': {
            'x-amzn-requestid': 'bed566af-9d58-11e9-9c17-8b08f77a2c0b',
            'content-type': 'text/xml',
            'content-length': '784',
            'date': 'Wed, 03 Jul 2019 06:06:49 GMT'
        }, 'RetryAttempts': 0
    }
}

"""
# ###################################   get_metric_statistics    #############################################
# 获取指定度量标准的统计信息。
# response = client.get_metric_statistics(
#     Namespace='AWS/DynamoDB',
#     MetricName='ConsumedWriteCapacityUnits',
#     Dimensions=[
#         {
#             'Name': 'TableName',
#             'Value': 'mytodo'
#         },
#     ],
#     StartTime=datetime(2019, 7, 2),
#     EndTime=datetime(2019, 7, 4),
#     Period=60 * 60,
#     Statistics=[
#         'Sum',
#     ],  # 'SampleCount'|'Average'|'Sum'|'Minimum'|'Maximum',
#     # ExtendedStatistics=[
#     #     'string',
#     # ],
#     # Unit='Seconds'
# )
# print(response)
"""
{
    'Label': 'ConsumedWriteCapacityUnits',
    'Datapoints': [
        {'Timestamp': datetime.datetime(2019, 7, 2, 22, 0, tzinfo=tzutc()), 'Sum': 0.0, 'Unit': 'Count'},
        {'Timestamp': datetime.datetime(2019, 7, 3, 3, 0, tzinfo=tzutc()), 'Sum': 0.0, 'Unit': 'Count'},
        {'Timestamp': datetime.datetime(2019, 7, 2, 12, 0, tzinfo=tzutc()), 'Sum': 0.0, 'Unit': 'Count'},
        {'Timestamp': datetime.datetime(2019, 7, 2, 17, 0, tzinfo=tzutc()), 'Sum': 0.0, 'Unit': 'Count'},
        {'Timestamp': datetime.datetime(2019, 7, 2, 14, 0, tzinfo=tzutc()), 'Sum': 0.0, 'Unit': 'Count'},
        {'Timestamp': datetime.datetime(2019, 7, 2, 4, 0, tzinfo=tzutc()), 'Sum': 0.0, 'Unit': 'Count'},
        {'Timestamp': datetime.datetime(2019, 7, 2, 9, 0, tzinfo=tzutc()), 'Sum': 0.0, 'Unit': 'Count'},
        {'Timestamp': datetime.datetime(2019, 7, 3, 5, 0, tzinfo=tzutc()), 'Sum': 0.0, 'Unit': 'Count'},
        {'Timestamp': datetime.datetime(2019, 7, 2, 1, 0, tzinfo=tzutc()), 'Sum': 0.0, 'Unit': 'Count'},
        {'Timestamp': datetime.datetime(2019, 7, 2, 6, 0, tzinfo=tzutc()), 'Sum': 0.0, 'Unit': 'Count'},
        {'Timestamp': datetime.datetime(2019, 7, 2, 19, 0, tzinfo=tzutc()), 'Sum': 0.0, 'Unit': 'Count'},
        {'Timestamp': datetime.datetime(2019, 7, 3, 0, 0, tzinfo=tzutc()), 'Sum': 0.0, 'Unit': 'Count'},
        {'Timestamp': datetime.datetime(2019, 7, 2, 16, 0, tzinfo=tzutc()), 'Sum': 0.0, 'Unit': 'Count'},
        {'Timestamp': datetime.datetime(2019, 7, 2, 21, 0, tzinfo=tzutc()), 'Sum': 0.0, 'Unit': 'Count'},
        {'Timestamp': datetime.datetime(2019, 7, 2, 11, 0, tzinfo=tzutc()), 'Sum': 0.0, 'Unit': 'Count'},
        {'Timestamp': datetime.datetime(2019, 7, 2, 8, 0, tzinfo=tzutc()), 'Sum': 0.0, 'Unit': 'Count'},
        {'Timestamp': datetime.datetime(2019, 7, 2, 13, 0, tzinfo=tzutc()), 'Sum': 0.0, 'Unit': 'Count'},
        {'Timestamp': datetime.datetime(2019, 7, 3, 2, 0, tzinfo=tzutc()), 'Sum': 0.0, 'Unit': 'Count'},
        {'Timestamp': datetime.datetime(2019, 7, 2, 3, 0, tzinfo=tzutc()), 'Sum': 0.0, 'Unit': 'Count'},
        {'Timestamp': datetime.datetime(2019, 7, 2, 0, 0, tzinfo=tzutc()), 'Sum': 0.0, 'Unit': 'Count'},
        {'Timestamp': datetime.datetime(2019, 7, 3, 4, 0, tzinfo=tzutc()), 'Sum': 0.0, 'Unit': 'Count'},
        {'Timestamp': datetime.datetime(2019, 7, 2, 18, 0, tzinfo=tzutc()), 'Sum': 0.0, 'Unit': 'Count'},
        {'Timestamp': datetime.datetime(2019, 7, 2, 23, 0, tzinfo=tzutc()), 'Sum': 0.0, 'Unit': 'Count'},
        {'Timestamp': datetime.datetime(2019, 7, 2, 15, 0, tzinfo=tzutc()), 'Sum': 0.0, 'Unit': 'Count'},
        {'Timestamp': datetime.datetime(2019, 7, 2, 20, 0, tzinfo=tzutc()), 'Sum': 0.0, 'Unit': 'Count'},
        {'Timestamp': datetime.datetime(2019, 7, 2, 5, 0, tzinfo=tzutc()), 'Sum': 0.0, 'Unit': 'Count'},
        {'Timestamp': datetime.datetime(2019, 7, 2, 10, 0, tzinfo=tzutc()), 'Sum': 0.0, 'Unit': 'Count'},
        {'Timestamp': datetime.datetime(2019, 7, 2, 7, 0, tzinfo=tzutc()), 'Sum': 0.0, 'Unit': 'Count'},
        {'Timestamp': datetime.datetime(2019, 7, 3, 6, 0, tzinfo=tzutc()), 'Sum': 0.0, 'Unit': 'Count'},
        {'Timestamp': datetime.datetime(2019, 7, 3, 1, 0, tzinfo=tzutc()), 'Sum': 0.0, 'Unit': 'Count'},
        {'Timestamp': datetime.datetime(2019, 7, 2, 2, 0, tzinfo=tzutc()), 'Sum': 0.0, 'Unit': 'Count'}],
    'ResponseMetadata': {
        'RequestId': '90609683-9d59-11e9-a2c6-097b44585d0b',
        'HTTPStatusCode': 200,
        'HTTPHeaders': {
            'x-amzn-requestid': '90609683-9d59-11e9-a2c6-097b44585d0b',
            'content-type': 'text/xml',
            'content-length': '4489',
            'vary': 'accept-encoding',
            'date': 'Wed, 03 Jul 2019 06:12:40 GMT'
        },
        'RetryAttempts': 0
    }
}

"""
# ###################################   get_metric_widget_image    #############################################

# response = client.get_metric_widget_image(
#     MetricWidget='CPUSurplusCreditBalance',
#     # OutputFormat=''
# )
# print(response)
# ###################################   get_paginator     #############################################
# describe_alarm_history True
# describe_alarms True
# get_metric_data True
# list_dashboards True
# list_metrics True
# response = client.get_paginator('describe_alarms')
# print(response, type(response))

# ###################################   get_waiter(waiter_name)    #############################################

# ###################################   list_dashboards    #############################################
# response = client.list_dashboards(
#     DashboardNamePrefix='te',
#     # NextToken='string'
# )
# print(response)
"""
{
    'DashboardEntries': [
        {
            'DashboardName': 'test',
            'DashboardArn': 'arn:aws-cn:cloudwatch::936669166135:dashboard/test',
            'LastModified': datetime.datetime(2019, 7, 3, 5, 48, 22, tzinfo=tzutc()),
            'Size': 221
        }
    ],
    'ResponseMetadata': {
        'RequestId': 'eb692ed6-9d64-11e9-ace0-9382dc27f07a',
        'HTTPStatusCode': 200,
        'HTTPHeaders': {
            'x-amzn-requestid': 'eb692ed6-9d64-11e9-ace0-9382dc27f07a',
            'content-type': 'text/xml',
            'content-length': '558',
            'date': 'Wed, 03 Jul 2019 07:33:57 GMT'
        },
        'RetryAttempts': 0
    }
}

"""
# ###################################   list_metrics    #############################################
# 列出指定的指标
# response = client.list_metrics(
#     Namespace='CW EXAMPLE METRICS',
#     MetricName='Default_Test',
#     Dimensions=[
#         {
#             'Name': 'key1',
#             'Value': 'value1'
#         }, {
#             'Name': 'key2',
#             'Value': 'value2'
#         },
#     ],
#     # NextToken='string'
# )
# print(response)
"""
{
    'Metrics': [],
    'ResponseMetadata': {
        'RequestId': 'b68d6c7c-9d65-11e9-83dc-ab9cd459fde0',
        'HTTPStatusCode': 200,
        'HTTPHeaders': {
            'x-amzn-requestid': 'b68d6c7c-9d65-11e9-83dc-ab9cd459fde0',
            'content-type': 'text/xml',
            'content-length': '268',
            'date': 'Wed, 03 Jul 2019 07:39:38 GMT'
        },
        'RetryAttempts': 0
    }
}"""

# ###################################   list_tags_for_resource   失败 #############################################
# response = client.list_tags_for_resource(
#     # ResourceARN='arn:aws-cn:s3:::asd123412423412'
#     ResourceARN='arn:aws-cn:s3:cn-north-1:asd123412423412:db:mysql-db'
# )
# print(response)

# ###################################   put_dashboard    #############################################
# response = client.put_dashboard(
#     DashboardName='string',
#     DashboardBody='string'
# )

# ###################################   put_metric_alarm    #############################################
response = client.put_metric_alarm(
    AlarmName='string',
    AlarmDescription='string',
    ActionsEnabled=True | False,
    OKActions=[
        'string',
    ],
    AlarmActions=[
        'string',
    ],
    InsufficientDataActions=[
        'string',
    ],
    MetricName='string',
    Namespace='string',
    Statistic='SampleCount' | 'Average' | 'Sum' | 'Minimum' | 'Maximum',
    ExtendedStatistic='string',
    Dimensions=[
        {
            'Name': 'string',
            'Value': 'string'
        },
    ],
    Period=123,
    Unit='Seconds' | 'Microseconds' | 'Milliseconds' | 'Bytes' | 'Kilobytes' | 'Megabytes' | 'Gigabytes' | 'Terabytes' | 'Bits' | 'Kilobits' | 'Megabits' | 'Gigabits' | 'Terabits' | 'Percent' | 'Count' | 'Bytes/Second' | 'Kilobytes/Second' | 'Megabytes/Second' | 'Gigabytes/Second' | 'Terabytes/Second' | 'Bits/Second' | 'Kilobits/Second' | 'Megabits/Second' | 'Gigabits/Second' | 'Terabits/Second' | 'Count/Second' | 'None',
    EvaluationPeriods=123,
    DatapointsToAlarm=123,
    Threshold=123.0,
    ComparisonOperator='GreaterThanOrEqualToThreshold' | 'GreaterThanThreshold' | 'LessThanThreshold' | 'LessThanOrEqualToThreshold',
    TreatMissingData='string',
    EvaluateLowSampleCountPercentile='string',
    Metrics=[
        {
            'Id': 'string',
            'MetricStat': {
                'Metric': {
                    'Namespace': 'string',
                    'MetricName': 'string',
                    'Dimensions': [
                        {
                            'Name': 'string',
                            'Value': 'string'
                        },
                    ]
                },
                'Period': 123,
                'Stat': 'string',
                'Unit': 'Seconds' | 'Microseconds' | 'Milliseconds' | 'Bytes' | 'Kilobytes' | 'Megabytes' | 'Gigabytes' | 'Terabytes' | 'Bits' | 'Kilobits' | 'Megabits' | 'Gigabits' | 'Terabits' | 'Percent' | 'Count' | 'Bytes/Second' | 'Kilobytes/Second' | 'Megabytes/Second' | 'Gigabytes/Second' | 'Terabytes/Second' | 'Bits/Second' | 'Kilobits/Second' | 'Megabits/Second' | 'Gigabits/Second' | 'Terabits/Second' | 'Count/Second' | 'None'
            },
            'Expression': 'string',
            'Label': 'string',
            'ReturnData': True | False
        },
    ],
    Tags=[
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
)
# ###################################   put_metric_data    #############################################
0
# ###################################   set_alarm_state    #############################################

# ###################################   tag_resource    #############################################
response = client.tag_resource(
    ResourceARN='string',
    Tags=[
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
)
# ###################################   untag_resource    #############################################
response = client.untag_resource(
    ResourceARN='string',
    TagKeys=[
        'string',
    ]
)
