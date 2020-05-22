import asyncio

loop = asyncio.get_event_loop()


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print("Task %s: Compute factorial(%s)..." % (name, i))
        await asyncio.sleep(1, result=number)
        f *= i
    print("Task %s: factorial(%s) = %s" % (name, number, f))


loop.run_until_complete(asyncio.gather(
    factorial("A", 2),
    factorial("B", 3),
    factorial("C", 4),
))
coro = asyncio.sleep(1, result=3)
future = asyncio.run_coroutine_threadsafe(coro, loop)
assert future.result() == 3

loop.close()
