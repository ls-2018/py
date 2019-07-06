# encoding=utf-8
"""
@Time: 2019/7/5 17:57 
@Author: liushuo
@File: get_object.py 
@Desc: 
@Software: PyCharm
"""

import boto3
from datetime import datetime

client = boto3.client('s3')
objs = client.list_objects(Bucket='l2c-web')
while 'index.html' in objs.keys():
    objs_contents = objs['Contents']
    for i in range(len(objs_contents)):
        filename = objs_contents[i]['Key']



# print(response)
