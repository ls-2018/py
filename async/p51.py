# 使用不同的启发式方式等待多个协程
# asyncio.wait_for()
# asyncio.gather()
import asyncio


async def raiser():
    raise Exception("An exception was raised")


async def main():
    raiser_future = asyncio.ensure_future(raiser())
    hello_world_future = asyncio.create_task(asyncio.sleep(1, 'i have returned'))
    # coros = {raiser_future, hello_world_future, raiser()}
    coros = {raiser_future, hello_world_future}
    """
    不要将协程直接传递给asyncio.wait,而是要先通过asyncio.create_task或loop.create_task将把他们泵装成一个任务。这样做的理由是
    使用asyncio.ensure_future将协程封装在asyncio.wait内部，可以使future实例保持不变。不能使用协程来检查asyncio.wait的返回集的内部状态
    -----协程的（完成、等待）状态
    
    asyncio.wait比asyncio.gather 更低级,因为他可以用于对协程进行分组，但是不能用于取消协程。
    
    """

    # finished, pending = await asyncio.wait(coros, return_when=asyncio.ALL_COMPLETED)
    # finished, pending = await asyncio.wait(coros, return_when=asyncio.FIRST_COMPLETED)
    finished, pending = await asyncio.wait(coros, return_when=asyncio.FIRST_EXCEPTION)
    assert raiser_future in finished
    assert raiser_future not in pending
    assert hello_world_future not in finished
    assert hello_world_future in pending
    err_war_thrown = None
    print(raiser_future.exception())
    try:
        print(hello_world_future.result())
    except asyncio.InvalidStateError as err:
        err_war_thrown = err
    assert err_war_thrown


asyncio.run(main())
