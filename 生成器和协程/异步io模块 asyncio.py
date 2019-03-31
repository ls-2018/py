# 协程 + 事件循环

import asyncio


async def func():  # async关键字不能和yield一起使用，引入coroutine装饰器来装饰downloader生成器。
    print('start')
    # 异步调用asyncio.sleep(1):
    await asyncio.sleep(1)  # time.sleep 异步的接口 对象 必须实现__await__
    # await 就相当于 yield from
    print('end')


# 获取EventLoop:
loop = asyncio.get_event_loop()
task1 = loop.create_task(func())
task2 = loop.create_task(func())
# 执行coroutine
loop.run_until_complete(asyncio.wait([task1, task2]))
# loop.run_until_complete(func())


# asyncio是一个底层模块
# 他完成了几个任务的轮流检测io,并且在遇到io的时候能够及时在任务之间进行切换
# 然后达到使用单线程实现异步的方式

# aiohttp
# 完全使用asyncio作为底层模块完成的


# loop 你的循环
# 你的协程任务就是 被async语法约束的 函数
# 你的协程任务遇到io才能切出去,如何标识你的任务遇到io了呢? await 对象

# async 语法 帮助我们创建协程任务
# asyncio模块 : 异步io模块 对协程任务的循环管理 内置了很多异步的接口帮助我们 异步的socketserver,采用异步的形式去访问socket server
