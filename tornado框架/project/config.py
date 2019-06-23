import os

BASE_DIR = os.path.dirname(__file__)
# 启动参数
options = {
    'port': 8001
}

# 系统配置
settings = {
    "debug": True,
    'static_path': os.path.join(BASE_DIR, 'static'),
    'static_url_prefix': '/static',
    'template_path': os.path.join(BASE_DIR, 'templates')
}

"""
debug=True
    1、自动重启                        autoreload=True
    2、取消缓存编译的模板              compiled_template_cache=False
    3、取消缓存静态文件的hash值        static_hash_cache=False
    4、提供追踪信息                    serve_traceback=True
"""
