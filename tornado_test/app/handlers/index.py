import tornado.web


# 当处理请求时会进行实例化并调用HTTP请求对应的方法
class IndexHandler(tornado.web.RequestHandler):
    # 定义get方法对HTTP的GET请求做出响应
    def get(self):
        # 从querystring查询字符串中获取id参数的值，若无则默认为0.
        id = self.get_argument("id", 0)
        # write方法将字符串写入HTTP响应
        self.write("hello world id = " + str(id))
