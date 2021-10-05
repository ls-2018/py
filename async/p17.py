import asyncio

import sys


async def main():
    await asyncio.sleep(1)
    print('hello')


loop = asyncio.new_event_loop()
try:
    loop.run_until_complete(main())
finally:
    try:
        loop.run_until_complete(loop.shutdown_asyncgens())  # 清理任何未被完全消耗的异步生成器
    finally:
        loop.close()
