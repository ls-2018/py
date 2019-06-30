"""
@Time: 2019/6/30 10:35 
@Author: liushuo
@File: web.py 
@Desc: 
@Software: PyCharm
"""
from tornado.httpclient import AsyncHTTPClient
from tornado.gen import coroutine


# 异步web请求客户端，用来进行异步web请求
def callback(response):
    print(type(response))


@coroutine
def x():
    client = AsyncHTTPClient()
    response = client.fetch('www.baidu.com')
    return response


# print(x())  # <Future finished result=<Future pending>>
# 用于执行一个web请求，并一步响应返回一个tornado.httpclient.HttpResponse对象
"""
request:   url或一个tornado.httpclient.HttpRequest对象
"""
from tornado.httpclient import HTTPRequest

from tornado.httpclient import HTTPResponse

import tornado.gen
tornado.gen.coroutine
tornado.gen.Return