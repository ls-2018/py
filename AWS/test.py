# encoding=utf-8
"""
@Time: 2019/7/2 17:07 
@Author: liushuo
@File: test.py 
@Desc: 
@Software: PyCharm
"""
# import json
#
# data = open('index.json', 'r', encoding='utf8').read()
# print(list(json.loads(data).get('terms').get('OnDemand').keys()))
import boto3

# client = boto3.client('s3')
# print(client.get_bucket_versioning(Bucket='asd123412423412'))
# import boto3, json
#
# client = boto3.client('iam')
# iam = boto3.resource('iam')
# response = client.list_users(
#     PathPrefix='/',
# )
# user_list=[]
# for i in response['Users']:
#     user_list.append(i['UserName'])
finally_dict = {}
finally_dict.setdefault('未分组', {}).setdefault('user', [])
print(finally_dict)
