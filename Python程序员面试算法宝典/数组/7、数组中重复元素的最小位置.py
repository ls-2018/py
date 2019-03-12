"""
给定了两个数字num1 num2 ，求这两个数字在数组中出现的位置的最小距离
"""
# 双重遍历Ｏ(n*n)


# 动态规划
"""
一次遍历，
遇到num1  标记为lastPos1,  与上一次遍历到的num2下标的位置的值lastPos2的差
遇到num2  标记为lastPos2,  与上一次遍历到的num1下标的位置的值lastPos2的差

这俩差，一直取最小
"""


def minDistance(array, num1, num2):
    if array is None or len(array) == 0:
        print('参数不合理')
        return
    lastPos1 = -1  # 上次遍历到num1的位置
    lastPos2 = -1  # 上次遍历到num2的位置
    minDis = 2 ** 32  # num１与ｎｕｍ２的最小位置
    for i in range(len(array)):
        if array[i] == num1:
            lastPos1 = i
            if lastPos2 >= 0:
                minDis = min(minDis, lastPos1 - lastPos2)
        elif array[i] == num2:
            lastPos2 = i
            if lastPos1 >= 0:
                minDis = min(minDis, lastPos2 - lastPos1)
    return minDis


if __name__ == '__main__':
    array = [4, 5, 6, 4, 7, 4, 6, 4, 7, 8, 5, 6, 4, 3, 10, 8]
    num1 = 4
    num2 = 8
    print(minDistance(array, num1, num2))
