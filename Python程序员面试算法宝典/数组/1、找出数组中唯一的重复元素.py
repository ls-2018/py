"""
数字1~1000放在含有1001个元素的数组中，其中只有唯一的一个元素值重复，其他数字只出现一次。
设计一个算法，将重复元素找出来，要求每个元素只能访问一次
"""


# 需要额外的辅助空间
def findDup(array):
    """
    以空间换时间，时间复杂度O(N)
    在数组中找到唯一重复的元素
    :param array:
    :return: 重复元素的值，如果无重复元素则返回-1
    """
    if array is None:
        return -1
    hash_table = dict()

    for i in array:
        if hash_table.get(i) is None:
            hash_table[i] = 1
        else:
            return i


# 累加求和法
def findDup_2(array):
    """风险：元素值太大或数组太长，可能会出现溢出"""
    if array is None:
        return
    lens = len(array)
    real_result = 0
    for i in range(lens):
        real_result += array[i]
    j = 1
    fuck_result = 0
    while j <= 1000:
        fuck_result += j
        j += 1
    return real_result - fuck_result


# 亦或法
def findDup_3(array):
    """
    (1^2^3^4^5)^(1^2^3^4^5^3) = (1^1)^(2^2)^(3^3^3)^(4^4)^(5^5) = 0^0^3^0^0 =3
    :param array:
    :return:
    """
    if array is None:
        return -1
    lens = len(array)
    result = 0
    for i in range(lens):
        result ^= array[i]
    j = 1
    while j <= 1000:
        result ^= j
        j += 1
    return result


if __name__ == '__main__':
    import random

    a = random.randint(1, 1000)
    print(a)
    demo = [i + 1 for i in range(1000)]
    demo.append(a)
    print('空间换时间', findDup(demo))
    print('累加求和法', findDup_2(demo))
    print('亦或法    ', findDup_3(demo))
