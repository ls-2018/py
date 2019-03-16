"""
10个房间里放着随机的金币，每个房间只能进入一次，并只能在一个房间中拿金币。
策略，前4个房间只看不拿，随后的房间只要看到比钱4个都多的金币，就拿；
    否则，拿最后一个。
"""
import random


def getMaxNum(n):
    """
    总共n个房间，判断用指定的策略是否能拿到最多金币
    """
    if n < 1:
        print('参数不合法')
        return

    a = [None] * n
    # 随机生成N个房间里金币的个数
    i = 0
    while i < n:
        a[i] = random.randint(1, n)
        i += 1

    # 找出前4个房间中最多的金币个数
    max4 = 0
    i = 0
    while i < 4:
        if a[i] > max4:
            max4 = a[i]
        i += 1

    i = 4
    while i < n - 1:
        if a[i] > max4:  # 能拿到最多的金币
            return True
        i += 1
    return False


if __name__ == '__main__':
    monitorCount = 1000
    success = 0
    i = 0
    while i < monitorCount:
        if getMaxNum(10):
            success += 1
        i += 1
    print(success / monitorCount)
