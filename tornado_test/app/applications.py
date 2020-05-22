import tornado.web
import tornado.ioloop
from tornado.options import define, options
from app.script.timed_program import tail_data
from app.handlers import handlers
from app.conf.settings import app_settings
import wtforms_json
import redis
import peewee_async
from peewee import MySQLDatabase

define('port', type=int, default=8000, help='run server as the given port')


class Application(tornado.web.Application):
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)
        # self.db = MySQLDatabase(**app_settings['databases']['write'])

        # self.database = peewee_async.MySQLDatabase(**app_settings['databases']['write'])
        # self.redis = redis.StrictRedis(
        #     connection_pool=redis.ConnectionPool(**conf.redis_conf),
        #     decode_responses=True
        # )
        # self.redis = redis.StrictRedis(
        #     **app_settings['redis'],
        #     decode_responses=True
        # )
        my_program_callback = tornado.ioloop.PeriodicCallback(tail_data, 5000)  # 5S
        my_program_callback.start()

    def start_server(self):
        for k, v in app_settings['log_conf'].items():
            options.__setattr__(k, v)
        options.parse_command_line()

        wtforms_json.init()
        app = Application(
            handlers, **app_settings['program']
        )
        app.listen(port=8000)
        print('the serve is running at http://%s:8000' % app_settings['program']['run_host'])
        tornado.ioloop.IOLoop.current().start()
