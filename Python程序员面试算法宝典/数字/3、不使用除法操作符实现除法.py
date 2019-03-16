# 直接相减
def divide_1(m, n):
    print(m, "除以", n, )
    res = 0
    while m > n:
        m = m - n
        res += 1
    print('商为:', res, '          余数为:', m)


# 移位法
def divide_2(m, n):
    """时间复杂度O(log(m/n))"""
    print(m, "除以", n, )
    result = 0
    while m >= n:
        multi = 1
        while multi * n <= (m >> 1):
            multi <<= 1
        result += multi
        m -= multi * n
    print('商为:', result, '          余数为:', m)


if __name__ == '__main__':
    divide_1(14, 4)
    divide_2(14, 4)
