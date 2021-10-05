import asyncio

loop = asyncio.get_event_loop()
loop.call_soon(print, "i am scheduled on a loop")
loop.call_soon_threadsafe(print, 'i am scheduled on a loop but threadsafe ')
loop.call_later(1, print, 'i am scheduled on a loop in one second')
loop.call_at(loop.time() + 1, print, 'i am scheduled on a loop in one second')
try:
    loop.run_forever()
except KeyboardInterrupt:
    loop.stop()
finally:
    loop.close()
