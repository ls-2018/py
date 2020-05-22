import asyncio
import functools

loop = asyncio.get_event_loop()


async def slow_operation(future):
    await asyncio.sleep(5)
    future.set_result('Future is done!')


def index(args):
    # print('args', args)
    # print('type', type(args))
    print(123)


future = asyncio.Future()
asyncio.ensure_future(slow_operation(future))
future.add_done_callback(functools.partial(index))
loop.run_until_complete(future)
# future.cancel()   # 会抛出异常，----->使用task（future的子类）

print(future.done())
if not future.cancelled():
    print(future.result())

loop.close()
