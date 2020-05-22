# 1. 回调过深造成代码很难维护
# 2. 栈撕裂造成异常无法向上抛出

# 协程： 可以被暂停并切换到其他协程运行的函数  Vs. 线程

from tornado.gen import coroutine


async def yield_test():
    yield 1
    yield 2
    yield 3


async def main():
    await yield_test()


async def main2():
    await yield_test()


yielder = yield_test()
for item in yielder:
    print(item)
