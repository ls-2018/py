# 发现回调时间长运行的回调函数
import asyncio
import logging
import sys
import time

# logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)


def slow():
    time.sleep(1.5)
    print('over')


async def main():
    loop = asyncio.get_running_loop()
    loop.slow_callback_duration = 1
    loop.call_soon(slow)


asyncio.run(main(), debug=True)
