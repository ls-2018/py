import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tushare
import datetime
import dateutil

d = {'open': [1, 2, 3]}
d2 = {'opxen': [1, 2, 3]}
bm_df = pd.DataFrame(data=d,  )
bm_df2 = pd.Series([1, 2, 3])
bm_df['x'] = bm_df2
print(bm_df)