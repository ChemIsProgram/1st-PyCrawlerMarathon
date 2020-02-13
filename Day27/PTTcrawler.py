# -*- coding: utf-8 -*-
import scrapy


class PttcrawlerSpider(scrapy.Spider):
    name = 'PTTcrawler'
    allowed_domains = ['https://www.ptt.cc/bbs/Gossiping/M.1581574000.A.23A.html']
    start_urls = ['http://https://www.ptt.cc/bbs/Gossiping/M.1581574000.A.23A.html/']

    def parse(self, response):
        pass
