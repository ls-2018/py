# # """
# # @Time: 2019/6/23 17:40
# # @Author: liushuo
# # @File: __init__.py
# # @Desc:
# # @Software: PyCharm
# # """
# #
# #
# # # import random, asyncio
# # #
# # #
# # # async def ask_for_potato():
# # #     await asyncio.sleep(random.random())
# # #
# # #
# # # ask_for_potato()
# # # async def async_function():
# # #     return 1
# #
# #
# # # async def await_coroutine():
# # #     result = await async_function()
# # #     print(result)
# # #
# # #
# # # await_coroutine().send(None)
# # #
# # #
# # # def run(coroutine):
# # #     try:
# # #         coroutine.send(None)
# # #     except StopIteration as e:
# # #         return e.value
# # #
# # #
# # # run(await_coroutine())
# # async def divide(x, y):
# #     print('-')
# #     return x / y
# #
# #
# # #
# # #
# # # def bad_call():
# # #     # This should raise a ZeroDivisionError, but it won't because
# # #     # the coroutine is called incorrectly.
# # #     print(divide(1, 2).asend(None))
# # #     print(divide(1, 2).ag_running)
# # #
# # #
# # # bad_call()
# # async def good_call():
# #     # await will unwrap the object returned by divide() and raise
# #     # the exception.
# #     a = await divide(1, 0)
# #     print(a)
# #
# #
# # from tornado.ioloop import IOLoop
# #
# # IOLoop.current().spawn_callback(divide, 1, 0)
# from tornado import gen
#
#
# async def x():
#     print(1)
#     return 2
#
#
# async def minute_loop():
#     while True:
#         await x()
#         await gen.sleep(1)
#
#
# from tornado.ioloop import IOLoop
#
# io_loop = IOLoop.current()
# io_loop.run_sync(minute_loop)
# from urllib.parse import urlencode
#
# url = '='
# url += "?" + urlencode(dict(next='--------'))
# print(url)
print(bool(None))
print(None == False)
from tornado.web import gen

gen.coroutine
