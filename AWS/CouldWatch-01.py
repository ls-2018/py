"""
@Time: 2019/7/2 12:46 
@Author: liushuo
@File: CouldWatch-01.py 
@Desc: 
@Software: PyCharm
"""
import boto3
from datetime import datetime

client = boto3.client('cloudwatch', )
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
# #     AlarmName='Default_Test_Alarm3',
# #     HistoryItemType='ConfigurationUpdate',
# #     StartDate=datetime(2015, 1, 1),
# #     EndDate=datetime(2019, 7, 2),
# #     MaxRecords=50,  # 小于等于100
# #     # NextToken=None
# # )
# # # #  'ConfigurationUpdate' | 'StateUpdate' | 'Action',
# # print(response)
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
response = client.describe_alarms(
    # AlarmNames=['Default_Test_Alarm3', ],
    # AlarmNamePrefix='TargetTracking-table',
    StateValue='ALARM',
    ActionPrefix='TargetTracking-table',
    MaxRecords=100,
    # NextToken='string'
)  # 'OK' | 'ALARM' | 'INSUFFICIENT_DATA',
print(response)
# ###################################   can_paginate    #############################################

# ###################################   can_paginate    #############################################

# ###################################   can_paginate    #############################################
# ###################################   can_paginate    #############################################

# ###################################   can_paginate    #############################################

# ###################################   can_paginate    #############################################
# ###################################   can_paginate    #############################################
