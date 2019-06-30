"""
@Time: 2019/6/30 9:34 
@Author: liushuo
@File: async.py 
@Desc: 
@Software: PyCharm
"""
import time
import threading


def genCoroutine(func):
    def wrapper(*args, **kwargs):
        # def func():
        #     print('开始处理reqA')
        #     res = yield longIo()
        #     print('接收到longIo的相应数据：', res)
        #     print('结束处理reqA')

        gen1 = func()  # reqA的生成器
        gen2 = next(gen1)  # longIo的生成器

        def run(g):
            """
            :param g:  longIo的生成器
            :return:
            """
            res = next(g)
            try:
                gen1.send(res)  # 返回给reqA数据
            except StopIteration:
                pass

        threading.Thread(target=run, args=(gen2,)).start()

    return wrapper


# 一个客户单的请求
@genCoroutine
def reqA():
    print('开始处理reqA')
    res = yield longIo()
    print('接收到longIo的相应数据：', res)
    print('结束处理reqA')


# handler 获取数据(数据库、其他服务器，循环耗时)
def longIo():
    print('开始耗时操作')
    time.sleep(5)
    print('结束耗时操作')
    # 返回数据
    yield 'sunck is a good man'


# 另一个客户端的请求
def reqB():
    print('开始处理reqB')
    time.sleep(5)
    print('结束处理reqB')


if __name__ == '__main__':
    print(time.time())
    reqA()
    reqB()
    print(time.time())
