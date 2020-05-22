from abc import ABC

from tornado.web import RequestHandler


class MainHandler(RequestHandler, ABC):
    def initialize(self, db):
        """
        用于实例化handler类的过程
        :return:None
        """
        self.db = db

    def prepare(self):
        """
        请求到来时，先执行的函数
        :return:None
        """
        pass

    def on_finish(self):
        """
        请求结束时，先执行的函数
        :return:
        """

    def set_default_headers(self):
        # ①
        self.set_header('name', 1234)

    def write_error(self, status_code: int, **kwargs):
        self.write(kwargs['reason'] + '123')
        if status_code == 500:
            return self.render('500.html')

    async def get(self):
        # ④
        import asyncio, time
        print('-', time.time())
        await asyncio.sleep(10)
        print('+', time.time())
        # self.write(str(time.time()))
        # self.send_error(status_code=500, reason='asdas')  # 直接在前端显示错误信息
        # self.set_status(200)  # 不管用

    # def get_template_path(self):
    #     return ''

    async def post(self):
        # post,get方式的参数一起获取。
        print(self.get_argument(name='name', default='', strip=True))  # 返回字符串
        print(self.get_arguments(name='name', strip=True))  # 返回列表

        # get方式的参数获取。
        print(self.get_query_argument(name='name', default='', strip=True))
        print(self.get_query_arguments(name='name', strip=True))
        print(self.request.arguments)  # 原始数据
        # post方式的参数获取。
        print(self.get_body_argument(name='name'))
        print(self.get_body_arguments(name='name'))
        print(self.request.body)  # 原始数据
        print(self.request.body_arguments)  # 原始数据处理后的
        self.write('hello')


class MainNameHandler(RequestHandler, ABC):

    async def get(self, name):
        self.write(name)
        self.redirect(self.reverse_url('index'), permanent=True)  # 301,永久

        # await self.finish({'name': name})  # 将缓冲区的内容发送出去
        # self.set_status(2001)
