import random


# demo = [1, 2, 3, 4, 5, 9, 6, 7, 8, ]
# print(random.choices(demo, k=3))

# 上边是简单方法,下边有一个相对麻烦的
def getRandom(a, m):
    """
    :param a:   源数据数组
    :param m:   获取的个数
    :return:
    """

    assert m < len(a), '获取的数据长度,不能超过数组长度'
    # 断言  不符合 ,就抛错
    i = 0
    while i < m:
        j = random.randint(i, len(a) - 1)
        a[i], a[j] = a[j], a[i]
        i += 1
    print(a[0:m])


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 9, 6, 7, 8, ]

    getRandom(a, 5)
