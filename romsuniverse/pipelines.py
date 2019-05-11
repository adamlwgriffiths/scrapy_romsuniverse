# -*- coding: utf-8 -*-
import os
import json
from romsuniverse.items import RomsUniverseRom
from scrapy.exceptions import DropItem

class JsonWriterPipeline(object):
    @classmethod
    def from_crawler(cls, crawler):
        return cls(path=crawler.settings.get('JSON_OUTPUT_PATH'))

    def __init__(self, path):
        self.path = path

    def process_item(self, item, spider):
        if isinstance(item, RomsUniverseRom):
            item_fname = item['url'].split('/')[-1]

            if not item['filenames'] or len(item['filenames']) is not len(item['downloads']):
                # bad item
                fname = os.path.join(self.path, f'__bad_items/{item_fname}.json')
                dname = os.path.dirname(fname)
            else:
                fname = os.path.join(self.path, f'{item["platform"]}/{item_fname}.json')
                dname = os.path.dirname(fname)

            if not os.path.isdir(dname):
                os.makedirs(dname)

            if os.path.exists(fname):
                raise DropItem('{item["platform"]}/{item_fname}')

            with open(fname, 'w') as f:
                f.write(json.dumps(dict(item), indent=4, sort_keys=True))
        return item
