"""
第7章/asgi_socketio/server.py
"""

import socketio, os

SERVER_ROOT = os.path.dirname(__file__)

# 创建一个 AsyncServer 实例
sio = socketio.AsyncServer()

app = socketio.ASGIApp(sio, static_files={
    # 配置静态文件目录为服务器应用目录下的 static 目录，这
    # 样可以使用 Socket.IO 内置的静态文件服务器处理静态请求
    "/static": os.path.join(SERVER_ROOT, "static")
})
