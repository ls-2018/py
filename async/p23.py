import asyncio
import random


async def work(i):
    print(await asyncio.sleep(random.randint(0, i)))
    result = f'work {i}'


async def main():
    # print(work(1),type(work(1)))
    # print(asyncio.ensure_future(work(1)),type(asyncio.ensure_future(work(1))))
    # tasks = [asyncio.ensure_future(work(i)) for i in range(10)]
    tasks = [work(i) for i in range(10)]
    await asyncio.gather(*tasks)


asyncio.run(main())





















