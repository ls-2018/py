"""
第7章/chatroom/server.py
"""

import socketio, os

SERVER_ROOT = os.path.dirname(__file__)

# 创建一个 AsyncServer 实例
sio = socketio.AsyncServer(
    # 配置该服务器的异步模式为 asgi
    async_mode='asgi'
)


# 侦听浏览器端发来的 msg 事件
@sio.event
async def msg(sid, content):
    # 向所有连接终端广播消息
    await sio.emit('msg', {'from': sid, 'content': content})


# 创建一个 ASGIApp 应用，可使用 uvicorn 等协调层实现调用
app = socketio.ASGIApp(
    sio,
    static_files={
        # 配置静态文件目录为服务器应用目录下的 static 目录，这
        # 样可以使用 Socket.IO 内置的静态文件服务器处理静态请求
        "/static": os.path.join(SERVER_ROOT, "static")
    }
)
