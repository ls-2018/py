from flask import Flask
from .views.user import user


def create_app():
    app = Flask(__name__)

    app.register_blueprint(user)
    # #################         Flask 实例化配置   ###########################
    """
    # 5-Flask 实例化配置
    # app = Flask(__name__)
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

    class MySet(object):
        DEBUG = True
        SECRET_KEY = 'session前端加密需要'

    app.config.from_object(MySet)
    # #################         Flask 特殊装饰器   ###########################
    """    
    
    @app.before_request # 在请求进入视图函数之前
    @app.after_request  # 在视图函数结束之后
    @app.errorhandler(404)   
    """

    @app.before_request
    def be1():
        # True \ False   决定是否往后执行
        return 1

    return app
