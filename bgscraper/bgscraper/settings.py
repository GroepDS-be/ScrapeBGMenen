# -*- coding: utf-8 -*-

# Scrapy settings for bgscraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'bgscraper'

SPIDER_MODULES = ['bgscraper.spiders']
NEWSPIDER_MODULE = 'bgscraper.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Linux; U; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13'

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_DEBUG = True

ITEM_PIPELINES = {
    'bgscraper.pipelines.BgscraperPipeline': 300,
}
