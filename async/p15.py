import asyncio
import sys

loop = asyncio.new_event_loop()
asyncio.get_event_loop()
asyncio.set_event_loop(loop)
if sys.platform != 'win32':
    watcher = asyncio.get_child_watcher()
    watcher.attach_loop(loop)

# 使用asyncio.ensure_future()调度第一个协程
# 或者使用loop.call_soon()调度一个同步回调函数
try:
    loop.run_forever()
finally:
    try:
        loop.run_until_complete(loop.shutdown_asyncgens())
    finally:
        loop.close()
