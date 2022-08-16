# 取消协程
import asyncio
from asyncio import Task


def method_one():
    async def cancellable(delay=10):
        loop = asyncio.get_running_loop()
        now = loop.time()
        try:
            print(f'sleeping from {now} for {delay} seconds...')
            await asyncio.sleep(delay)
            print(f'sleep {delay} seconds ...')
        except asyncio.CancelledError:
            print(f'Cancelled at {now} after {loop.time() - now} seconds')

    async def main():
        coro = cancellable()
        task = asyncio.create_task(coro)
        await asyncio.sleep(3)
        task.cancel()

    asyncio.run(main())


def method_two():
    async def cancellable(delay=10):
        loop = asyncio.get_running_loop()
        now = loop.time()
        try:
            print(f'sleep from {now} for {delay} seconds ...')
            await asyncio.sleep(delay)
            print(f'slept for {delay} seconds without disturbance ...')
        except asyncio.CancelledError:
            print(f'Cancelled at {now} after {loop.time() - now} seconds')

    async def main():
        coro = cancellable()
        task = asyncio.create_task(coro)  # 不堵塞
        await asyncio.sleep(3)

        def canceller(_task: Task, _fut):
            _task.cancel()
            _fut.set_result(None)

        loop = asyncio.get_running_loop()
        fut = loop.create_future()
        loop.call_soon_threadsafe(canceller, task, fut)
        await fut

    asyncio.run(main())


if __name__ == '__main__':
    method_two()
