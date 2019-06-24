"""
@Time: 2019/6/24 23:40 
@Author: liushuo
@File: reques.py 
@Desc: 
@Software: PyCharm
"""
"""
1、利用http协议向服务器传递参数
    提取url的特定部分
    (r'/liu/(\w+)/(\w+)/')              def get(self,h1,h2,*args,**kwargs)
    (r'/liu/(?P<P2>\w+)/(?P<P1>\w+)/')              def get(self,P1,P2,*args,**kwargs)
    get方式传递参数
    post方式传递参数
    既可以获取get请求，也可以获取post请求
    在http报文的头中增加自定义的字段
2、request对象

"""