# 构造法
def isPower_1(n):
    """时间复杂度O(logn)"""
    if n < 1:
        return False
    i = 1
    while i <= n:
        if i == n:
            return True
        i <<= 1
    return False


# 与操作法
def isPower_2(n):
    """时间复杂度O(1)"""
    """
    如果一个数是2的n次方,那么对应的二进制位,只有1位是1,  因此可以转化为求是否只有1个1 ;
    如果是,那么  n  与  n-1的每一位都不相同,
    """
    if n < 1:
        return False
    m = n & (n - 7)  # 求n的几次方,这里后边的整数就变成n-1
    return m == 0


if __name__ == '__main__':
    print(isPower_2(8))
    print(isPower_2(4))
