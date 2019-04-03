# -*- coding: utf-8 -*-
import scrapy

from scrapy.http.request import f
class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        # response.xpath('')  # 返回列表   Selector
        # response.xpath('').extract()
        # response.xpath('').extract_first()
        print(response)
