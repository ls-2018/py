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
    server.start(2)  # 启动4个进程，默认1
    """
    以后不用以上这种方式启动多进程：
    存在问题：
        1、每个子进程都回从父进程中复制一份IOLoop的实例,如果在创建子进程前修改了IOLoop,会影响所有的子进程。
        2、所有的进程都是由一个命令启动的，无法做到在不停止服务的情况下修改代码。
        3、所有进程共享一个端口，想要分别监控很困难
    """

    tornado.ioloop.IOLoop.current().start()
    """
    IOLoop.current()    返回当前线程的IOLoop实例
    """
