import os
from tornado.web import url
from app.handlers import index

handlers = [

    ('/', index.IndexHandler),
    # url('/html', HtmlHandler),
    # url('/data/?', DBHandler),
    # url(r'/(?P<name>\w+)/?', MainNameHandler),
    # (r"/(.*?)/(.*?)/(.*)", RedirectHandler, {"url": "/{1}/{0}/{2}", 'permanent': True}),

    # (r"/api/register", Passport.RegisterHandler),
    # (r"/api/login", Passport.LoginHandler),
    # (r"/api/logout", Passport.LogoutHandler),
]
