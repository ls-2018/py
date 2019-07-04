"""
@Time: 2019/7/2 12:46 
@Author: liushuo
@File: CouldWatch-01.py 
@Desc: 
@Software: PyCharm
"""
import boto3

cloudwatch = boto3.resource('cloudwatch')
alarm = cloudwatch.Alarm('xasd')

attributes = [
    "actions_enabled",
    'alarm_actions',
    'alarm_arn',
    'alarm_configuration_updated_timestamp',
    'alarm_description',
    'alarm_name',
    'comparison_operator',
    'datapoints_to_alarm',
    'dimensions',
    'evaluate_low_sample_count_percentile',
    'evaluation_periods',
    'extended_statistic',
    'insufficient_data_actions',
    'metric_name',
    'metrics',
    'namespace',
    'ok_actions',
    'period',
    'state_reason',
    'state_reason_data',
    'state_updated_timestamp',
    'state_value',
    'statistic',
    'threshold',
    'treat_missing_data',
    "unit",
    'metric']
for attr in attributes:
    print(getattr(alarm, attr, '-'))
"""
True
['arn:aws-cn:sns:cn-north-1:936669166135:app-test-ypf']
arn:aws-cn:cloudwatch:cn-north-1:936669166135:alarm:xasd
2019-07-03 08:00:40.652000+00:00
DO NOT EDIT OR DELETE. For TargetTrackingScaling policy arn:aws-cn:autoscaling:cn-north-1:936669166135:scalingPolicy:c73c6306-bb5a-41bf-9472-b1e8ac3d86a7:resource/dynamodb/table/mytodo:policyName/DynamoDBWriteCapacityUtilization:table/mytodo.
xasd
GreaterThanOrEqualToThreshold
None
[{'Name': 'InstanceId', 'Value': 'i-03821c70f8b32025e'}]
None
1
None
[]
DiskReadOps
None
AWS/EC2
[]
300
Threshold Crossed: no datapoints were received for 1 period and 1 missing datapoint was treated as [Breaching].
{"version":"1.0","queryDate":"2019-07-03T08:01:28.393+0000","statistic":"Average","period":300,"recentDatapoints":[],"threshold":0.1}
2019-07-03 08:01:28.401000+00:00
ALARM
Average
0.1
breaching
None
cloudwatch.Metric(namespace='AWS/EC2', name='DiskReadOps')
    # action
    # alarm.metric.delete()
    # alarm.metric.describe_history()
    # alarm.metric.disable_actions()
    # alarm.metric.enable_actions()
    # alarm.metric.get_available_subresources()
    # alarm.metric.load()
    # alarm.metric.reload()
    # alarm.metric.set_state()
"""


