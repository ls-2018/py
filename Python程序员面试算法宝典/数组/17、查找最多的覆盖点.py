"""
坐标轴上从左到右依次的点为a[0].....a[n-1]，设一根木棒的长度为L，求L最多能覆盖坐标轴上的几个点?
a[j] -a[i] <=L  && a[j+10] - a[i] >L    这两个条件的j与i中间的所有点个数中的最大值。
前提不存在==L的点
"""


def maxCover(a, L):
    count = 2
    maxCount = 1  # 最长覆盖的点数
    start = 0  # 覆盖坐标的起始位置
    n = len(a)
    i = 0
    j = 1
    while i < n and j < n:
        while (j < n) and (a[j] - a[i] <= L):
            j += 1
            count += 1
        j -= 1
        count -= 1
        if count > maxCount:
            start = i
            maxCount = count
        i += 1
        j += 1
    print('覆盖的坐标点：')
    i = start
    while i < (start + maxCount):
        print(a[i])
        i += 1
    print()
    return maxCount


if __name__ == '__main__':
    a = [1, 3, 7, 8, 10, 11, 12, 13, 15, 16, 17, 19, 25]
    print('最长覆盖点数：', maxCover(a, 8))
