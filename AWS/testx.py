# encoding=utf-8
"""
@Time: 2019/7/8 10:09
@Author: liushuo
@File: get_data.py
@Desc:
@Software: PyCharm
"""
"""
936669166135            支付用户账号ID
"""

import boto3
import pandas as pd

#
s3 = boto3.resource('s3')
bucket = s3.Bucket('s3-billing')
data1 = data2 = None
for obj in bucket.objects.all():
    if '936669166135-aws-billing-csv-2017-10.csv' == obj.key:
        data1 = pd.read_csv(obj.get()['Body'])
    if '936669166135-aws-billing-csv-2017-09.csv' == obj.key:
        data2 = pd.read_csv(obj.get()['Body'])
print(data1, data2)

for k, v in enumerate(list(data1.index)):
    data1.loc[list(data1.index)[-1] + k] = list(data2.loc[k])
print(data1)

#   2017,1-2018-12 获取对应的 年和月
import time

# 2017-09
s1 = "2018-02-09"
s2 = "2019-01-09"
res1 = time.strptime(s1, '%Y-%m-%d')
res2 = time.strptime(s2, '%Y-%m-%d')

y = res1.tm_year
m = res1.tm_mon
fin = []
while res2.tm_year >= y:
    for i in range(1, 13):
        if res2.tm_year > y:
            if y == res1.tm_year and i < m:
                continue
            temp = (y, i)
            fin.append(temp)
            if i == 12:
                y += 1

        elif res2.tm_year == y:
            if i <= res2.tm_mon:
                temp = (y, i)
                fin.append(temp)
            else:
                y += 1
                break

print(fin)

demo = [(2018, 2), (2018, 3), (2018, 4), (2018, 5), (2018, 6), (2018, 7), (2018, 8), (2018, 9), (2018, 10), (2018, 11),
        (2018, 12), (2019, 1)]
for i in demo:
    print("-%04d-%s.csv" % (i[0], str(i[1]).zfill(2)))
# [[fill]align][sign][#][0][width][,][.precision][type]
