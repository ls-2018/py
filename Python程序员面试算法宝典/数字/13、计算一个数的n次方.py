# 方法１：蛮力
"""
当计算出 2^50 后，没必要再乘50个2 了，直接用前面的结果平方
"""

# 递归法
"""
    n>0 首先计算2^(n/2)的值tmp,如果n为奇数，计算结果=tmp*tmp*d，如果为偶数，不用在乘d
    
    n<0 首先计算2^(|n/2|)的值tmp,如果n为奇数，计算结果=1/(tmp*tmp*d)，如果为偶数，不用在乘d
"""


def power(d, n):
    if n == 0:
        return 1
    if n == 1:
        return d

    tmp = power(d, abs(n) // 2)

    if n > 0:
        if n % 2 == 1:
            return tmp * tmp * d
        else:
            return tmp * tmp
    else:
        if n % 2 == 1:
            print(1 / (tmp * tmp * d))
            return 1 / (tmp * tmp * d)
        else:
            return 1 / (tmp * tmp)


if __name__ == '__main__':
    print(power(3, 3))
