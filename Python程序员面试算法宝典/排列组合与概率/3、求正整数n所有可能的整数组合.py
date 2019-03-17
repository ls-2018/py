"""
给定一个正整数n，求解出所有和为n的整数组合，要求组合按照递增方式展示，而且唯一
"""


# 递归
# def getAllCombination(sums, result, count):
#     """
#     求和为 sums的所有整数组合
#     :param sums: 正整数,进入当前函数的需要分割的数,
#     :param result: 存储组合结果
#     :param count: count存储组合中的个数
#     :return:
#     """
#     if sums < 0:
#         return
#     if sums == 0:
#         # 数组的组合满足和为sums的条件,打印所有组合
#         print('满足条件的组合')
#         i = 0
#         while i < count:
#             print(result[i], end=' ')
#             i += 1
#         print()
#         return
#     # 确定组合中下一个取值
#     i = 1 if count == 0 else result[count - 1]
#
#     while i <= sums:
#         result[count] = i
#         count += 1
#         getAllCombination(sums - i, result, count)  # 求和为 sums-1的组合
#         count -= 1  # 递归完成后,去掉最后一个组合的数字
#         i += 1  # 找下一个数字作为组合中的数字


def getAllCombination_2(n, result):
    if n == 0:
        print(result, '-------')
        return
    temp = result[-1]
    i = max(1, temp)
    while i <= n:
        result.append(i)
        getAllCombination_2(n - i, result)
        result.pop()
        i += 1


def showAllCombination(n):
    """
    找到和为n的所有整数的组合
    :param n:
    :return:
    """
    if n < 1:
        print('参数不符合要求')
        return
    result = [0]  # 存储和为n的组合方式
    # getAllCombination(n, result, 0)
    getAllCombination_2(n, result)


if __name__ == '__main__':
    showAllCombination(4)
