


import asyncio
from threading import Thread


class LoopShowerThread(Thread):
    def run(self) -> None:
        try:
            loop = asyncio.get_event_loop()
            print(loop)
        except RuntimeError:
            print('No event loop!')


loop = asyncio.get_event_loop()  # 只在主线程上创建一个循环
print(loop)
thread = LoopShowerThread()
thread.start()

thread.join()
