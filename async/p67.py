import random
import asyncio
import functools
from concurrent.futures.thread import ThreadPoolExecutor
from dataclasses import dataclass

import asyncio


def method_one():
    # 停止异步生成器
    async def async_gen_coro():
        yield 1
        yield 2
        yield 3

    async def main():
        async_gen = async_gen_coro()
        await async_gen.asend(None)  # 跳过一个yield
        await async_gen.aclose()
        async for i in async_gen:
            print(i)

    asyncio.run(main())


def method_two():
    async def endless_async_gen():
        while True:
            yield 3
            await asyncio.sleep(1)

    async def main():
        async for i in endless_async_gen():
            print(i)

    loop = asyncio.new_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print('')
    finally:
        try:
            loop.run_until_complete(loop.shutdown_asyncgens())
        finally:
            loop.close()


if __name__ == '__main__':
    method_two()
