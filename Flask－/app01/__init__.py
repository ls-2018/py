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
    static_url_path         静态文件访问路径    更改为/static            默认'/' + 'static_folder' 
  
    url_prefix='/user'      蓝图的前置URL
    
    static_host =   CDN的时候用
    # 下边不用
    host_matching = False,  # 如果不是特别需要的话,慎用,否则所有的route 都需要host=""的参数
    subdomain_matching = False,  # 理论上来说是用来限制SERVER_NAME子域名的,但是目前还没有感觉出来区别在哪里
    instance_path = None,  # 指向另一个Flask实例的路径
    instance_relative_config = False  # 是否加载另一个实例的配置
    root_path = None  # 主模块所在的目录的绝对路径,默认项目目录
    
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
        DEBUG = False
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
        # None \ 非None   决定是否往后执行
        return None

    @app.after_request  # after会全部执行，与django中间件不同
    def be1(response):
        return response

    @app.errorhandler(404)
    def han(response):
        print(response)
        """404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."""
        return '404'

    return app
#