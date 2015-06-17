# -*- coding: utf-8 -*-

#
# This file is part of https://github.com/AvidSoftware-be/ScrapeBGMenen, licensed under GNU Affero GPLv3 or later.
#
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
