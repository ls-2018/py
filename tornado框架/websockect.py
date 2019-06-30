"""
@Time: 2019/6/30 17:16 
@Author: liushuo
@File: websockect.py 
@Desc: 
@Software: PyCharm
"""
from tornado.websocket import WebSocketHandler
import tornado.web
import tornado.gen
from tornado.httpclient import AsyncHTTPClient, HTTPClient
import tornado.ioloop
import time
from tornado.concurrent import Future

users = []


class EchoWebSocket(WebSocketHandler):
    def open(self, *args, **kwargs):
        # 当一个链接建立后调用
        print('open')
        print(self.request.remote_ip)
        users.append(self)

    def on_message(self, message):
        # 服务端收到消息调用
        print(message)
        users[0].write_message('ok')

    def on_close(self):
        # 关闭后调用
        print('on_close')
        users.reverse(self)

    def check_origin(self, origin):
        #     判断源origin,跨域要重写
        return True

    def on_pong(self, data):
        print(data, 'pong')

    def close(self, code=None, reason=None):
        # 主动关闭
        pass


class ChatHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        with open('wc.html', 'r',encoding='utf8') as f:
            self.write(f.read())


if __name__ == '__main__':
    app = tornado.web.Application([
        ('/socket', EchoWebSocket),
        (r'/', ChatHandler),
    ], websocket_ping_interval=10)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
