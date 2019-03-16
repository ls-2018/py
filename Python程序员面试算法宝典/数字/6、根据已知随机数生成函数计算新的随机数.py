"""
已知随机数生成函数rand7()能产生随机数是整数1-7的均匀分布，如何构造rand10()函数，时期产生的随机数是整数1-10的均匀分布
"""
import random


def rand7():
    return int(random.randint(1, 7))


def rand10():
    x = 0
    while True:
        x = (rand7() - 1) * 7 + rand7()  # {0,1,2,3,4,5,6} * 7 + {1,2,3,4,5,6,7}  = {1 .... 49}  49个整数，几率一样
        if x <= 40:  # 舍弃大于41的数，均匀分布在 1~40，
            break
    return x % 10 + 1  # 将其映射,1-10区间上的整数


if __name__ == '__main__':
    a = set()
    for i in range(1000):
        print(rand10(), end=' ')
        a.add(rand10())
        # a.add(rand7())
    print()
    print(a)
