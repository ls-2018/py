import numpy as np
import pandas as pd

dict = {'a': [1, 2, 3, 4], 'b': [2, 3, 4, 7]}
demo = pd.DataFrame(data=dict)
print(demo)
print(len(demo))# 每个元素的长度

print(demo['a'])  # series
print(demo[['a','b']])# 切列
