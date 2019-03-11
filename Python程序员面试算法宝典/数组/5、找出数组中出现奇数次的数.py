"""
数组中有N+2个整数，其中，N个数出现了偶数次，2个数出现了奇数次（这两个数不同）。
"""

# 字典法
"""
key(整数) : value(1|0) 第一次添加置为1，第二次置为0，最会找出为1的。
"""

# 亦或法
"""
a,b亦或得到的c,其中二进制有多个1，取第一个为1的位数（也就是a和b中对应的位数有一个为1，而在对应的数组中，最后肯定是由单独的一个数，所引发的。
            ------》把所有对应位为1的在亦或一次；偶数次的没有影响，假设得到的是a，a再与c以后就可以得到b,再与c亦或就可以得到a.
        ）

"""


def get2Num(array):
    if array is None or len(array) < 1:
        print('参数不合理')
        return
    result = 0
    position = 0
    # 计算数组中所有数字亦或的结果
    i = 0
    while i < len(array):
        result = result ^ array[i]
        i += 1
    tmpResult = result  # 临时存储亦或结果

    # 找出亦或结果结果中其中一个位置为1 的位数（如1100，位置为1位数为2和3）
    i = result
    while i & 1 == 0:
        position += 1
        i = i >> 1
    i = 1
    while i < len(array):
        demo = array[i]
        if (demo >> position) & 1 == 1:
            result = result ^ array[i]
        i += 1
    print(result)
    print(result ^ tmpResult)


if __name__ == '__main__':
    array = [3, 5, 6, 6, 5, 7, 2, 2]
    get2Num(array)
