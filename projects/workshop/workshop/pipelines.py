# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class QuotationPipeline(object):
    def process_item(self, item, spider):
        if item['text'] is None:
            raise Exception('Some None text field in a item dictionary')

        return item
