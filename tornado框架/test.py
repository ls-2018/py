"""
@Time: 2019/6/30 16:49 
@Author: liushuo
@File: test.py 
@Desc: 
@Software: PyCharm
"""
import tornado.ioloop
import tornado.web
from tornado import gen
from tornado.concurrent import Future




class AsyncHandler(tornado.web.RequestHandler):

    @gen.coroutine
    def get(self):
        future = Future()
        # future.add_done_callback(self.doing)
        # yield future
        # 或
        tornado.ioloop.IOLoop.current().add_future(future,self.doing)
        yield future

    def doing(self, *args, **kwargs):
        self.write('async')
        import time
        time.sleep(5)
        self.finish()


class StopHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('---------------')

application = tornado.web.Application([

    (r"/async", AsyncHandler),
    (r"/", StopHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

# 远端url控制某个url的future
