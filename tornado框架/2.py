"""
@Time: 2019/6/30 12:05 
@Author: liushuo
@File: 2.py 
@Desc:    tornado  5.x
@Software: PyCharm
"""
import tornado.web
from tornado.web import RequestHandler
from tornado.gen import coroutine
import tornado.ioloop


def x():
    import time

    time.sleep(12)
    return '123'


class Indexhandler(RequestHandler):
    @coroutine
    def get(self):
        num = x()
        self.write(num)


class homehandler(RequestHandler):

    def get(self):
        self.write('===========')


if __name__ == '__main__':
    app = tornado.web.Application([
        ('/', Indexhandler),
        ('/home', homehandler)
    ])
    app.listen(8001)

    tornado.ioloop.IOLoop.current().start()
