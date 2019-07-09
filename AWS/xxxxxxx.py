# encoding=utf-8

import pandas as pd
import numpy as np

data = pd.read_csv(r'D:\Destop\123.csv', dtype={'LinkedAccountId': np.object})

link_user = '515743265704'
# instance_name = 'dacproes2uatinstance' # 实例名字

tag_name = 'user:' + 'appenv'  # 标签名
tag_value = 'dac-uat'  # 标签名

# user_unique = list(data['LinkedAccountId'].unique())
# if user_unique[-1] == np.nan:
#     user_unique.remove(np.nan)

user_i = [True if i == link_user else False for i in list(data['LinkedAccountId'])]
data = data.loc[user_i]

# instance_i = [True if i == instance_name else False for i in list(data['aws:cloudformation:logical-id'])]
# data = data.loc[instance_i]


tag_i = [True if i == tag_value else False for i in list(data[tag_name])]
data = data.loc[tag_i]

# res = data[tag_name].notnull()
# a = data.loc[res]  # 这个标签有值的索引

# 各服务名字        AmazonS3

#       ProductCode
service_list = list(data['ProductCode'].unique())
for service in service_list:
    service_i = [True if i == service else False for i in list(data['ProductCode'])]
 
    temp = dict()
    temp['CostBeforeTax'] = data.loc[service_i, 'CostBeforeTax'].sum()
    temp['Credits'] = data.loc[service_i, 'Credits'].sum()
    temp['TaxAmount'] = data.loc[service_i, 'TaxAmount'].sum()
    temp['UsageQuantity'] = data.loc[service_i, 'UsageQuantity'].sum()
    temp['TotalCost'] = data.loc[service_i, 'TotalCost'].sum()
    print(service, temp)
 