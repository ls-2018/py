"""
@Time: 2019/6/30 15:18 
@Author: liushuo
@File: 3.py 
@Desc: tornado  5.x
@Software: PyCharm
"""
import tornado.web
import tornado.gen
from tornado.httpclient import AsyncHTTPClient, HTTPClient
import tornado.ioloop
import time
from tornado.concurrent import Future


class Index(tornado.web.RequestHandler):
    def _on_download(self, response):
        print(response)
        # time.sleep(10)
        self.write(response.body)
        self.finish()

    @tornado.gen.coroutine
    # @tornado.web.asynchronous  # 取消自动关闭通道
    def get(self, *args, **kwargs):
        print(time.time(), '1')
        # http = AsyncHTTPClient()
        # 方式一   不是异步
        # data = yield http.fetch("http://www.baidu.com/", self._on_download)
        # 方式二   不是异步
        # data = yield http.fetch("http://www.baidu.com/")
        # print('K.O.', data)

        future = Future()
        # tornado.ioloop.IOLoop.current().add_timeout(time.time() + 1, self.doing)# 异步的
        # 或者
        # future.add_done_callback(self.doing)# 异步的
        yield future

        # content = yield self.doing2()        # 不是异步的
        # self.write(content)
        # print(time.time(), '1')

    def doing(self, *args, **kwargs):
        self.write('async')
        time.sleep(10)
        self.finish()  # 手动关闭
        print(time.time(), '1')

    def doing2(self):
        future = Future()
        time.sleep(10)
        future.set_result('--------123')
        return future


class Index2(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        print(time.time(), '2')
        time.sleep(1)
        self.write('1111111111111111----')
        print(time.time(), '2')


if __name__ == '__main__':
    app = tornado.web.Application([
        ('/', Index),
        ('/2', Index2)
    ])
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
