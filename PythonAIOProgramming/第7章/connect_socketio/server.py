"""
第7章/connect_socketio/server.py
"""

import socketio, os

SERVER_ROOT = os.path.dirname(__file__)

# 创建一个 AsyncServer 实例
sio = socketio.AsyncServer(
    # 配置该服务器的异步模式为 asgi
    async_mode='asgi',
    # 配置该服务器允许来自所有域的连接
    cors_allowed_origins="*"
)


@sio.event
async def my_event(sid):
    pass
    """
    侦听浏览器端发来的 ping 消息，并向该连接发回 pong 消息
    :param sid: Socket.IO 为该连接编码的唯一标识
    :param data: 通过该事件传来的数据
    :return:
    """

    # 向该连接发回 pong 消息
    await sio.emit("my_event_callback", to=sid)


@sio.event
async def login(sid, data):
    # 该函数的返回值将作为浏览器端回调函数的传入参数传给浏览器端
    return f"Hello {data['name']}, you are granted!"


app = socketio.ASGIApp(sio, static_files={
    # 配置静态文件目录为服务器应用目录下的 static 目录，这
    # 样可以使用 Socket.IO 内置的静态文件服务器处理静态请求
    "/static": os.path.join(SERVER_ROOT, "static")
})
