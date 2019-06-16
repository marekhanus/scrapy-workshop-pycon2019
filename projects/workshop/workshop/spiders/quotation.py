# -*- coding: utf-8 -*-
import scrapy


class QuotationSpider(scrapy.Spider):
    name = 'quotation'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        pass
