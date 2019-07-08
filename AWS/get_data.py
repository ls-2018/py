# encoding=utf-8
"""
@Time: 2019/7/8 10:09 
@Author: liushuo
@File: get_data.py 
@Desc: 
@Software: PyCharm
"""
import boto3
import pandas as pd

# s3 = boto3.resource('s3')
# bucket = s3.Bucket('s3-billing')
# data1 = data2 = None
# for obj in bucket.objects.all():
#     if '936669166135-aws-billing-csv-2017-10.csv' == obj.key:
#         data1 = pd.read_csv(obj.get()['Body'])
#     if '936669166135-aws-billing-csv-2017-9.csv' == obj.key:
#         data2 = pd.read_csv(obj.get()['Body'])

# if data1 and data2:
#     data1.append()


df1 = pd.DataFrame({'a': [1, 2, 3, 4, 5], 'b': [1, 2, 3, 5, 4], 'c': [1, 2, 3, 5, 4], 'd': [1, 2, 3, 5, 4]})

# s = pd.Series([16, 17, 1, 2], index=df1.columns)
# df = df1.append(s, )

# s = pd.Series([16, 17, 18, 19], name='E', index=df.index)
# df = pd.concat([df, s], axis=1)
df = pd.DataFrame({}).append([{'A': 16, 'B': 17, 'C': 18, 'D': 19}, {'A': 20, 'B': 21, 'C': 22, 'D': 23}],
                             ignore_index=True)
# df.loc[3] = [16, 17, 18, 19]

df2 = pd.DataFrame({}).append([{'A': 116, 'B': 117, 'C': 118, 'D': 191}, {'A': 210, 'B': 211, 'C': 122, 'D': 213}],
                              ignore_index=True)

for k, v in enumerate(list(df2.index)):
    df1.loc[list(df1.index)[-1] + k] = list(df2.loc[k])  # df2.iloc[k]
    # print(v)
print(df1)
"""
    A   B   C   D
0  16  17  18  19
1  20  21  22  23
3  16  17  18  19
"""
# df = df.append([1, 2, 3, 4], ignore_index=True)
"""
      A     B     C     D    0
0  16.0  17.0  18.0  19.0  NaN
1  20.0  21.0  22.0  23.0  NaN
2   NaN   NaN   NaN   NaN  1.0
3   NaN   NaN   NaN   NaN  2.0
4   NaN   NaN   NaN   NaN  3.0
5   NaN   NaN   NaN   NaN  4.0
"""
# s = pd.Series([16, 17, 18, 19])
# df = pd.concat([df, s])
