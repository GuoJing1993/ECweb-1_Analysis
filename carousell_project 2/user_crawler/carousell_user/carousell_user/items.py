# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CarousellUserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    user_id=scrapy.Field()
    user_sold=scrapy.Field()
    user_revenue=scrapy.Field()
    user_unsold=scrapy.Field()
    user_greview=scrapy.Field()
    user_breview=scrapy.Field()    
    pass
    
#class CarousellUserItem_2(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
#    user_greview=scrapy.Field()
#    user_breview=scrapy.Field()
#    pass
    
