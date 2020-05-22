'''
# asyncio orm + 同步mysql(使用concurrent 来结合两者)
'''
import time
import asyncio
import concurrent

def func():
    '''同步耗时操作'''
    time.sleep(2)
    return 'ok'


async def main():
    loop = asyncio.get_running_loop()

    fut = loop.run_in_executor(None, func)
    # 1、运行默认的executor (thread) ,调用submit方法申请一个县城区执行一个func函数,并返回一个concurrent.futures.Future对象
    # 2、调用asyncio.warp_future对上面对象进行封装
    result = await fut

    print(result)


asyncio.run(main())
