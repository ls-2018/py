"""


uvloop 是asyncio 事件循环的替代方案

区别：
    uvloop  第三方;效率大于官方
    asyncio 官方

pip install uvloop
"""
import asyncio
import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy)

# 编写asyncio代码，和之前一样
# 内部的时间循环会自动变为uvloop
asyncio.run()

