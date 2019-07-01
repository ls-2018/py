"""
@Time: 2019/7/1 18:53 
@Author: liushuo
@File: S3-1.py 
@Desc: 
@Software: PyCharm
"""
import boto3
import config

s3 = boto3.resource('s3', **config.S3_Setting)  # choice service

# Print out bucket names
for bucket in s3.buckets.all():  # bucket  name
    print(bucket.name)

# Upload a new file
data = open('./images/test.png', 'rb')
# 要先创建库
s3.Bucket('liushuo-test').put_object(Key='test.png', Body=data)
