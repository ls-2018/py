import asyncio
import threading
from threading import Thread

# 循环存在与循环策略的上下文中,
# DefaultEventLoopPolicy 检查每个线程的循环并且不允许通过asyncio.get_event_loop()在主线程之外创建循环
asyncio.get_event_loop()


def create_event_loop_thread(worker, *args, **kwargs):
    def _worker(*args, **kwargs):
        # 线程本地事件循环
        loop = asyncio.new_event_loop()
        print(id(loop))
        asyncio.set_event_loop(loop)
        try:
            loop.run_until_complete(worker(*args, **kwargs))
        finally:
            loop.close()

    return Thread(target=_worker, args=args, kwargs=kwargs)


async def print_coro(*args, **kwargs):
    print(f"inside the print coro on {threading.get_ident()}", flush=True)


if __name__ == '__main__':
    workers = [create_event_loop_thread(print_coro) for i in range(10)]
    for thread in workers:
        thread.start()
    for thread in workers:
        thread.join()
