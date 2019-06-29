import tornado.web
from views import index
from config import settings
from tornado.web import StaticFileHandler
import os


class Application(tornado.web.Application):
    def __init__(self, *args, **kwargs):
        handlers = [
            ('/', index.IndexHandler, {'name': 'zhangsan'}),
            tornado.web.url('/kind', index.KindHandler, kwargs={'arg': "demo"}, name='kind'),
            ('/(.*)$', StaticFileHandler,
             {'path': os.path.join(settings.BASE_DIR, 'static'), 'default_filename': "index.html"})

        ]
        super(Application, self).__init__(handlers, *args, **kwargs, **settings)
