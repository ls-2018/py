from tornado.web import RequestHandler, authenticated
from tornado import gen

gen.coroutine


class IndexHandler(RequestHandler):
    def initialize(self, name):
        print(name)
        self.name = name

    def set_default_headers(self):
        """
        在进入http响应处理方法之前进行调用，统一进行设置header,
        会被get方法，重置
        :return:
        """
        self.set_header('k', 'v')

    async def get(self, *args, **kwargs):
        # print(self.get_query_argument('flag')) # 没有报错
        # self.write('<h1>hello world!</h1>')
        # self.write('<h1>hello world!</h1>')
        # self.write('<h1>hello world!</h1>')
        # self.finish()
        # self.set_header('k', 'v')

        # self.send_error(status_code=500, **kwargs)  # 抛出异常，以后的不再执行
        from tornado.httpclient import AsyncHTTPClient
        http_client = AsyncHTTPClient()
        response = await http_client.fetch('/kind')
        return response.body

    def write_error(self, status_code, **kwargs):
        """ 遇到异常，以后的执行"""
        code = None
        if status_code == 500:
            code = 500
            self.write('服务器内部错误')
        elif status_code == 404:
            code = 404
            self.write('资源部存在')
        self.set_status(code, '')

    def prepare(self):
        """类似中间件"""
        pass

    def on_finish(self):
        """
        请求结束后执行，   资源释放，日志处理
        :return:
        """
        pass

    """
    正常情况下
    set_default_headers
    initialize
    prepare
    HTTP方法
    on_finish
    """

    """
    在http方法内抛异常
    set_default_headers
    initialize
    prepare
    HTTP方法
    set_default_headers
    write_error
    on_finish
    """


class KindHandler(RequestHandler):
    def initialize(self, arg):
        print(arg)
        # self.clear_all_cookies(path="/", domain=None)
        # self.clear_cookie(name='', path="/", domain='baidu.com')
        # self.clear_header('name')
        self.set_secure_cookie('name', 'value', expires_days=30, version=None, )
        self.get_secure_cookie('name', value=None, max_age_days=31, min_version=None, )
        """
        max_age_days 最大过滤时间（不获取）
        min_version
        """
        # self.get_secure_cookie_key_version()
        """
        self.set_cookie(
            name,
            self.create_signed_value(name, value, version=version),
            expires_days=expires_days,
            **kwargs
        )
        """
        # self.set_cookie('name', 'value', domain=None, expires=None, path="/", expires_days=None, )

    def get(self, *args, **kwargs):
        print(self.reverse_url('kind'))
        print(self.request.method)
        print(self.request.url)
        print(self.request.path)
        print(self.request.host)
        print(self.request.remote_ip)
        print(self.request.query)
        print(self.request.version)
        print(self.request.headers)
        print(self.request.body)
        print(self.request.files)
        self.redirect('/?flag=1')


# def test():
#     import tornado.httputil
#     # tornado.httputil.HTTPFile()
#     """
#     {
#         xxxx:{
#             filename
#             body
#             content_type
#         }
#     }
#     """

class HomeHandler(RequestHandler):
    def get_current_user(self):
        # return True   # 登陆成功
        return False  # 验证失败，跳转配置中的login_url

    @authenticated
    def get(self):
        pass
