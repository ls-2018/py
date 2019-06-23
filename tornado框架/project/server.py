import tornado.ioloop
from config import options
from urls import Application


if __name__ == '__main__':
    app = Application()
    app.listen(options['port'])
    tornado.ioloop.IOLoop.current().start()
