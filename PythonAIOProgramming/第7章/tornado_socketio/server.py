"""
第7章/aiohttp_socketio/server.py
"""

import os, socketio, asyncio, time
import tornado.web
import tornado.ioloop

SERVER_ROOT = os.path.dirname(__file__)

# 创建 socketio 服务器，异步模式配置为 tornado
sio = socketio.AsyncServer(async_mode='tornado')


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


if __name__ == '__main__':
    # 创建 tornado 服务器
    app = tornado.web.Application([
        # 将 socketio 应用映射到 /socket.io/ 路径
        (r"/socket.io/", socketio.get_tornado_handler(sio)),
        (
            r"/static/(.*)",
            tornado.web.StaticFileHandler,
            {"path": os.path.join(SERVER_ROOT, "static")}
        )
    ])

    try:
        app.listen(8000)
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        print("User stopped server")
