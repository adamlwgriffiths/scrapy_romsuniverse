# -*- coding: utf-8 -*-
import re
import logging
import scrapy
from romsuniverse.items import RomsUniverseRom

class RomsUniverseSpider(scrapy.Spider):
    name = 'romsuniverse'
    allowed_domains = ['romsuniverse.com']

    def start_requests(self):
        platforms = getattr(self, 'platforms', None)
        if platforms:
            # platform links are in the format: /roms/<platform>
            for platform in platforms.split(','):
                yield scrapy.Request(f'http://www.romsuniverse.com/roms/{platform}', self.parse_platform)
        else:
            # dynamically find platforms
            yield scrapy.Request('http://www.romsuniverse.com/listall.php', self.parse_systems)

    def parse_systems(self, response):
        for system in set(response.xpath('//div[@class="container"]//a[contains(@href,"/roms/")]/@href').getall()):
            yield scrapy.Request(system, self.parse_platform)

    def parse_platform(self, response):
        # get platform from the breadcrumb link
        platform = response.xpath('//ol[@class="breadcrumb"]/li[2]/a/@href').re_first(r'/roms/([^/]+)')

        # rom links are in the format: /download/<platform>/<rom><id>
        for href in response.xpath(f'//a[contains(@href,"download/{platform}")]/@href').getall():
            yield scrapy.Request(response.urljoin(href), self.parse_rom)

        next_page = response.xpath('//a[text()=" > "]/@href').get()
        if next_page:
            yield scrapy.Request(next_page, self.parse_platform)

    def parse_rom(self, response):
        # most consistent way to get id is from url
        # some games (mame especially) have sets of downloads, so create a list of roms
        try:
            item = RomsUniverseRom()
            item['url'] = response.url
            item['id'] = re.search(r'(\d+)$', response.url).group(1)
            item['name'] = response.xpath('//div[contains(@class, "widget-item")]/h1/text()').get().strip()
            item['platform'] = re.search(r'/download/([^/]+)/', response.url).group(1)
            item['downloads'] = response.xpath('//a[contains(@href, "downloadrom")]/@href').getall()
            item['filenames'] = response.xpath('//a[contains(@href, "downloadrom")]/@href').re(r'filename=([^&]+)')
            return item
        except Exception as e:
            logging.warning(f'Failed to process {response.url}')
