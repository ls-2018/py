import time
import asyncio

start = time.time()


async def func():
    await asyncio.sleep(2)
    print(time.time())
    return 123


async def sleep():
    res = await func()
    print(res)
    return '---------'


ioloop = asyncio.get_event_loop()
tasks = []
for i in range(5):
    # ioloop.run_until_complete(sleep())
    task = asyncio.ensure_future(sleep())
    # task = asyncio.create_task(sleep())
    # task.add_done_callback(func)
    tasks.append(task)
    # ioloop.run_until_complete(task)   # 会返回task协程返回的值


async def main():
    for _task in asyncio.as_completed(tasks):
        result = await _task
        print(result)


# 添加任务列表
# ioloop.run_until_complete(asyncio.wait(tasks))  # 利用wait 将多个协程封装为一个协程,wait执行完成后会返回dones,pending两个任务列表
# ioloop.run_until_complete(asyncio.gather(*tasks)) # 利用gather 将多个协程封装为一个协程,gather执行完成后会返回results一个任务列表
ioloop.run_until_complete(main())

# for task in tasks:
#     print(task.result())
print('end time:', time.time() - start)
