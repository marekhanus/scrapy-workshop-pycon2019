# -*- coding: utf-8 -*-
import scrapy


class QuotationSpider(scrapy.Spider):
    name = 'quotation'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):
            yield {
                # 'text': None,  # just for testing quotation pipeline
                'text': quote.xpath('./span[@class="text"]/text()').extract_first(),
                'author': quote.xpath('.//small[@class="author"]/text()').extract_first(),
                'tags': quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract(),
            }

        next_url_link = response.xpath('//nav//li[@class="next"]/a/@href').extract_first()
        if next_url_link is not None:
            yield scrapy.Request(response.urljoin(next_url_link))
