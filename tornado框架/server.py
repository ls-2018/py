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
    # app.listen(8000)  ---->  返回了一个服务器
    # 手动创建一个服务器
    import tornado.httpserver

    server = tornado.httpserver.HTTPServer(app)
    # server.listen(8088, '127.0.0.1')# 默认单进程

    server.bind(8008)
    server.start(1)  # 启动4个进程，默认1

    # tornado.ioloop.IOLoop.current().start()
    """
    IOLoop.current()    返回当前线程的IOLoop实例
    """
