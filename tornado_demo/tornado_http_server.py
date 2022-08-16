"""
第6章/tornado_routes/routes.py
"""
import os
import tornado.wsgi
from tornado.web import Application
import tornado.ioloop
from tornado.web import StaticFileHandler
import tornado.ioloop
from tornado.routing import Rule, RuleRouter, PathMatches
from web2py import wsgihandler
import tornado.locale

SERVER_ROOT = os.path.dirname(__file__)


# HomePage 是一个继承自 tornado.web.RequestHandler 的类
class HomePage(tornado.web.RequestHandler):
    async def get(self):
        # 根据浏览器语言自动翻译
        self.locale = tornado.locale.get(
            self.get_query_argument("lang", "zh_CN")
        )
        words = self.locale.translate("Hello")
        # 渲染模板，并向其传入参数 greeting_word
        await self.render("index.html", greeting_word=words)


class Users(tornado.web.RequestHandler):
    async def get(self):
        await self.render("server2_index.html", users=['李明', '张亮'])


class AppPage(tornado.web.RequestHandler):

    def get(self, path_arg1):
        """
        该函数必须可以接受两个参数
        :param path_arg1: 对应正则表达式截取的第1个变量
        :return:
        """
        self.write(f"Arg1 is: {path_arg1}")


app1 = Application([
    # 该路径设置了一个个截取的的变量
    (r"/app1/handler", AppPage),
])

# 创建一个WSGI容器用于支持WSGI应用
wsgi_container = tornado.wsgi.WSGIContainer(
    wsgihandler.application
)

if __name__ == '__main__':
    # 从指定的目录中加载语言表
    tornado.locale.load_translations(os.path.join(SERVER_ROOT, "languages"))
    # 创建Web服务器应用
    app = tornado.web.Application(

        [
            (
                r"/static/(.*)",
                StaticFileHandler,
                # 配置当前文件同目录下的 static 目录为静态文件所在目录
                dict(path=os.path.join(SERVER_ROOT, "static"))
            ),
            ("/", HomePage),  # 将HomePage映射到 / 路径上
            Rule(PathMatches(r"/app1.*"), app1),  # http://127.0.0.1:8888/app1/handler
            # (
            #     r"/welcome.*",
            #     # 使用 FallbackHandler 可将指定的请求交由 wsgi 应用处理
            #     tornado.web.FallbackHandler,
            #     dict(fallback=wsgi_container)
            # )
        ],
        template_path=os.path.join(SERVER_ROOT, "template"),
        debug=True
    )
    app.listen(8888)  # 侦听端口 8888
    tornado.ioloop.IOLoop.current().start()  # 启动
