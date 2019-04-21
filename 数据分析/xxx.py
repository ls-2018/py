# import numpy as np
# import pandas as pd
#
# dict = {'a': [1, 2, 3, 4], 'b': [2, 3, 4, 7]}
# demo = pd.DataFrame(data=dict)
# print(demo)
# print(len(demo))# 每个元素的长度
#
# print(demo['a'])  # series
# print(demo[['a','b']])# 切列




import datetime
demo1 = datetime.datetime.strptime('2018-01-01','%Y-%m-%d',)
demo2 = datetime.datetime.strptime('2018-02-01','%Y-%m-%d',)
date = demo2-demo1
print(date,type(date))
print(date.total_seconds())

print(datetime.timedelta(seconds=date.total_seconds()))