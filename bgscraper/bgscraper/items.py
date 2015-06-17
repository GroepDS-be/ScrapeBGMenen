# -*- coding: utf-8 -*-

#
# This file is part of https://github.com/AvidSoftware-be/ScrapeBGMenen, licensed under GNU Affero GPLv3 or later.
#

import scrapy


class BgscraperItem(scrapy.Item):

    naam = scrapy.Field()
    adres = scrapy.Field()
    postcode = scrapy.Field()
    gemeente = scrapy.Field()

