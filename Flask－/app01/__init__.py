from flask import Flask
from .views.user import user


def create_app():
    app = Flask(__name__)

    app.register_blueprint(user)
    # #################         Flask 实例化配置   ###########################
    # 5-Flask 实例化配置

    # app = Flask(__name__)
    """
    template_folder='', static_folder='', static_url_path='/{static_folder}'
    template_folder         模板存放目录    默认 templates
    static_folder           静态文件存放目录    默认 static
    static_url_path         静态文件访问路径    默认'/' + 'static_folder' 
    url_prefix='/user'      蓝图的前置URL
    """

    # #################         Flask 对象配置   ###########################
    """
    # 6-Flask 对象配置
    app.config['SECRET_KEY']= 'session前端加密需要'
    app.config['DEBUG']= True
    app.default_config
    app.secret_key = 'session前端加密需要'
    """

    # class MySet(object):
    #     DEBUG = False
    #     SECRET_KEY = 'session前端加密需要'

    # app.config.from_object(MySet)
    return app
