# ###############################   不使用加减乘除操作符    ###########################################################

# 置函数:bin()、oct()、int()、hex()可


def add_jia(n1, n2):
    """
    不使用加减乘除实现加法
        不考虑进位的二进制加法,可以用 亦或  实现
            只考虑进位,  可以用 与,然后左移一位,与上面相加,
            如果有进位,重复上面;没有-->结束
    以下方法不能计算负数
    """
    sums = 0  # 不进位相加结果
    carry = 0  # 保存进位值
    while carry != 0:
        sums = n1 ^ n2  # 亦或代替不进位相加
        carry = (n1 & n2) << 1  # 与操作代替计算进位值
        n1 = sums
        n2 = carry

    return sums


def add(a, b):
    import ctypes
    a = ctypes.c_int32(a).value
    b = ctypes.c_int32(b).value
    while b != 0:
        carry = ctypes.c_int32(a & b).value
        a = ctypes.c_int32(a ^ b).value
        b = ctypes.c_int32(carry << 1).value

    return a


MAX_BIT = 2 ** 32
MAX_BIT_COMPLIMENT = -2 ** 32


def add_2(a, b):
    """模拟整形溢出"""
    while b != 0:
        if b == MAX_BIT:
            return a ^ MAX_BIT_COMPLIMENT
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a


def multi(a, b):
    """
        乘法
        二进制,乘1左移对应的位数,相加
    """
    neg = (a > 0) ^ (b > 0)
    # 根据neg,确定结果的正负
    if b < 0:
        b = add(~b, 1)
    if a < 0:
        a = add(~a, 1)
    result = 0
    # key =1 想左移位后的值,value移位的次数即位置编号
    bit_position = dict()
    # 计算出1向左移动(0,1,2,3...31)位的值
    i = 0
    while i < 32:
        bit_position[1 << i] = i
        i += 1

    while b > 0:
        # 计算出最后一位1的位置编号
        position = bit_position[b & ~(b - 1)]
        result += (a << position)
        b &= b - 1  # 去掉最后一位1
    if neg:
        result = add(~result, 1)
    return result


if __name__ == '__main__':
    # print('add_jia', add_jia(2, 4))  # 在计算负数相加时,会有问题
    print(add(-1, 3))
    print(add(50, add(~3, 1)))  # a - b = a + (-b) = a + (~b) + 1
    print(multi(11, 12))
