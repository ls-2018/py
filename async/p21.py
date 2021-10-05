import asyncio
from functools import partial as func


class SchedulerLoop(asyncio.SelectorEventLoop):
    def __init__(self):
        super(SchedulerLoop, self).__init__()
        self._scheduled_callback_futures = []

    def _future(self, done_hook):
        fut = self.create_future()
        fut.add_done_callback(func(
            self.unwrapper, function=done_hook
        ))
        return fut

    @staticmethod
    def unwrapper(fut: asyncio.Future, function):
        return function()

    def _scheduled_callback_futures(self, callback, *args, context=None):
        fut = self._future(func(callback, *args))
        self._scheduled_callback_futures.append(fut)
        self.call_soon_threadsafe(fut.set_result, None, context=context)

    def schedule_soon_threadsafe(self, callback, *args, context=None):
        fut = self._future(func(callback, *args))
        self._scheduled_callback_futures.append(fut)
        self.schedule_soon_threadsafe(fut.set_result, None, context=context)

    def schedule_soon(self, callback, *args, context=None):
        fut = self._future(func(callback, *args))
        self._scheduled_callback_futures.append(fut)
        self.call_soon(fut.set_result, None, context=context)

    def schedule_later(self, delay_in_seconds, callback, *args, context=None):
        fut = self._future(func(callback, *args))
        self._scheduled_callback_futures.append(fut)
        self.call_later(delay_in_seconds, fut.set_result, None, context=context)

    def schedule_at(self, delay_in_seconds, callback, *args, context=None):
        fut = self._future(func(callback, *args))
        self._scheduled_callback_futures.append(fut)
        self.call_at(delay_in_seconds, fut.set_result, None, context=context)

    async def await_callbacks(self):
        callbacks_futs = self._scheduled_callback_futures[:]
        self._scheduled_callback_futures[:] = []
        await asyncio.gather(*callbacks_futs)


async def main(loop: SchedulerLoop):
    loop.schedule_soon_threadsafe(print, 'hallo')
    loop.schedule_soon(print, 'this will be printed when the loop starts running')

    def callback(value):
        print(value)

    loop.schedule_soon_threadsafe(func(callback, value='this will get printed when the loop start running'))
    offset_in_seconds = 4
    loop.schedule_at(loop.time() + offset_in_seconds,
                     func(print, f'this will be printed after {offset_in_seconds} seconds'))

    loop.schedule_later(offset_in_seconds, func(print, f"this will be printed after {offset_in_seconds} seconds too"))
    await loop.await_callbacks()


loop = SchedulerLoop()
loop.run_until_complete(main(loop))

# todo 跑步起来
