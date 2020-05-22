from abc import ABC
import tornado.web
import tornado.ioloop
from tornado.options import define, options
from views import *

define('port', default=9000, help='run as the given port', type=int)
define('debug', default=True, help='', type=bool)
# options.parse_command_line()
options.parse_config_file('conf.cfg')

settings = {
    'static_path': 'static',  # /static/test.jpg
    'static_url_prefix': '/static/',
    'template_path': 'templates'
}

if __name__ == '__main__':
    app = tornado.web.Application([
        tornado.web.url('/', MainHandler, name='index', kwargs={'db': 'test'}),
        tornado.web.URLSpec(r'/(?P<name>\w+)/?', MainNameHandler),
        (r"/(.*?)/(.*?)/(.*)", tornado.web.RedirectHandler, {"url": "/{1}/{0}/{2}", 'permanent': True}),
        (r"/static/(.*?)", tornado.web.StaticFileHandler, {"path": settings['static_path']}),

    ], debug=options.debug, **settings)
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
