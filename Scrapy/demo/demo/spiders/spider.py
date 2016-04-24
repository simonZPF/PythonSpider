# -*-coding:utf8 -*-
from scrapy.spiders import CrawlSpider

class Demo(CrawlSpider):
    name= "demo"
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):

        print response.body