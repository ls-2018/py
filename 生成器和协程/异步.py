async def download(url):
    return 'eva'


def run(coroutine):
    try:
        coroutine.send(None)
    except StopIteration as e:
        return e.value


coro = download('http://www.baidu.com/')
ret = run(coro)
print(ret)

"""
async关键字不能和yield一起使用，
"""
import asyncio
import threading
from concurrent.futures import ThreadPoolExecutor

ioloop = asyncio.get_event_loop()


async def wget(url):
    reader, writer = await asyncio.open_connection(url, 80)

    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % url
    writer.write(header.encode('utf8'))
    await writer.drain()
    # 接收到数据
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header --- %s' % url)


def start_loop(_ioloop):
    asyncio.set_event_loop(_ioloop)
    _ioloop.run_forever()


def say_baa():
    i = 0
    while i < 10:
        print('...baa {0}'.format(i))
        i += 1
    return 123


threading.Thread(target=start_loop, args=(ioloop,)).start()

asyncio.run_coroutine_threadsafe(wget('http://www.baidu.com'), loop=ioloop)
executor = ThreadPoolExecutor(2)
loop = asyncio.get_event_loop()
# asyncio.ensure_future(loop.run_in_executor(executor, say_baa))
# asyncio.ensure_future(loop.run_in_executor(executor, say_baa))
# asyncio.ensure_future(loop.run_in_executor(executor, say_baa))
# tasks = []
# for i in range(20):
#     url = "http://shop.projectsedu.com/goods/{}/".format(i)
#     task = loop.run_in_executor(executor, wget, 'http://www.baidu.com')
#     tasks.append(task)
# loop.run_until_complete(asyncio.wait([say_baa]))
# 也就是 asyncio.get_event_loop()。初始情况下，get_event_loop() 只会在主线程帮您创建新的 event loop，
# 并且在主线程中多次调用始终返回该 event loop；而在其他线程中调用 get_event_loop() 则会报错，
# 除非您在这些线程里面手动调用过 set_event_loop()。细节请参考 文档。
