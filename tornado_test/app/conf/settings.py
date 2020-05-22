import os
import uuid
import base64

# 获取项目的绝对路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 静态文件
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
STATIC_PATH = os.path.join(BASE_DIR, 'static')
if not os.path.exists(os.path.join(BASE_DIR, 'logs')):
    os.makedirs(os.path.join(BASE_DIR, 'logs'))
app_settings = dict(
    program=dict(
        debug=True,
        xsrf_cookies=base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes),
        cookie_secret=base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes),
        expire_seconds=36000,
        app_name='codo_cmdb',
        static_path=STATIC_PATH,  # /static/test.jpg
        static_url_prefix='/static/',
        template_path=TEMPLATE_PATH,
        # 'xsrf_cookies': True,
        run_host='127.0.0.1',
    ),
    databases={
        'write': {
            "host": '127.0.0.1',
            "user": 'root',
            "password": '1234',
            "dbname": 'tornado',
            "port": 3306,
            'charset': 'utf8mb4'
        },
        'read': {
            "host": '127.0.0.1',
            "user": 'root',
            "password": '1234',
            "database": 'tornado',
            "port": 3306,
            'charset': 'utf8mb4'
        }
    },
    redis={
        'host': '193.112.27.150',
        'port': 6379,
        'password': 'ls-root123'
    },
    log_conf={
        'log_file_prefix': os.path.join(BASE_DIR, 'logs', 'log'),
        'log_file_max_size': 5 * 1024 * 1024,  # 5M
        'log_file_num_backups': 10,
        'logging': 'warning'
    }
)
