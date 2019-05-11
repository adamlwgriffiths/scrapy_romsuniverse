# -*- coding: utf-8 -*-
import scrapy

class RomsUniverseRom(scrapy.Item):
    url = scrapy.Field()
    id = scrapy.Field()
    name = scrapy.Field()
    platform = scrapy.Field()
    downloads = scrapy.Field()
    filenames = scrapy.Field()
