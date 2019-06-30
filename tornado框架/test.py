"""
@Time: 2019/6/30 16:49 
@Author: liushuo
@File: test.py 
@Desc: 
@Software: PyCharm
"""
import tornado.web
import tornado.gen
from tornado.httpclient import AsyncHTTPClient,HTTPClient
import tornado.ioloop
import time
from tornado.concurrent import Future

http = HTTPClient()
res = http.fetch("http://www.baidu.com/")
print(res.body)
