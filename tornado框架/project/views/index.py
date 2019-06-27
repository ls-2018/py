from tornado.web import RequestHandler
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


class KindHandler(RequestHandler):
    def initialize(self, arg):
        print(arg)

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
