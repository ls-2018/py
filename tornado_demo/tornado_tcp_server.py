"""
第6章/tornado_tcp_server/tornado_tcp_server.py
"""

import asyncio, time

from tornado.iostream import StreamClosedError
from tornado.tcpserver import TCPServer
from tornado.ioloop import IOLoop


class EchoServer(TCPServer):
    async def handle_stream(self, stream, address):
        for i in range(6):
            try:
                # 向连接终端发送数据
                await stream.write(
                    f"[{time.strftime('%X')}] Count {i}\n".encode("utf-8")
                )
                # 等待1秒
                await asyncio.sleep(1)
            except StreamClosedError:
                break


server = EchoServer()
server.listen(8888)
try:
    IOLoop.current().start()
except KeyboardInterrupt as e:
    print("Exit")

# telnet  127.0.0.1 8888
