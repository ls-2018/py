# encoding=utf-8
"""
@Time: 2019/7/9 14:17 
@Author: liushuo
@File: asd.py 
@Desc: 
@Software: PyCharm
"""
path = r'D:\Destop\441271182313-aws-cost-allocation-ACTS-2019-04(1) - 副本.csv'
import pandas as pd

data = pd.read_csv(path)
print(data)
