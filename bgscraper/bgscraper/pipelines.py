# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


class BgscraperPipeline(object):

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        item['naam'] = item['naam'].replace(',','')
        item['adres'] = item['adres'].replace(',','')
        item['postcode'] = item['postcode'].replace(',','')
        item['gemeente'] = item['gemeente'].replace(',','')

        #dubbels eruit halen
        if item['naam'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['naam'])
            return item
