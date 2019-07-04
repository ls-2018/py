# encoding=utf-8
"""
@Time: 2019/7/4 15:13 
@Author: liushuo
@File: 获取IAM的信息.py 
@Desc: 
@Software: PyCharm
"""
import boto3, json

client = boto3.client('iam')
iam = boto3.resource('iam')
account_summary = client.get_account_summary()
finally_dict = {
    '用户总数': account_summary['SummaryMap']['Users'],
    '角色总数': account_summary['SummaryMap']['Roles'],
    '组数': account_summary['SummaryMap']['Groups'],
}

users_info = client.list_users(
    PathPrefix='/',
)
for _user in users_info['Users']:
    try:
        group_name = list(iam.User(_user['UserName']).groups.all())[0].name  # 无组 下去
        finally_dict.setdefault(group_name, {}).setdefault('user', []).append(_user['UserName'])
        finally_dict.setdefault(group_name, {})['count'] = finally_dict[group_name].get('count', 0) + 1
    except IndexError:
        finally_dict.setdefault('未分组', {}).setdefault('user', []).append(_user['UserName'])
        finally_dict['未分组']['count'] = finally_dict['未分组'].get('count', 0) + 1

print(json.dumps(finally_dict, indent=4, ensure_ascii=False))

# group_list = client.list_groups()
# for group in group_list['Groups']:
#     group_name = group['GroupName']
#     _group = iam.Group(group_name)
#     for user in _group.users.all():
#         finally_dict.setdefault(group_name, {})
#         print(user)
#         finally_dict[group_name].setdefault('user', []).append(user.name)
#         finally_dict[group_name]['count'] = finally_dict[group_name].get('count', 0) + 1
