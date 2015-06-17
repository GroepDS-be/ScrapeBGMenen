# -*- coding: utf-8 -*-
#
# This file is part of https://github.com/AvidSoftware-be/ScrapeBGMenen, licensed under GNU Affero GPLv3 or later.
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
