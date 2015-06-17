# -*- coding: utf-8 -*-
import scrapy
from bgscraper.items import BgscraperItem


class BgmSpider(scrapy.Spider):
    name = "bgm"
    allowed_domains = ["menen.be"]
    start_urls = [
        'http://www.menen.be/bedrijvengids?latitude=50.8013179&longitude=3.1185616&waar=Wahisstraat&nummer=&afstand=10000&form=proximity&order=title',
    ]

    for page in range(1, 146, 1):
        start_urls.append(
            'http://www.menen.be/bedrijvengids?page=%s&latitude=50.8013179&longitude=3.1185616&waar=Wahisstraat&nummer=&afstand=10000&form=proximity&order=title' % page)

    def parse(self, response):
        for sel in response.xpath('//*[@id="company-search-results"]/li[*]'):
            it = BgscraperItem()

            it['naam'] = sel.xpath('./div/div/h3/a/text()').extract()[0].strip()
            it['adres'] = sel.xpath('./div/div/p/text()[1]').extract()[0].strip()
            it['postcode'],it['gemeente'] = sel.xpath('./div/div/p/text()[2]').extract()[0].strip().split()
            #print '"%s","%s","%s","%s"'%(naam,adres,postcode,gemeente)

            yield it