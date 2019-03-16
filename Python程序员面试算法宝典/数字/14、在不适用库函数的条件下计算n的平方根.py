"""
f(x) = x*x -50
f'(x) = 2x


y = f(x0) + f'(x0)(x-x0)
--->x1 = x0- f(x0)/f'(x0) = x0 - x0/2 + a/2x0 = 0.5(x0 + a/x0)

"""


def square(n, e):
    """
    :param n:
    :param e: 精度
    :return:
    """

    new_one = n
    last_one = 1
    while new_one - last_one > e:
        new_one = (new_one + last_one) / 2
        last_one = n / new_one
    return new_one


if __name__ == '__main__':
    n = 50
    e = 0.000001
    print(n, '的平方根为：', square(n, e))
    n = 4
    print(n, '的平方根为：', square(n, e))
