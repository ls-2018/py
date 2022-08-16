# 取消多个协程
import asyncio
from asyncio import Task


async def cancellable(delay=10, *, loop):
    now = loop.time()
    try:
        print(f'sleeping from {now} for {delay} seconds...')
        await asyncio.sleep(delay)
        print(f'sleep for {delay} without disturbance...')
    except asyncio.CancelledError:
        print(f'cancelled at {now} after {loop.time() - now}')


def canceller(_task: Task, _fut):
    _task.cancel()
    _fut.set_result(None)


async def cancel_thread_safe(gathered_tasks, loop):
    fut = loop.create_future()
    loop.call_soon_threadsafe(canceller, gathered_tasks, fut)


async def main():
    loop = asyncio.get_running_loop()
    coros = [cancellable(i, loop=loop) for i in range(10)]
    gathered_tasks = asyncio.gather(*coros)  # 并发调度,不堵塞
    await asyncio.sleep(3)
    await cancel_thread_safe(gathered_tasks, loop)

    try:
        print(await gathered_tasks)
    except asyncio.CancelledError:
        print('was cancelled')


asyncio.run(main())
