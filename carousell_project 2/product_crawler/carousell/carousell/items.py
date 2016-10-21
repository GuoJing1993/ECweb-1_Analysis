# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CarousellItem(scrapy.Item):
    item_category = scrapy.Field()
    item_id = scrapy.Field()
    item_title = scrapy.Field()
    item_keywords = scrapy.Field()
    item_description = scrapy.Field()
    item_label = scrapy.Field()
    item_sellerName = scrapy.Field()
    item_sellerurl = scrapy.Field()
    item_price = scrapy.Field()
    item_location = scrapy.Field()
    item_face_able = scrapy.Field()
    item_truck_able = scrapy.Field()
    item_likes = scrapy.Field()
    post_time = scrapy.Field()
    def __repr__(self):
        """only print out attr1 after exiting the Pipeline"""
        return repr({"item_id": self['item_id']})
    pass