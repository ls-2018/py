# -*- coding: utf-8 -*-
import scrapy

from scrapy.http.request import Request


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']
    i = 1

    def parse(self, response):
        # response.xpath('')  # 返回列表   Selector
        # response.xpath('').extract()
        # response.xpath('').extract_first()
        print(response)
        print(self.i)
        self.i += 1
        for i in range(10):
            yield Request(url='http://baidu.com/', callback=self.parse)
