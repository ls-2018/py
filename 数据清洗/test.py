import pandas as pd

demo1 = pd.Series([1, 2, 3, 4, None])
demo2 = pd.Series([1, 2, 3, 4, None, 3])
demo = demo1 + demo2
print(demo)
print(demo.isnull())
print(demo[~demo.isnull()])
