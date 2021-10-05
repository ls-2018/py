"""
第7章/asgi_websocket/server.py
"""

import asyncio, os

SERVER_ROOT = os.path.dirname(__file__)


async def handle_lifespan(scope, receive, send):
    while True:
        # 不断读取数据
        message = await receive()
        # 如果读取消息类型为 lifespan.startup，则进行初始化操作
        if message['type'] == 'lifespan.startup':
            # 在初始化完成后，向 asgi 环境发送启动完成消息
            await send({'type': 'lifespan.startup.complete'})
        # 如果读取消息类型为 lifespan.shutdown，则进行收尾工作
        elif message['type'] == 'lifespan.shutdown':
            # 在收尾工作结束后，向 asgi 环境发送收尾完成消息
            await send({'type': 'lifespan.shutdown.complete'})
            break


async def handle_home_page_request(scope, receive, send):
    # 向浏览器发送 HTTP 协议头
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/html'],
        ]
    })

    # 获取当前的事件循环
    loop = asyncio.get_running_loop()
    # 以异步 IO 的方式打开 index.html 文件，并配置打开模式
    # 为读取二进制
    f = await loop.run_in_executor(
        None, open,
        os.path.join(SERVER_ROOT, "index.html"), "rb"
    )
    # 以异步 IO 的方式读取文件
    data = await loop.run_in_executor(None, f.read)
    # 以异步 IO 的方式关闭文件
    await loop.run_in_executor(None, f.close)

    # 向浏览器发送文件内容
    await send({
        'type': 'http.response.body',
        'body': data,
        'more_body': False
    })


async def handle_ws_conn(scope, receive, send):
    while True:
        msg = await receive()
        msg_type = msg['type']

        if msg_type == 'websocket.receive':
            # 当接收到浏览器端的 Ping 消息，回应 Pong
            if msg['text'] == 'Ping':
                await send({'type': 'websocket.send', 'text': "Pong"})

        # 该消息类型表示 WebSocket 建立
        elif msg_type == 'websocket.connect':
            print("Client connected")
            # 向浏览器发送 websocket.accept 消息表示接受该连接
            await send({'type': 'websocket.accept'})

        # 该消息类型表示失去了 WebSocket 连接
        if msg_type == 'websocket.disconnect':
            print("Client disconnected")
            break


async def send_404_error(scope, receive, send):
    await send({
        'type': 'http.response.start',
        'status': 404,
        'headers': [
            [b'content-type', b'text/html'],
        ]
    })
    await send({
        'type': 'http.response.body',
        'body': b"Not found",
        'more_body': False
    })


async def app(scope, receive, send):
    # 获取请求类型
    request_type = scope['type']

    # 如果是 http 类型的请求，则由该程序段处理
    if request_type == 'http':
        # 获取请求的路径
        request_path = scope['path']
        if request_path == "/":
            await handle_home_page_request(scope, receive, send)
        else:
            # 对于其它路径的请求，均向浏览器发回 404 错误
            await send_404_error(scope, receive, send)

    # 如果是 websocket 类型的请求，则由该程序段处理
    elif request_type == 'websocket':
        await handle_ws_conn(scope, receive, send)

    # 如果是生命周期类型的请求，则由该程序段处理
    elif request_type == 'lifespan':
        await handle_lifespan(scope, receive, send)
    else:
        raise NotImplementedError()
