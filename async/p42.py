# 协程超时
import asyncio


async def delayed_print(text, delay):
    print(await asyncio.sleep(delay, result=text))


async def main():
    delay = 3
    on_time_coro = delayed_print(f'i will print after{delay} seconds', delay)
    await asyncio.wait_for(on_time_coro, delay + 1)
    try:
        delayed_coro = delayed_print(f'i will print after {delay + 1} seconds', delay + 1)
        await asyncio.wait_for(delayed_coro, delay)
    except asyncio.TimeoutError:
        print(f'i timed out after {delay} seconds')


asyncio.run(main())
   