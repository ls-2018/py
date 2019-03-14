import datetime

start = datetime.datetime.today()
sum = 0
demo = 10 ** 7
print(demo)
for i in range(demo):
    sum += 1
print(datetime.datetime.today() - start)

"""
如果要想在1s之内解决问题  ---> 也就是10^8次加法


O(N^2)算法，可以处理大约10^4级别的数据

"""
