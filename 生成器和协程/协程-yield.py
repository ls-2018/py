import time


def customer():
    # 接受任务
    while 1:
        x = yield
        print(x)


def producer():
    """生产数据"""
    g = customer()
    next(g)
    for i in range(5):
        g.send(i)


producer()
