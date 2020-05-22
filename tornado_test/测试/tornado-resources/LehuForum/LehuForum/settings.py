import os

import peewee_async

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

settings = {
    "SITE_URL": 'http://127.0.0.1:9001',
    "static_path": os.path.join(BASE_DIR, 'statics'),
    "MEDIA_ROOT": os.path.join(BASE_DIR, "media"),
    "static_url_prefix": "/static/",
    "template_path": "templates",
    "secret_key": "ZGGA#Mp4yL4w5CDu",
    "jwt_expire": 7 * 24 * 3600,
    "db": {
        "host": "127.0.0.1",
        "user": "root",
        "password": "12345678",
        "name": "tornado",
        "port": 3306
    },
    "redis": {
        "host": "193.112.27.150",
        "port": 6379,
        "password": "ls-root123"
    }
}

database = peewee_async.MySQLDatabase(
    settings['db']['name'], host=settings['db']['host'], port=settings['db']['port'], user=settings['db']['user'],
    password=settings['db']['password']
)
