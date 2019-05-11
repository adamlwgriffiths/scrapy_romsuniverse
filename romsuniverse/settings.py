# -*- coding: utf-8 -*-
import os

BOT_NAME = 'romsuniverse'

SPIDER_MODULES = ['romsuniverse.spiders']
NEWSPIDER_MODULE = 'romsuniverse.spiders'

LOG_LEVEL = 'INFO'

ROBOTSTXT_OBEY = True

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'romsuniverse.middlewares.RomsUniverseSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'romsuniverse.middlewares.RomsUniverseDownloaderMiddleware': 543,
#}

ITEM_PIPELINES = {
    'romsuniverse.pipelines.JsonWriterPipeline': 300,
}

JSON_OUTPUT_PATH = os.path.join(os.path.dirname(__file__), 'data')
