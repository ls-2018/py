# 等待多个协程
import asyncio
from asyncio import Task
import asyncio


async def print_delayed(delay, text, result):
    print(await asyncio.sleep(delay, text))
    return result


async def main():
    workload = [
        print_delayed(1, 'printing this after 1 second', 1),
        print_delayed(2, 'printing this after 1 second', 2),
        print_delayed(3, 'printing this after 1 second', 3),
    ]
    """
    gather 使用     asyncio.ensure_future() 调度并执行多个协程或future
    入口顺序不一定是协程、future被调度的顺序

    """

    # result = await asyncio.gather(*workload)
    result = ''
    try:
        # result = await asyncio.wait_for(asyncio.gather(*workload), 2)
        # result = await asyncio.wait(workload, timeout=2)
        result = await asyncio.wait(workload)
    except asyncio.TimeoutError:
        pass
    print(result)


if __name__ == '__main__':
    asyncio.run(main())
