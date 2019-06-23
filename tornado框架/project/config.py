import os

BASE_DIR = os.path.dirname(__file__)
# 启动参数
options = {
    'port': 8000
}

# 系统配置
settings = {
    "debug": True,
    'static_path': os.path.join(BASE_DIR, 'static'),
    'static_url_prefix': None,
    'template_path': os.path.join(BASE_DIR, 'templates')
}
