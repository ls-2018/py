import matplotlib.pyplot as plt
import mpl_finance as fin
from matplotlib.dates import date2num
import pandas as pd

df = pd.read_csv('test.csv', parse_dates=['date'], index_col=['date'], sep='\s+')[['open', 'close', 'high', 'low']]
df['time'] = date2num(df.index.to_pydatetime())

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1)  # 创建子图实例，传入第一参数

arr = df[['time', 'open', 'close', 'high', 'low']].values  # 获取序列化值，传入第二参数

fin.candlestick_ochl(ax, arr)  # 把子图和数据传入


plt.show()
