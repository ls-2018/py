from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def initialize(self, **kwargs):
        self.recv = kwargs

    def set_default_headers(self):
        """
        在进入http响应处理方法之前进行调用，统一进行设置header,
        会被get方法，重置
        :return:
        """
        self.set_header('k', 'v')

    def get(self, *args, **kwargs):
        print(self.get_query_argument('flag'))
        self.write('<h1>hello world!</h1>')
        self.write('<h1>hello world!</h1>')
        self.write('<h1>hello world!</h1>')
        self.finish()
        self.set_header('k', 'v')
        print(self.recv)

        self.send_error(status_code=500, **kwargs)  # 抛出异常，以后的不再执行

    def write_error(self, status_code, **kwargs):
        code = None
        if status_code == 500:
            code = 500
            self.write('服务器内部错误')
        elif status_code == 404:
            code = 404
            self.write('资源部存在')
        self.set_status(code, '')
