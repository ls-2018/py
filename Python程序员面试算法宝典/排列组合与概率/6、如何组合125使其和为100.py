"""
100 个  1   为100
20  个  5   为100
50  个  2   为100
"""


# 方法1
def func_1(n):
    count = 0  # 和为100 的情况
    num1 = n
    num2 = n // 2
    num5 = n // 5
    x = 0
    while x <= num1:
        y = 0
        while y <= num2:
            z = 0
            while z <= num5:
                if x + 2 * y + 5 * z == n:
                    count += 1
                z += 1
            y += 1
        x += 1
    print(count)


# 数字规律法
def func_2(n):
    """
    x+2y+5z=100
    ------>
    x+5z是偶数且  x+5z<=100的个数
    """
    count = 0
    m = 0
    while m <= n:
        count += (m + 2) // 2
        m += 5
    print(count)


if __name__ == '__main__':
    func_1(100)
    func_2(100)
