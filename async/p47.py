# 不允许取消协程
import asyncio
from asyncio import Task


async def cancellable(delay=10):
    now = asyncio.get_running_loop().time()
    try:
        print(f'sleeping from {now} for {delay} seconds...')
        await asyncio.sleep(delay)
        print(f'sleep for {delay} without disturbance...')
    except asyncio.CancelledError:
        print(f'cancelled at {asyncio.get_running_loop().time()} ')


def canceller(_task: Task, _fut):
    _task.cancel()
    _fut.set_result(None)


async def cancel_thread_safe(task, *, delay=3, loop):
    await asyncio.sleep(delay)
    fut = loop.create_future()
    loop.call_soon_threadsafe(canceller, task, fut)
    await fut


async def main():
    complate_time = 10
    cancel_after_secs = 3
    loop = asyncio.get_running_loop()
    coro = cancellable(delay=complate_time)
    # asyncio.shield 不能保护协程不会从内部被取消
    shielded_task = asyncio.shield(coro)
    asyncio.create_task(cancel_thread_safe(shielded_task, delay=cancel_after_secs, loop=loop))
    # await cancel_thread_safe(shielded_task, delay=cancel_after_secs, loop=loop)
    try:
        await shielded_task
    except asyncio.CancelledError:
        print('was cancelled')


asyncio.run(main())
