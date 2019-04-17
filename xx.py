# by luffycity.com
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals


def func():
    pass


dispatcher.connect(func, signals.spider_closed)

# class MyExtend(object):
#     def __init__(self):
#         pass
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         self = cls()
#         crawler.signals.connect(self.x1, signal=signals.spider_opened)
#         crawler.signals.connect(self.x2, signal=signals.spider_closed)
#         return self
#
#     def x1(self, spider):
#         print('open')
#


#     def x2(self, spider):
#         print('close')

