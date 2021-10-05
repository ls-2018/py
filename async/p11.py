"""
使用multiprocessing构建跨平台解决方案,在进程本地事件循环中运行多个协程
通过这种方式，可以绕过GIL强加的Cpython限制,
并利用asyncio提高I、O密集型任务上的单核CPU使用率
"""
from multiprocessing import Process
import asyncio
import os
import random
import typing

process = []


def cleanup():
    global process
    while process:
        proc = process.pop()  # type: Process
        try:
            proc.join()
        except KeyboardInterrupt:
            proc.terminate()


async def worker():
    random_delay = random.randint(0, 3)
    result = await asyncio.sleep(random_delay, result=f"working in process:{os.getpid()}")
    print(result)


def process_main(coro_worker: typing.Callable, num_of_coroutines: int):
    print(f'pid:{os.getpid()}')
    loop = asyncio.get_event_loop()  # 都可以，因为在主线程中
    loop = asyncio.new_event_loop()
    try:
        workers = [coro_worker() for _ in range(num_of_coroutines)]
        loop.run_until_complete(asyncio.gather(*workers, loop=loop))
    except KeyboardInterrupt:
        print(f"Stopping {os.getpid()}")
        loop.stop()
    finally:
        loop.close()


def main(processes: list, num_procs, num_coros, process_main):
    for _ in range(num_coros):
        proc = Process(target=process_main, args=(worker, num_procs))
        processes.append(proc)
        proc.start()


if __name__ == '__main__':
    try:
        main(process, 10, 2, process_main)
    except KeyboardInterrupt:
        print('CTRL+C ')
    finally:
        cleanup()
        print('cleanup finished')
