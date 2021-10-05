import os
import tempfile
import time
from concurrent.futures.thread import ThreadPoolExecutor
from contextlib import asynccontextmanager
import asyncio


class Sync:
    def __init__(self):
        self.pending = []
        self.finished = None

    def schedule_coro(self, coro, shield=False):
        # todo 到底有什么区别
        fut = asyncio.shield(coro) if shield else asyncio.ensure_future(coro)
        self.pending.append(fut)
        return fut

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.finished = await asyncio.gather(*self.pending, return_exceptions=True)


async def workload():
    print(time.time())
    await asyncio.sleep(3)
    return 42


async def main():
    async with Sync() as sync:
        sync.schedule_coro(workload())
        sync.schedule_coro(workload())
        sync.schedule_coro(workload())
        sync.schedule_coro(workload())
    print(sync.finished)


asyncio.run(main())
print(time.time(), '---')
