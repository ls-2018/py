import random
import asyncio


async def random_number_gen(delay, start, end):
    while True:
        yield random.randint(start, end)
        await asyncio.sleep(delay)


async def main():
    async for i in random_number_gen(1, 0, 100):
        print(i)


asyncio.run(main())
