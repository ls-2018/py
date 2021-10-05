"""
第7章/aiohttp_socketio/server.py
"""

from aiohttp import web
import os, socketio, asyncio, time

SERVER_ROOT = os.path.dirname(__file__)

# 配置 AIOHTTP >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 声明 aiohttp 的路由表
routes = web.RouteTableDef()


# 将对网站根路径的访问用该函数处理
@routes.get("/")
async def home_page(request):
    # 将页面重定向到 /static/index.html 页面
    raise web.HTTPTemporaryRedirect("/static/index.html")


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# 配置 socketio >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 创建 socketio 服务器，异步模式配置为 aiohttp
sio = socketio.AsyncServer(async_mode='aiohttp')


async def echo_task(sid):
    for i in range(1, 6):
        # 向浏览器端发送消息
        await sio.emit(
            "echo",
            f"[{time.strftime('%X')}] Count: {i}",
            sid
        )
        # 等待1秒
        await asyncio.sleep(1)


@sio.event
async def connect(sid, environ):
    """
    连接成功
    """
    asyncio.create_task(echo_task(sid))


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

if __name__ == '__main__':
    # 创建 aiohttp 服务器应用
    app = web.Application()

    # 将aiohttp服务器与socketio服务器关联
    sio.attach(app)

    # 添加静态文件目录
    routes.static("/static", os.path.join(SERVER_ROOT, "static"))
    app.add_routes(routes)
    web.run_app(app)
