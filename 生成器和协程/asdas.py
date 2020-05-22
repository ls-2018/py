import asyncio
import threading

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
# 给时间循环添加新任务
# ioloop.call_soon_threadsafe(run, 4, url)  # 同步任务
