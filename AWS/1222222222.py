# encoding=utf-8

import pandas as pd

data = pd.read_csv(r'D:\Destop\123.csv')
user_tag = []
# for i in list(data.columns):
#     if i.startswith('user:'):
#         user_tag.append(i)
# print(user_tag)
print(data['user: appenv'].isnull())
# print(data.isnull())
