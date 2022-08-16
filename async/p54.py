# 等待多个协程并忽略异常
import asyncio
import sys


async def print_delay(delay, text):
    print(await asyncio.sleep(delay, text))


async def raise_delayed(delay, text):
    raise Exception(await asyncio.sleep(delay, text))


async def main():
    workload = [
        print_delay(5, 'a'),
        raise_delayed(2, 'b'),
        print_delay(5, 'c'),
    ]
    res = None
    try:
        # gather 等待所有任务执行完毕
        # return_exceptions=False直接抛出异常，return_exceptions=True,会将异常对象放在res里
        gathered = asyncio.gather(*workload, return_exceptions=True)
        res = await gathered
    except asyncio.CancelledError:
        print('the gathered task was cancelled', file=sys.stderr)
    finally:
        print('res:', res)


asyncio.run(main())
