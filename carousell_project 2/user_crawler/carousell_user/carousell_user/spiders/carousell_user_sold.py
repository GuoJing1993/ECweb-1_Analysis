# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re
import json
from carousell_user.items import CarousellUserItem


user_data=CarousellUserItem()

class carousellCrawler(CrawlSpider):
    name='carousell_user_sold'
    global memberlist
    memberlist=[]
    start_urls=[]
    for i in range(1,2):
        try:
            start_urls.append('https://carousell.com/categories/women-s-fashion-4/?page='+str(i))
        except:
            pass

    def parse(self, response):
        list_page=BeautifulSoup(response.body)
        domain='https://carousell.com/'        
        for user in list_page.select('h3'):
            user=str(user)
            user_id=re.search('>(.*?)</h3>',user,re.S).group(1)
            if user_id in memberlist:
                continue
            else:
                yield scrapy.Request('https://carousell.com/ui/iso/api-main;path=%2F2.0%2Fuser%2F'+user_id+'%2Fproducts%2F;query=%7B%22start%22%3A0%2C%22count%22%3A3000%2C%22sort%22%3A%22recent%22%7D;requireAuth=false?_csrf=XJGqQy4y-0BxffIG5Yyx6BxpZt3C7fSze-IQ&returnMeta=true', self.parse_detail_1)
                #yield scrapy.Request('https://carousell.com/ui/iso/api;path=%2Fprofiles%2F'+ user_id+'%2Freviews%2F;query=%7B%22count%22%3A6%2C%22user_type%22%3A%22S%22%7D?_csrf=KpacvfN1-MsPDEyCUwKWweiGEj3n9QkXuxNI&returnMeta=true', self.parse_detail_2)    
                memberlist.append(user_id)

#       for user in list_page.select('h3'):
#            user=str(user)
#            user_id=re.search('>(.*?)</h3>',user,re.S).group(1)
#            if user_id in memberlist:
#                continue
#            else:
#                yield scrapy.Request(domain+ user_id, self.parse_detail_2)
#                memberlist.append(user_id)

    def parse_detail_1(self, response):
        user_product_json= json.loads(response.body_as_unicode())
        sold=0
        unsold=0
        revenue=0.0
        for i in range(3000):
            try:
                if user_product_json['data'][i]['status'] == 'S':
                    sold=sold+1
                    revenue=revenue+float(user_product_json['data'][i]['price'])
                else:
                    unsold=unsold+1
            except:
                continue
        user_data['user_id']=user_product_json['data'][0]['seller']['username']
        user_data['user_sold']=sold
        user_data['user_revenue']=revenue
        user_data['user_unsold']=unsold
        return user_data
        
    def parse_detail_2(self, response):
        user_comment_json= json.loads(response.body_as_unicode())
        global greview
        greview=0
        global breview
        breview=0
        for i in range(3000):
            try:
                if user_comment_json['data']['result'][i]['review_type'] == '+':
                    greview=greview+1
                else:
                    breview=breview+1
            except:
                continue
        user_data['user_greview']=greview
        user_data['user_breview']=breview
        return user_data
        
#    def parse_detail_3(self, response):
#        user_html= BeautifulSoup(response.body)