"""
[1,2,4,5,6,4,2],唯一的数有1,5,6只要输出其中一个就行;前提条件不唯一的都是偶数次

一个奇数个,分成两组,奇数组亦或得到的就是唯一的.

分组依据:唯一的数的二进制位(0,1),肯定能分成两组,其他的数,也依据这个比特位分组

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
    while i < 32:  # int类型在32位机器为32位
        result1 = result0 = count0 = count1 = 0
        j = 0
        while j < size:
            if isOne(array[j], i):  # 判断这个数的第i为是否为1
                result1 ^= array[j]  # 第i位为1的值亦或操作
                count1 += 1  # 第i为为1的数字个数
            else:
                result0 ^= array[j]
                count0 += 1
            j += 1
        i += 1

        # 判断哪一个是奇数组,
        if count1 % 2 == 1 and result0 != 0:  # 如果result0=0 ,不能区分这三个数字,不能将其分配到两个数组内;有可能三个都跑到一个数组内了,因此偶数组编变成了零
            return result1
        if count0 % 2 == 1 and result1 != 0:
            return result0
        """
        假如说,第一次判断第0为是否为1 时,都为0
        ---->result1 = result0 = count0 = count1 = 0
        """


if __name__ == '__main__':
    arr = [6, 5, 9, 4, 4, 3, 3, ]
    result = findSingle(arr)
    if result:
        print(result)
    else:
        print('没找到')
