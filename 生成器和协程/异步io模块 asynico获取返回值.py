import asyncio

# 执行任务获取返回值
'''

async def hello():
    print("Hello world!")
    await asyncio.sleep(1)
    print("Hello again!")
    return 'done'

loop = asyncio.get_event_loop()
task = loop.create_task(hello())
loop.run_until_complete(task)


ret = task.result()
print(ret)
'''
# 执行多个任务按照返回的顺序获取返回值
import asyncio


async def hello(i):
    print("Hello world!", i)
    await asyncio.sleep(i)
    print("Hello again!")
    return 'done', i



async def main():
    tasks = []
    for i in range(5):
        tasks.append(asyncio.ensure_future(hello((20 - i) / 10)))

    for res in asyncio.as_completed(tasks):
        result = await res
        print(result)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
