# encoding=utf-8
"""
@Time: 2019/7/10 9:18 
@Author: liushuo
@File: xxx.py 
@Desc: 
@Software: PyCharm
"""
import boto3

# finally_dict = {}
# finally_dict['TotalCost'] = [{'name': '1', 'y': 2}, {'name': '2', 'y': 3},{'name': '3', 'y': 1}]
# finally_dict['TotalCost'] = sorted(finally_dict['TotalCost'], key=lambda x: x['y'])
# print(finally_dict)
# client = boto3.client('s3')
# s3 = boto3.resource('s3')
# response = client.list_buckets()
# print([item['Name'] for item in response['Buckets']])
s3 = boto3.resource('s3')
s3_bucket = 'liushuo-test'
# bucket = s3.Bucket(s3_bucket)
PayerAccountId = '441271182313'
date_time = '2017-10'
import pandas as pd
import numpy as np

type = {
    'CostBeforeTax': np.float,
    'Credits': np.float,
    'TaxAmount': np.float,
    'UsageQuantity': np.float,
    'TotalCost': np.float,
    'UsageStartDate': np.object,
    'UsageEndDate': np.object,
    'PayerAccountId': np.object,
    'LinkedAccountId': np.object,
    'InvoiceID': np.object,
}

# obj = s3.Object(s3_bucket, f'{PayerAccountId}-aws-billing-csv-{date_time}.csv')
obj = s3.Object(s3_bucket, '441271182313-aws-billing-csv-2017-10.csv')
tag_name='user:bgrp'
data = pd.read_csv(obj.get()['Body'], dtype=type)
print(data.columns)
print(data[tag_name])
print(list(data[tag_name].unique()))
