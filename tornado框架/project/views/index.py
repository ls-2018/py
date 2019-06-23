from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def initialize(self, **kwargs):
        self.recv = kwargs

    def get(self, *args, **kwargs):
        self.write('<h1>hello world!</h1>')
        self.write('<h1>hello world!</h1>')
        self.write('<h1>hello world!</h1>')
        self.finish()
        print(self.recv)
