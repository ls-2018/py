# 直接计算
def isPower_1(n):
    if n < 1:
        print(n, '不是自然数')
        return False
    i = 0
    while i < n:
        m = i * i
        if m == n:
            print(n, '是%s的平方数' % i)
            return
        elif m > n:
            print(n, '不是平方数')
            return
        i += 1
    print(n, '不是平方数')


# 二分查找
def isPower_2(n):
    low = 1
    high = n
    while low < high:
        mid = (low + high) // 2
        power = mid * mid
        if power > n:
            high = mid - 1
        elif power < n:
            low = mid + 1
        else:
            print(n, '是%s的平方数' % mid)
            return True
    print(n, '不是平方数')


# 减法运算法
def isPower_3(n):
    temp = n
    # n^2 = (1 + (2*(n-1))* n / 2 = (n-1)^2 + 2(n-1)  + 1 =  1 + 3  + ...  +(2*(n-1) +1 )
    minus = 1
    while n > 0:
        n = n - minus
        if n == 0:
            print(temp, '是%s的平方数' % ((minus + 1) // 2))
            return
        elif n < 0:
            print(temp, '不是平方数')
            return
        else:
            minus += 2
    print(temp, '不是平方数')
    return


if __name__ == '__main__':
    # isPower_1(15)
    # isPower_1(16)
    # isPower_2(16)
    # isPower_2(161)
    isPower_3(16)
    isPower_3(15)
