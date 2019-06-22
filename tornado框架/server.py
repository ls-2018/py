import tornado.web
# 基础web框架模块
import tornado.ioloop
# 核心IO循环模块，封装了Linux的epoll和BSD的kqueue

# 类比django中的视图类
class IndexHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.write('<h1>hello world!</h1>')


if __name__ == '__main__':
    app = tornado.web.Application([
        ('/', IndexHandler)
    ])
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
