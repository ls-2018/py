import tornado.web
from views import index
from config import settings


class Application(tornado.web.Application):
    def __init__(self, *args, **kwargs):
        handlers = [
            ('/', index.IndexHandler)

        ]
        super(Application, self).__init__(handlers, *args, **kwargs, **settings)
