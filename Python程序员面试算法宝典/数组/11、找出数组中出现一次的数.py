"""
[1,2,4,5,6,4,2],唯一的数有1,5,6只要输出其中一个就行;前提条件不唯一的都是偶数次

"""


def isOne(n, i):
    """
    判断n的二进制数从右往左数第i位为1
    :param n:
    :param i:
    :return:
    """
    return n >> i & 1 == 1


def findSingle(array):
    size = len(array)
    i = 0
    while i < 32:
        result1 = result0 = count0 = count1 = 0
        j = 0
        while j < size:
            if isOne(array[j], i):
                result1 ^= array[j]  # 第i位为1的值亦或操作
                count1 += 1  # 第i为为1的数字个数
            else:
                result0 ^= array[j]
                count0 += 1
            j += 1
        i += 1
        if count1 % 2 == 1 and result0 != 0:
            return result1
        if count0 % 2 == 1 and result1 != 0:
            return result0
    return -1


if __name__ == '__main__':
    arr = [6, 5, 9, 4, 4, 3, 3]
    result = findSingle(arr)
    if result != -1:
        print(result)
    else:
        print('没找到')
