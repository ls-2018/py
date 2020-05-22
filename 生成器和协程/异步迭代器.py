import asyncio


class Stu:
    def __init__(self):
        self.num = 100

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.num > 0:
            a = self.num
            self.num -= 1
            return a
        else:
            raise StopAsyncIteration


async def func():
    obj = Stu()
    async for item in obj:
        print(item)


asyncio.run(func())
