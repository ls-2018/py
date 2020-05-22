import asyncio
import functools
import datetime

loop = asyncio.get_event_loop()


async def index():
    print(123)
    await asyncio.sleep(5)
    loop.close()


def callback():
    print('-----')


def display_date(end_time, loop):
    print(datetime.datetime.now())
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, display_date, end_time, loop)
    else:
        loop.stop()


async def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    await asyncio.sleep(1.0)
    return x + y


async def print_sum(x, y):
    result = await compute(x, y)
    print("%s + %s = %s" % (x, y, result))


if __name__ == '__main__':
    # 所有run系列的函数都是阻塞的
    # loop.run_until_complete(index(132))
    # loop.call_soon(functools.partial(print, "Hello", flush=True))
    # loop.call_soon_threadsafe(functools.partial(print, "Hello", flush=True))

    # loop.call_soon(display_date, loop.time() + 5.0, loop)
    # loop.call_later(3, callback, loop)
    # loop.call_later(3, functools.partial(print, "Hello", flush=True))
    # a = loop.call_at(
    #     loop.time() + 5,
    #     functools.partial(print, "Hello", flush=True)
    # )
    # a.cancel()  # 取消回调函数的执行,依旧会阻塞
    # print(a, type(a))
    loop.run_until_complete(print_sum(1, 2))

    loop.run_forever()
