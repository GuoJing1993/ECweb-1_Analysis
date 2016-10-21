# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


#class CarousellPipeline(object):
#    def process_item(self, item, spider):
#        return item
        
from scrapy.exceptions import DropItem

class CarousellPipeline(object):
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['item_id'] in self.ids_seen:
            raise DropItem("Duplicate item found")
        else:
            self.ids_seen.add(item['item_id'])
            return item
