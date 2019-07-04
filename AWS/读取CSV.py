# encoding=utf-8
"""
@Time: 2019/7/4 16:55 
@Author: liushuo
@File: 读取CSV.py 
@Desc: 
@Software: PyCharm
"""
import pandas as pd

data = pd.read_csv('D:\\Destop\\book\\AWS\\936669166135-aws-billing-csv-2019-01.csv')

account_total = data['RecordID']
i_list = [True if i.startswith('AccountTotal:') else False for i in list(account_total)]
temp = account_total[account_total[i_list].index]

print(data['CostBeforeTax'][temp.index[0]])
print(data['Credits'][temp.index[0]])
print(data['TaxAmount'][temp.index[0]])
