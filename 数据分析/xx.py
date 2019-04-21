import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tushare
import datetime
import dateutil
d = {'open':[1,2,3]}
bm_init=1
bm_df = pd.DataFrame(data=d)
print((bm_df['open'] - bm_init) / bm_init)