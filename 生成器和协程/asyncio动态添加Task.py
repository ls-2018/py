import asyncio
import threading

# 所有run系列的函数都是阻塞的

ioloop = asyncio.get_event_loop()


def start_loop(_loop):
    asyncio.set_event_loop(_loop)
    _loop.run_forever()


async def wget(url):
    print('开始加载%s...' % url)
    reader, writer = await asyncio.open_connection(url, 80)
    header = "GET / HTTP/1.0\r\nHost: %s\r\n\r\n" % url
    writer.write(header.encode('utf8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        # print(line)
    print('ok')
    writer.close()


threading.Thread(target=start_loop, args=(ioloop,)).start()
for url in ['www.163.com', 'www.baidu.com', 'www.sina.com']:
    asyncio.run_coroutine_threadsafe(wget(url), ioloop)

# coro = asyncio.sleep(1, result=3)
# future = asyncio.run_coroutine_threadsafe(coro, ioloop)
# assert future.result() == 3
#
# ioloop.close()

'''
Task对象, 用于动态的添加任务的
方法： 
    立即加到事件循环
    task = asyncio.create_task(协程对象)    
    task = loop.create_task(协程对象)
    task = loop.ensure_future(协程对象)
    
    
    task.add_done_callback(func)
'''
# loop.run_in_executor(executor, say_baa)
# loop.call_soon(functools.partial(print, "Hello", flush=True))
# loop.call_soon_threadsafe(functools.partial(print, "Hello", flush=True))

# ioloop.call_soon(display_date, loop.time() + 5.0, loop)
# ioloop.call_later(3, callback, loop)
# ioloop.call_later(3, functools.partial(print, "Hello", flush=True))
# a = ioloop.call_at(
#     ioloop.time() + 5,
#     functools.partial(print, "Hello", flush=True)
# )
# a.cancel()  # 取消回调函数的执行,依旧会阻塞
# ioloop.call_soon_threadsafe(run, 4, url)  # 同步任务
# loop.run_until_complete(asyncio.wait([say_baa]))
# ioloop.run_until_complete(print_sum(1, 2))
# ioloop.run_until_complete(asyncio.gather(
#     factorial("A", 2),
# ))
# 利用gather 将多个协程封装为一个协程,gather执行完成后会返回results一个任务列表
# 利用wait 将多个协程封装为一个协程,wait执行完成后会返回dones,pending两个任务列表
