from tornado.web import url

from apps.operates.handlers import MessageHandler

urlpattern = [
    url("/messages/", MessageHandler)
]
