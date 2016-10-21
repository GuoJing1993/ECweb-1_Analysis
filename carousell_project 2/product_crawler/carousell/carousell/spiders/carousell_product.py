# -*- coding: utf-8 -*-

import scrapy
from bs4 import BeautifulSoup
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re
from carousell.items import CarousellItem
import requests
import time

#---她的時尚---

class carousellSpider1(CrawlSpider):
    name='1'
    allowed_domains = ['carousell.com']
    l=[]
    #x=requests.get('https://carousell.com/')
    #x=x.text
    #y=re.findall('<a href="(/categories/.*?/)" title=".*?" data-reactid=".*?">',x)
    #for i in y[0:3]:
    for j in range(1,350):
        l.append('https://carousell.com/categories/women-s-fashion-4/?page='+str(j))

    start_urls=l

    #rules=[
    #    Rule(LinkExtractor(allow=('women-s-fashion-4')), callback='parse_list', follow=True)
    #]
    
    def parse(self, response):
        global list_page
        list_page=BeautifulSoup(response.body)
        for item in list_page.select('a.pdt-card-thumbnail'):
            item=str(item)
            item_id=re.search('href="/p/(.*?)/',item,re.S).group(1)
            yield scrapy.Request('https://carousell.com/p/'+ item_id, self.parse_detail)
            time.sleep(0.5)
       
    def parse_detail(self, response):
         
         item_data=CarousellItem()
         
         # --- 以下是商品資訊 ---
         item_data['item_category']='women-s-fashion-4'
         item_html= BeautifulSoup(response.body)
         item_id=re.search('app-argument=https://carousell.com/p/(.*?)/',str(item_html),re.S).group(1)
         item_data['item_id']=item_id
         
         item_title=re.search('<title data-react-helmet="true">(.*?)</title>',str(item_html),re.S).group(1)
         item_data['item_title']=item_title
         
         item_keywords=item_html.find("meta", {"name":"keywords"})['content']
         item_data['item_keywords']=item_keywords
         
         item_description=item_html.find("meta", {"name":"description"})['content'].replace("\n", " ").strip()
         item_data['item_description']=item_description
         
         try:
            item_label=item_html.find("span",{"class":"pdt-buy-box-condition label label-info"}).string
         except:
            item_label = None
         item_data['item_label']=item_label
                  
         item_sellerName=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1].string
         item_data['item_sellerName']=item_sellerName
         
         url=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1]['href']
         item_sellerurl='https://carousell.com'+url
         item_data['item_sellerurl']=item_sellerurl

         price=item_html.find("i",{"class":"fa fa-tag"}).parent
         item_price=re.search('-->NT\$(.*?)<!--',str(price)).group(1)
         item_data['item_price']=item_price
              
         loc=item_html.find("i",{"class":"fa fa-map-marker"}).parent.contents[1]
         item_location=re.search('>(.*?), Taiwan',str(loc)).group(1)
         item_data['item_location']=item_location
                  
         try:
            item_face_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-male"}).parent.contents[1].contents[0].string
            item_face_able=1
         except:
            item_face_able=0
         item_data['item_face_able']=item_face_able
            
         try:
            item_truck_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-truck"}).parent.contents[1].contents[0].string
            item_truck_able=1
         except:
            item_truck_able=0
         item_data['item_truck_able']=item_truck_able

         likes=item_html.find("span",{"class":"pdt-buy-box-likes-count"}).parent
         item_likes=re.search('-->(.*?)<!--',str(likes)).group(1)
         item_data['item_likes']=item_likes

         post_time=item_html.find("time",{"class":"text-muted"}).contents[1].string
         item_data['post_time']=post_time
            
         return item_data

#---他的時尚---

class carousellSpider2(CrawlSpider):
    name='2'
    allowed_domains = ['carousell.com']
    l=[]
    #x=requests.get('https://carousell.com/')
    #x=x.text
    #y=re.findall('<a href="(/categories/.*?/)" title=".*?" data-reactid=".*?">',x)
    #for i in y[0:3]:
    for j in range(1,350):
        l.append('https://carousell.com/categories/men-s-fashion-3/?page='+str(j))

    start_urls=l

    #rules=[
    #    Rule(LinkExtractor(allow=('women-s-fashion-4')), callback='parse_list', follow=True)
    #]
    
    def parse(self, response):
        global list_page
        list_page=BeautifulSoup(response.body)
        for item in list_page.select('a.pdt-card-thumbnail'):
            item=str(item)
            item_id=re.search('href="/p/(.*?)/',item,re.S).group(1)
            yield scrapy.Request('https://carousell.com/p/'+ item_id, self.parse_detail)
            time.sleep(0.5)            
       
    def parse_detail(self, response):
         
         item_data=CarousellItem()
         
         # --- 以下是商品資訊 ---
         item_data['item_category']='men-s-fashion-3'
         item_html= BeautifulSoup(response.body)
         item_id=re.search('app-argument=https://carousell.com/p/(.*?)/',str(item_html),re.S).group(1)
         item_data['item_id']=item_id
         
         item_title=re.search('<title data-react-helmet="true">(.*?)</title>',str(item_html),re.S).group(1)
         item_data['item_title']=item_title
         
         item_keywords=item_html.find("meta", {"name":"keywords"})['content']
         item_data['item_keywords']=item_keywords
         
         item_description=item_html.find("meta", {"name":"description"})['content'].replace("\n", " ").strip()
         item_data['item_description']=item_description
         
         try:
            item_label=item_html.find("span",{"class":"pdt-buy-box-condition label label-info"}).string
         except:
            item_label = None
         item_data['item_label']=item_label
                  
         item_sellerName=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1].string
         item_data['item_sellerName']=item_sellerName
         
         url=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1]['href']
         item_sellerurl='https://carousell.com'+url
         item_data['item_sellerurl']=item_sellerurl

         price=item_html.find("i",{"class":"fa fa-tag"}).parent
         item_price=re.search('-->NT\$(.*?)<!--',str(price)).group(1)
         item_data['item_price']=item_price
              
         loc=item_html.find("i",{"class":"fa fa-map-marker"}).parent.contents[1]
         item_location=re.search('>(.*?), Taiwan',str(loc)).group(1)
         item_data['item_location']=item_location
                  
         try:
            item_face_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-male"}).parent.contents[1].contents[0].string
            item_face_able=1
         except:
            item_face_able=0
         item_data['item_face_able']=item_face_able
            
         try:
            item_truck_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-truck"}).parent.contents[1].contents[0].string
            item_truck_able=1
         except:
            item_truck_able=0
         item_data['item_truck_able']=item_truck_able

         likes=item_html.find("span",{"class":"pdt-buy-box-likes-count"}).parent
         item_likes=re.search('-->(.*?)<!--',str(likes)).group(1)
         item_data['item_likes']=item_likes

         post_time=item_html.find("time",{"class":"text-muted"}).contents[1].string
         item_data['post_time']=post_time
            
         return item_data

#---名牌精品---

class carousellSpider3(CrawlSpider):
    name='3'
    allowed_domains = ['carousell.com']
    l=[]
    #x=requests.get('https://carousell.com/')
    #x=x.text
    #y=re.findall('<a href="(/categories/.*?/)" title=".*?" data-reactid=".*?">',x)
    #for i in y[0:3]:
    for j in range(1,350):
        l.append('https://carousell.com/categories/luxury-20/?page='+str(j))

    start_urls=l

    #rules=[
    #    Rule(LinkExtractor(allow=('women-s-fashion-4')), callback='parse_list', follow=True)
    #]
    
    def parse(self, response):
        global list_page
        list_page=BeautifulSoup(response.body)
        for item in list_page.select('a.pdt-card-thumbnail'):
            item=str(item)
            item_id=re.search('href="/p/(.*?)/',item,re.S).group(1)
            yield scrapy.Request('https://carousell.com/p/'+ item_id, self.parse_detail)
            time.sleep(0.5)            
       
    def parse_detail(self, response):
         
         item_data=CarousellItem()
         
         # --- 以下是商品資訊 ---
         item_data['item_category']='luxury-20'
         item_html= BeautifulSoup(response.body)
         item_id=re.search('app-argument=https://carousell.com/p/(.*?)/',str(item_html),re.S).group(1)
         item_data['item_id']=item_id
         
         item_title=re.search('<title data-react-helmet="true">(.*?)</title>',str(item_html),re.S).group(1)
         item_data['item_title']=item_title
         
         item_keywords=item_html.find("meta", {"name":"keywords"})['content']
         item_data['item_keywords']=item_keywords
         
         item_description=item_html.find("meta", {"name":"description"})['content'].replace("\n", " ").strip()
         item_data['item_description']=item_description
         
         try:
            item_label=item_html.find("span",{"class":"pdt-buy-box-condition label label-info"}).string
         except:
            item_label = None
         item_data['item_label']=item_label
                  
         item_sellerName=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1].string
         item_data['item_sellerName']=item_sellerName
         
         url=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1]['href']
         item_sellerurl='https://carousell.com'+url
         item_data['item_sellerurl']=item_sellerurl

         price=item_html.find("i",{"class":"fa fa-tag"}).parent
         item_price=re.search('-->NT\$(.*?)<!--',str(price)).group(1)
         item_data['item_price']=item_price
              
         loc=item_html.find("i",{"class":"fa fa-map-marker"}).parent.contents[1]
         item_location=re.search('>(.*?), Taiwan',str(loc)).group(1)
         item_data['item_location']=item_location
                  
         try:
            item_face_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-male"}).parent.contents[1].contents[0].string
            item_face_able=1
         except:
            item_face_able=0
         item_data['item_face_able']=item_face_able
            
         try:
            item_truck_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-truck"}).parent.contents[1].contents[0].string
            item_truck_able=1
         except:
            item_truck_able=0
         item_data['item_truck_able']=item_truck_able

         likes=item_html.find("span",{"class":"pdt-buy-box-likes-count"}).parent
         item_likes=re.search('-->(.*?)<!--',str(likes)).group(1)
         item_data['item_likes']=item_likes

         post_time=item_html.find("time",{"class":"text-muted"}).contents[1].string
         item_data['post_time']=post_time
            
         return item_data
         
#---美妝保養---

class carousellSpider4(CrawlSpider):
    name='4'
    allowed_domains = ['carousell.com']
    l=[]
    #x=requests.get('https://carousell.com/')
    #x=x.text
    #y=re.findall('<a href="(/categories/.*?/)" title=".*?" data-reactid=".*?">',x)
    #for i in y[0:3]:
    for j in range(1,350):
        l.append('https://carousell.com/categories/health-beauty-11/?page='+str(j))

    start_urls=l

    #rules=[
    #    Rule(LinkExtractor(allow=('women-s-fashion-4')), callback='parse_list', follow=True)
    #]
    
    def parse(self, response):
        global list_page
        list_page=BeautifulSoup(response.body)
        for item in list_page.select('a.pdt-card-thumbnail'):
            item=str(item)
            item_id=re.search('href="/p/(.*?)/',item,re.S).group(1)
            yield scrapy.Request('https://carousell.com/p/'+ item_id, self.parse_detail)
            time.sleep(0.5)            
       
    def parse_detail(self, response):
         
         item_data=CarousellItem()
         
         # --- 以下是商品資訊 ---
         item_data['item_category']='health-beauty-11'
         item_html= BeautifulSoup(response.body)
         item_id=re.search('app-argument=https://carousell.com/p/(.*?)/',str(item_html),re.S).group(1)
         item_data['item_id']=item_id
         
         item_title=re.search('<title data-react-helmet="true">(.*?)</title>',str(item_html),re.S).group(1)
         item_data['item_title']=item_title
         
         item_keywords=item_html.find("meta", {"name":"keywords"})['content']
         item_data['item_keywords']=item_keywords
         
         item_description=item_html.find("meta", {"name":"description"})['content'].replace("\n", " ").strip()
         item_data['item_description']=item_description
         
         try:
            item_label=item_html.find("span",{"class":"pdt-buy-box-condition label label-info"}).string
         except:
            item_label = None
         item_data['item_label']=item_label
                  
         item_sellerName=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1].string
         item_data['item_sellerName']=item_sellerName
         
         url=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1]['href']
         item_sellerurl='https://carousell.com'+url
         item_data['item_sellerurl']=item_sellerurl

         price=item_html.find("i",{"class":"fa fa-tag"}).parent
         item_price=re.search('-->NT\$(.*?)<!--',str(price)).group(1)
         item_data['item_price']=item_price
              
         loc=item_html.find("i",{"class":"fa fa-map-marker"}).parent.contents[1]
         item_location=re.search('>(.*?), Taiwan',str(loc)).group(1)
         item_data['item_location']=item_location
                  
         try:
            item_face_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-male"}).parent.contents[1].contents[0].string
            item_face_able=1
         except:
            item_face_able=0
         item_data['item_face_able']=item_face_able
            
         try:
            item_truck_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-truck"}).parent.contents[1].contents[0].string
            item_truck_able=1
         except:
            item_truck_able=0
         item_data['item_truck_able']=item_truck_able

         likes=item_html.find("span",{"class":"pdt-buy-box-likes-count"}).parent
         item_likes=re.search('-->(.*?)<!--',str(likes)).group(1)
         item_data['item_likes']=item_likes

         post_time=item_html.find("time",{"class":"text-muted"}).contents[1].string
         item_data['post_time']=post_time
            
         return item_data

#---居家生活---

class carousellSpider5(CrawlSpider):
    name='5'
    allowed_domains = ['carousell.com']
    l=[]
    #headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
    #x=requests.get('https://carousell.com/')
    #x=x.text
    #y=re.findall('<a href="(/categories/.*?/)" title=".*?" data-reactid=".*?">',x)
    #for i in y[0:3]:
    for j in range(1,350):
        l.append('https://carousell.com/categories/furniture-home-13/?page='+str(j))

    start_urls=l

    #rules=[
    #    Rule(LinkExtractor(allow=('women-s-fashion-4')), callback='parse_list', follow=True)
    #]
    
    def parse(self, response):
        global list_page
        list_page=BeautifulSoup(response.body)
        for item in list_page.select('a.pdt-card-thumbnail'):
            item=str(item)
            item_id=re.search('href="/p/(.*?)/',item,re.S).group(1)
            yield scrapy.Request('https://carousell.com/p/'+ item_id, self.parse_detail)
            time.sleep(0.5)
       
    def parse_detail(self, response):
         
         item_data=CarousellItem()
         
         # --- 以下是商品資訊 ---
         item_data['item_category']='furniture-home-13'
         item_html= BeautifulSoup(response.body)
         item_id=re.search('app-argument=https://carousell.com/p/(.*?)/',str(item_html),re.S).group(1)
         item_data['item_id']=item_id
         
         item_title=re.search('<title data-react-helmet="true">(.*?)</title>',str(item_html),re.S).group(1)
         item_data['item_title']=item_title
         
         item_keywords=item_html.find("meta", {"name":"keywords"})['content']
         item_data['item_keywords']=item_keywords
         
         item_description=item_html.find("meta", {"name":"description"})['content'].replace("\n", " ").strip()
         item_data['item_description']=item_description
         
         try:
            item_label=item_html.find("span",{"class":"pdt-buy-box-condition label label-info"}).string
         except:
            item_label = None
         item_data['item_label']=item_label
                  
         item_sellerName=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1].string
         item_data['item_sellerName']=item_sellerName
         
         url=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1]['href']
         item_sellerurl='https://carousell.com'+url
         item_data['item_sellerurl']=item_sellerurl

         price=item_html.find("i",{"class":"fa fa-tag"}).parent
         item_price=re.search('-->NT\$(.*?)<!--',str(price)).group(1)
         item_data['item_price']=item_price
              
         loc=item_html.find("i",{"class":"fa fa-map-marker"}).parent.contents[1]
         item_location=re.search('>(.*?), Taiwan',str(loc)).group(1)
         item_data['item_location']=item_location
                  
         try:
            item_face_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-male"}).parent.contents[1].contents[0].string
            item_face_able=1
         except:
            item_face_able=0
         item_data['item_face_able']=item_face_able
            
         try:
            item_truck_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-truck"}).parent.contents[1].contents[0].string
            item_truck_able=1
         except:
            item_truck_able=0
         item_data['item_truck_able']=item_truck_able

         likes=item_html.find("span",{"class":"pdt-buy-box-likes-count"}).parent
         item_likes=re.search('-->(.*?)<!--',str(likes)).group(1)
         item_data['item_likes']=item_likes

         post_time=item_html.find("time",{"class":"text-muted"}).contents[1].string
         item_data['post_time']=post_time
            
         return item_data

#---廚房電器---

class carousellSpider6(CrawlSpider):
    name='6'
    allowed_domains = ['carousell.com']
    l=[]
    #x=requests.get('https://carousell.com/')
    #x=x.text
    #y=re.findall('<a href="(/categories/.*?/)" title=".*?" data-reactid=".*?">',x)
    #for i in y[0:3]:
    for j in range(1,350):
        l.append('https://carousell.com/categories/kitchen-appliances-30/?page='+str(j))

    start_urls=l

    #rules=[
    #    Rule(LinkExtractor(allow=('women-s-fashion-4')), callback='parse_list', follow=True)
    #]
    
    def parse(self, response):
        global list_page
        list_page=BeautifulSoup(response.body)
        for item in list_page.select('a.pdt-card-thumbnail'):
            item=str(item)
            item_id=re.search('href="/p/(.*?)/',item,re.S).group(1)
            yield scrapy.Request('https://carousell.com/p/'+ item_id, self.parse_detail)
       
    def parse_detail(self, response):
         
         item_data=CarousellItem()
         
         # --- 以下是商品資訊 ---
         item_data['item_category']='kitchen-appliances-30'
         item_html= BeautifulSoup(response.body)
         item_id=re.search('app-argument=https://carousell.com/p/(.*?)/',str(item_html),re.S).group(1)
         item_data['item_id']=item_id
         
         item_title=re.search('<title data-react-helmet="true">(.*?)</title>',str(item_html),re.S).group(1)
         item_data['item_title']=item_title
         
         item_keywords=item_html.find("meta", {"name":"keywords"})['content']
         item_data['item_keywords']=item_keywords
         
         item_description=item_html.find("meta", {"name":"description"})['content'].replace("\n", " ").strip()
         item_data['item_description']=item_description
         
         try:
            item_label=item_html.find("span",{"class":"pdt-buy-box-condition label label-info"}).string
         except:
            item_label = None
         item_data['item_label']=item_label
                  
         item_sellerName=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1].string
         item_data['item_sellerName']=item_sellerName
         
         url=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1]['href']
         item_sellerurl='https://carousell.com'+url
         item_data['item_sellerurl']=item_sellerurl

         price=item_html.find("i",{"class":"fa fa-tag"}).parent
         item_price=re.search('-->NT\$(.*?)<!--',str(price)).group(1)
         item_data['item_price']=item_price
              
         loc=item_html.find("i",{"class":"fa fa-map-marker"}).parent.contents[1]
         item_location=re.search('>(.*?), Taiwan',str(loc)).group(1)
         item_data['item_location']=item_location
                  
         try:
            item_face_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-male"}).parent.contents[1].contents[0].string
            item_face_able=1
         except:
            item_face_able=0
         item_data['item_face_able']=item_face_able
            
         try:
            item_truck_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-truck"}).parent.contents[1].contents[0].string
            item_truck_able=1
         except:
            item_truck_able=0
         item_data['item_truck_able']=item_truck_able

         likes=item_html.find("span",{"class":"pdt-buy-box-likes-count"}).parent
         item_likes=re.search('-->(.*?)<!--',str(likes)).group(1)
         item_data['item_likes']=item_likes

         post_time=item_html.find("time",{"class":"text-muted"}).contents[1].string
         item_data['post_time']=post_time
            
         return item_data

#---媽媽寶寶---

class carousellSpider7(CrawlSpider):
    name='7'
    allowed_domains = ['carousell.com']
    l=[]
    #x=requests.get('https://carousell.com/')
    #x=x.text
    #y=re.findall('<a href="(/categories/.*?/)" title=".*?" data-reactid=".*?">',x)
    #for i in y[0:3]:
    for j in range(1,350):
        l.append('https://carousell.com/categories/parents-babies-kids-19/?page='+str(j))

    start_urls=l

    #rules=[
    #    Rule(LinkExtractor(allow=('women-s-fashion-4')), callback='parse_list', follow=True)
    #]
    
    def parse(self, response):
        global list_page
        list_page=BeautifulSoup(response.body)
        for item in list_page.select('a.pdt-card-thumbnail'):
            item=str(item)
            item_id=re.search('href="/p/(.*?)/',item,re.S).group(1)
            yield scrapy.Request('https://carousell.com/p/'+ item_id, self.parse_detail)
       
    def parse_detail(self, response):
         
         item_data=CarousellItem()
         
         # --- 以下是商品資訊 ---
         item_data['item_category']='parents-babies-kids-19'
         item_html= BeautifulSoup(response.body)
         item_id=re.search('app-argument=https://carousell.com/p/(.*?)/',str(item_html),re.S).group(1)
         item_data['item_id']=item_id
         
         item_title=re.search('<title data-react-helmet="true">(.*?)</title>',str(item_html),re.S).group(1)
         item_data['item_title']=item_title
         
         item_keywords=item_html.find("meta", {"name":"keywords"})['content']
         item_data['item_keywords']=item_keywords
         
         item_description=item_html.find("meta", {"name":"description"})['content'].replace("\n", " ").strip()
         item_data['item_description']=item_description
         
         try:
            item_label=item_html.find("span",{"class":"pdt-buy-box-condition label label-info"}).string
         except:
            item_label = None
         item_data['item_label']=item_label
                  
         item_sellerName=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1].string
         item_data['item_sellerName']=item_sellerName
         
         url=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1]['href']
         item_sellerurl='https://carousell.com'+url
         item_data['item_sellerurl']=item_sellerurl

         price=item_html.find("i",{"class":"fa fa-tag"}).parent
         item_price=re.search('-->NT\$(.*?)<!--',str(price)).group(1)
         item_data['item_price']=item_price
              
         loc=item_html.find("i",{"class":"fa fa-map-marker"}).parent.contents[1]
         item_location=re.search('>(.*?), Taiwan',str(loc)).group(1)
         item_data['item_location']=item_location
                  
         try:
            item_face_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-male"}).parent.contents[1].contents[0].string
            item_face_able=1
         except:
            item_face_able=0
         item_data['item_face_able']=item_face_able
            
         try:
            item_truck_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-truck"}).parent.contents[1].contents[0].string
            item_truck_able=1
         except:
            item_truck_able=0
         item_data['item_truck_able']=item_truck_able

         likes=item_html.find("span",{"class":"pdt-buy-box-likes-count"}).parent
         item_likes=re.search('-->(.*?)<!--',str(likes)).group(1)
         item_data['item_likes']=item_likes

         post_time=item_html.find("time",{"class":"text-muted"}).contents[1].string
         item_data['post_time']=post_time
            
         return item_data

#---賣屋租屋---

class carousellSpider8(CrawlSpider):
    name='8'
    allowed_domains = ['carousell.com']
    l=[]
    #x=requests.get('https://carousell.com/')
    #x=x.text
    #y=re.findall('<a href="(/categories/.*?/)" title=".*?" data-reactid=".*?">',x)
    #for i in y[0:3]:
    for j in range(1,350):
        l.append('https://carousell.com/categories/property-102/?page='+str(j))

    start_urls=l

    #rules=[
    #    Rule(LinkExtractor(allow=('women-s-fashion-4')), callback='parse_list', follow=True)
    #]
    
    def parse(self, response):
        global list_page
        list_page=BeautifulSoup(response.body)
        for item in list_page.select('a.pdt-card-thumbnail'):
            item=str(item)
            item_id=re.search('href="/p/(.*?)/',item,re.S).group(1)
            yield scrapy.Request('https://carousell.com/p/'+ item_id, self.parse_detail)
       
    def parse_detail(self, response):
         
         item_data=CarousellItem()
         
         # --- 以下是商品資訊 ---
         item_data['item_category']='property-102'
         item_html= BeautifulSoup(response.body)
         item_id=re.search('app-argument=https://carousell.com/p/(.*?)/',str(item_html),re.S).group(1)
         item_data['item_id']=item_id
         
         item_title=re.search('<title data-react-helmet="true">(.*?)</title>',str(item_html),re.S).group(1)
         item_data['item_title']=item_title
         
         item_keywords=item_html.find("meta", {"name":"keywords"})['content']
         item_data['item_keywords']=item_keywords
         
         item_description=item_html.find("meta", {"name":"description"})['content'].replace("\n", " ").strip()
         item_data['item_description']=item_description
         
         try:
            item_label=item_html.find("span",{"class":"pdt-buy-box-condition label label-info"}).string
         except:
            item_label = None
         item_data['item_label']=item_label
                  
         item_sellerName=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1].string
         item_data['item_sellerName']=item_sellerName
         
         url=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1]['href']
         item_sellerurl='https://carousell.com'+url
         item_data['item_sellerurl']=item_sellerurl

         price=item_html.find("i",{"class":"fa fa-tag"}).parent
         item_price=re.search('-->NT\$(.*?)<!--',str(price)).group(1)
         item_data['item_price']=item_price
              
         loc=item_html.find("i",{"class":"fa fa-map-marker"}).parent.contents[1]
         item_location=re.search('>(.*?), Taiwan',str(loc)).group(1)
         item_data['item_location']=item_location
                  
         try:
            item_face_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-male"}).parent.contents[1].contents[0].string
            item_face_able=1
         except:
            item_face_able=0
         item_data['item_face_able']=item_face_able
            
         try:
            item_truck_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-truck"}).parent.contents[1].contents[0].string
            item_truck_able=1
         except:
            item_truck_able=0
         item_data['item_truck_able']=item_truck_able

         likes=item_html.find("span",{"class":"pdt-buy-box-likes-count"}).parent
         item_likes=re.search('-->(.*?)<!--',str(likes)).group(1)
         item_data['item_likes']=item_likes

         post_time=item_html.find("time",{"class":"text-muted"}).contents[1].string
         item_data['post_time']=post_time
            
         return item_data
         
#---手作設計---

class carousellSpider9(CrawlSpider):
    name='9'
    allowed_domains = ['carousell.com']
    l=[]
    #x=requests.get('https://carousell.com/')
    #x=x.text
    #y=re.findall('<a href="(/categories/.*?/)" title=".*?" data-reactid=".*?">',x)
    #for i in y[0:3]:
    for j in range(1,350):
        l.append('https://carousell.com/categories/design-craft-8/?page='+str(j))

    start_urls=l

    #rules=[
    #    Rule(LinkExtractor(allow=('women-s-fashion-4')), callback='parse_list', follow=True)
    #]
    
    def parse(self, response):
        global list_page
        list_page=BeautifulSoup(response.body)
        for item in list_page.select('a.pdt-card-thumbnail'):
            item=str(item)
            item_id=re.search('href="/p/(.*?)/',item,re.S).group(1)
            yield scrapy.Request('https://carousell.com/p/'+ item_id, self.parse_detail)
       
    def parse_detail(self, response):
         
         item_data=CarousellItem()
         
         # --- 以下是商品資訊 ---
         item_data['item_category']='design-craft-8'
         item_html= BeautifulSoup(response.body)
         item_id=re.search('app-argument=https://carousell.com/p/(.*?)/',str(item_html),re.S).group(1)
         item_data['item_id']=item_id
         
         item_title=re.search('<title data-react-helmet="true">(.*?)</title>',str(item_html),re.S).group(1)
         item_data['item_title']=item_title
         
         item_keywords=item_html.find("meta", {"name":"keywords"})['content']
         item_data['item_keywords']=item_keywords
         
         item_description=item_html.find("meta", {"name":"description"})['content'].replace("\n", " ").strip()
         item_data['item_description']=item_description
         
         try:
            item_label=item_html.find("span",{"class":"pdt-buy-box-condition label label-info"}).string
         except:
            item_label = None
         item_data['item_label']=item_label
                  
         item_sellerName=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1].string
         item_data['item_sellerName']=item_sellerName
         
         url=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1]['href']
         item_sellerurl='https://carousell.com'+url
         item_data['item_sellerurl']=item_sellerurl

         price=item_html.find("i",{"class":"fa fa-tag"}).parent
         item_price=re.search('-->NT\$(.*?)<!--',str(price)).group(1)
         item_data['item_price']=item_price
              
         loc=item_html.find("i",{"class":"fa fa-map-marker"}).parent.contents[1]
         item_location=re.search('>(.*?), Taiwan',str(loc)).group(1)
         item_data['item_location']=item_location
                  
         try:
            item_face_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-male"}).parent.contents[1].contents[0].string
            item_face_able=1
         except:
            item_face_able=0
         item_data['item_face_able']=item_face_able
            
         try:
            item_truck_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-truck"}).parent.contents[1].contents[0].string
            item_truck_able=1
         except:
            item_truck_able=0
         item_data['item_truck_able']=item_truck_able

         likes=item_html.find("span",{"class":"pdt-buy-box-likes-count"}).parent
         item_likes=re.search('-->(.*?)<!--',str(likes)).group(1)
         item_data['item_likes']=item_likes

         post_time=item_html.find("time",{"class":"text-muted"}).contents[1].string
         item_data['post_time']=post_time
            
         return item_data

#---3C---

class carousellSpider10(CrawlSpider):
    name='10'
    allowed_domains = ['carousell.com']
    l=[]
    #x=requests.get('https://carousell.com/')
    #x=x.text
    #y=re.findall('<a href="(/categories/.*?/)" title=".*?" data-reactid=".*?">',x)
    #for i in y[0:3]:
    for j in range(1,350):
        l.append('https://carousell.com/categories/electronics-gadgets-7/?page='+str(j))

    start_urls=l

    #rules=[
    #    Rule(LinkExtractor(allow=('women-s-fashion-4')), callback='parse_list', follow=True)
    #]
    
    def parse(self, response):
        global list_page
        list_page=BeautifulSoup(response.body)
        for item in list_page.select('a.pdt-card-thumbnail'):
            item=str(item)
            item_id=re.search('href="/p/(.*?)/',item,re.S).group(1)
            yield scrapy.Request('https://carousell.com/p/'+ item_id, self.parse_detail)
       
    def parse_detail(self, response):
         
         item_data=CarousellItem()
         
         # --- 以下是商品資訊 ---
         item_data['item_category']='electronics-gadgets-7'
         item_html= BeautifulSoup(response.body)
         item_id=re.search('app-argument=https://carousell.com/p/(.*?)/',str(item_html),re.S).group(1)
         item_data['item_id']=item_id
         
         item_title=re.search('<title data-react-helmet="true">(.*?)</title>',str(item_html),re.S).group(1)
         item_data['item_title']=item_title
         
         item_keywords=item_html.find("meta", {"name":"keywords"})['content']
         item_data['item_keywords']=item_keywords
         
         item_description=item_html.find("meta", {"name":"description"})['content'].replace("\n", " ").strip()
         item_data['item_description']=item_description
         
         try:
            item_label=item_html.find("span",{"class":"pdt-buy-box-condition label label-info"}).string
         except:
            item_label = None
         item_data['item_label']=item_label
                  
         item_sellerName=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1].string
         item_data['item_sellerName']=item_sellerName
         
         url=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1]['href']
         item_sellerurl='https://carousell.com'+url
         item_data['item_sellerurl']=item_sellerurl

         price=item_html.find("i",{"class":"fa fa-tag"}).parent
         item_price=re.search('-->NT\$(.*?)<!--',str(price)).group(1)
         item_data['item_price']=item_price
              
         loc=item_html.find("i",{"class":"fa fa-map-marker"}).parent.contents[1]
         item_location=re.search('>(.*?), Taiwan',str(loc)).group(1)
         item_data['item_location']=item_location
                  
         try:
            item_face_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-male"}).parent.contents[1].contents[0].string
            item_face_able=1
         except:
            item_face_able=0
         item_data['item_face_able']=item_face_able
            
         try:
            item_truck_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-truck"}).parent.contents[1].contents[0].string
            item_truck_able=1
         except:
            item_truck_able=0
         item_data['item_truck_able']=item_truck_able

         likes=item_html.find("span",{"class":"pdt-buy-box-likes-count"}).parent
         item_likes=re.search('-->(.*?)<!--',str(likes)).group(1)
         item_data['item_likes']=item_likes

         post_time=item_html.find("time",{"class":"text-muted"}).contents[1].string
         item_data['post_time']=post_time
            
         return item_data

#---音樂---

class carousellSpider11(CrawlSpider):
    name='11'
    allowed_domains = ['carousell.com']
    l=[]
    #x=requests.get('https://carousell.com/')
    #x=x.text
    #y=re.findall('<a href="(/categories/.*?/)" title=".*?" data-reactid=".*?">',x)
    #for i in y[0:3]:
    for j in range(1,350):
        l.append('https://carousell.com/categories/music-14/?page='+str(j))

    start_urls=l

    #rules=[
    #    Rule(LinkExtractor(allow=('women-s-fashion-4')), callback='parse_list', follow=True)
    #]
    
    def parse(self, response):
        global list_page
        list_page=BeautifulSoup(response.body)
        for item in list_page.select('a.pdt-card-thumbnail'):
            item=str(item)
            item_id=re.search('href="/p/(.*?)/',item,re.S).group(1)
            yield scrapy.Request('https://carousell.com/p/'+ item_id, self.parse_detail)
       
    def parse_detail(self, response):
         
         item_data=CarousellItem()
         
         # --- 以下是商品資訊 ---
         item_data['item_category']='music-14'
         item_html= BeautifulSoup(response.body)
         item_id=re.search('app-argument=https://carousell.com/p/(.*?)/',str(item_html),re.S).group(1)
         item_data['item_id']=item_id
         
         item_title=re.search('<title data-react-helmet="true">(.*?)</title>',str(item_html),re.S).group(1)
         item_data['item_title']=item_title
         
         item_keywords=item_html.find("meta", {"name":"keywords"})['content']
         item_data['item_keywords']=item_keywords
         
         item_description=item_html.find("meta", {"name":"description"})['content'].replace("\n", " ").strip()
         item_data['item_description']=item_description
         
         try:
            item_label=item_html.find("span",{"class":"pdt-buy-box-condition label label-info"}).string
         except:
            item_label = None
         item_data['item_label']=item_label
                  
         item_sellerName=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1].string
         item_data['item_sellerName']=item_sellerName
         
         url=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1]['href']
         item_sellerurl='https://carousell.com'+url
         item_data['item_sellerurl']=item_sellerurl

         price=item_html.find("i",{"class":"fa fa-tag"}).parent
         item_price=re.search('-->NT\$(.*?)<!--',str(price)).group(1)
         item_data['item_price']=item_price
              
         loc=item_html.find("i",{"class":"fa fa-map-marker"}).parent.contents[1]
         item_location=re.search('>(.*?), Taiwan',str(loc)).group(1)
         item_data['item_location']=item_location
                  
         try:
            item_face_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-male"}).parent.contents[1].contents[0].string
            item_face_able=1
         except:
            item_face_able=0
         item_data['item_face_able']=item_face_able
            
         try:
            item_truck_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-truck"}).parent.contents[1].contents[0].string
            item_truck_able=1
         except:
            item_truck_able=0
         item_data['item_truck_able']=item_truck_able

         likes=item_html.find("span",{"class":"pdt-buy-box-likes-count"}).parent
         item_likes=re.search('-->(.*?)<!--',str(likes)).group(1)
         item_data['item_likes']=item_likes

         post_time=item_html.find("time",{"class":"text-muted"}).contents[1].string
         item_data['post_time']=post_time
            
         return item_data

#---賣屋租屋---

class carousellSpider12(CrawlSpider):
    name='12'
    allowed_domains = ['carousell.com']
    l=[]
    #x=requests.get('https://carousell.com/')
    #x=x.text
    #y=re.findall('<a href="(/categories/.*?/)" title=".*?" data-reactid=".*?">',x)
    #for i in y[0:3]:
    for j in range(1,350):
        l.append('https://carousell.com/categories/photography-6/?page='+str(j))

    start_urls=l

    #rules=[
    #    Rule(LinkExtractor(allow=('women-s-fashion-4')), callback='parse_list', follow=True)
    #]
    
    def parse(self, response):
        global list_page
        list_page=BeautifulSoup(response.body)
        for item in list_page.select('a.pdt-card-thumbnail'):
            item=str(item)
            item_id=re.search('href="/p/(.*?)/',item,re.S).group(1)
            yield scrapy.Request('https://carousell.com/p/'+ item_id, self.parse_detail)
       
    def parse_detail(self, response):
         
         item_data=CarousellItem()
         
         # --- 以下是商品資訊 ---
         item_data['item_category']='photography-6'
         item_html= BeautifulSoup(response.body)
         item_id=re.search('app-argument=https://carousell.com/p/(.*?)/',str(item_html),re.S).group(1)
         item_data['item_id']=item_id
         
         item_title=re.search('<title data-react-helmet="true">(.*?)</title>',str(item_html),re.S).group(1)
         item_data['item_title']=item_title
         
         item_keywords=item_html.find("meta", {"name":"keywords"})['content']
         item_data['item_keywords']=item_keywords
         
         item_description=item_html.find("meta", {"name":"description"})['content'].replace("\n", " ").strip()
         item_data['item_description']=item_description
         
         try:
            item_label=item_html.find("span",{"class":"pdt-buy-box-condition label label-info"}).string
         except:
            item_label = None
         item_data['item_label']=item_label
                  
         item_sellerName=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1].string
         item_data['item_sellerName']=item_sellerName
         
         url=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1]['href']
         item_sellerurl='https://carousell.com'+url
         item_data['item_sellerurl']=item_sellerurl

         price=item_html.find("i",{"class":"fa fa-tag"}).parent
         item_price=re.search('-->NT\$(.*?)<!--',str(price)).group(1)
         item_data['item_price']=item_price
              
         loc=item_html.find("i",{"class":"fa fa-map-marker"}).parent.contents[1]
         item_location=re.search('>(.*?), Taiwan',str(loc)).group(1)
         item_data['item_location']=item_location
                  
         try:
            item_face_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-male"}).parent.contents[1].contents[0].string
            item_face_able=1
         except:
            item_face_able=0
         item_data['item_face_able']=item_face_able
            
         try:
            item_truck_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-truck"}).parent.contents[1].contents[0].string
            item_truck_able=1
         except:
            item_truck_able=0
         item_data['item_truck_able']=item_truck_able

         likes=item_html.find("span",{"class":"pdt-buy-box-likes-count"}).parent
         item_likes=re.search('-->(.*?)<!--',str(likes)).group(1)
         item_data['item_likes']=item_likes

         post_time=item_html.find("time",{"class":"text-muted"}).contents[1].string
         item_data['post_time']=post_time
            
         return item_data

#---相機配件---

class carousellSpider13(CrawlSpider):
    name='13'
    allowed_domains = ['carousell.com']
    l=[]
    #x=requests.get('https://carousell.com/')
    #x=x.text
    #y=re.findall('<a href="(/categories/.*?/)" title=".*?" data-reactid=".*?">',x)
    #for i in y[0:3]:
    for j in range(1,350):
        l.append('https://carousell.com/categories/property-102/?page='+str(j))

    start_urls=l

    #rules=[
    #    Rule(LinkExtractor(allow=('women-s-fashion-4')), callback='parse_list', follow=True)
    #]
    
    def parse(self, response):
        global list_page
        list_page=BeautifulSoup(response.body)
        for item in list_page.select('a.pdt-card-thumbnail'):
            item=str(item)
            item_id=re.search('href="/p/(.*?)/',item,re.S).group(1)
            yield scrapy.Request('https://carousell.com/p/'+ item_id, self.parse_detail)
       
    def parse_detail(self, response):
         
         item_data=CarousellItem()
         
         # --- 以下是商品資訊 ---
         item_data['item_category']='property-102'
         item_html= BeautifulSoup(response.body)
         item_id=re.search('app-argument=https://carousell.com/p/(.*?)/',str(item_html),re.S).group(1)
         item_data['item_id']=item_id
         
         item_title=re.search('<title data-react-helmet="true">(.*?)</title>',str(item_html),re.S).group(1)
         item_data['item_title']=item_title
         
         item_keywords=item_html.find("meta", {"name":"keywords"})['content']
         item_data['item_keywords']=item_keywords
         
         item_description=item_html.find("meta", {"name":"description"})['content'].replace("\n", " ").strip()
         item_data['item_description']=item_description
         
         try:
            item_label=item_html.find("span",{"class":"pdt-buy-box-condition label label-info"}).string
         except:
            item_label = None
         item_data['item_label']=item_label
                  
         item_sellerName=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1].string
         item_data['item_sellerName']=item_sellerName
         
         url=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1]['href']
         item_sellerurl='https://carousell.com'+url
         item_data['item_sellerurl']=item_sellerurl

         price=item_html.find("i",{"class":"fa fa-tag"}).parent
         item_price=re.search('-->NT\$(.*?)<!--',str(price)).group(1)
         item_data['item_price']=item_price
              
         loc=item_html.find("i",{"class":"fa fa-map-marker"}).parent.contents[1]
         item_location=re.search('>(.*?), Taiwan',str(loc)).group(1)
         item_data['item_location']=item_location
                  
         try:
            item_face_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-male"}).parent.contents[1].contents[0].string
            item_face_able=1
         except:
            item_face_able=0
         item_data['item_face_able']=item_face_able
            
         try:
            item_truck_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-truck"}).parent.contents[1].contents[0].string
            item_truck_able=1
         except:
            item_truck_able=0
         item_data['item_truck_able']=item_truck_able

         likes=item_html.find("span",{"class":"pdt-buy-box-likes-count"}).parent
         item_likes=re.search('-->(.*?)<!--',str(likes)).group(1)
         item_data['item_likes']=item_likes

         post_time=item_html.find("time",{"class":"text-muted"}).contents[1].string
         item_data['post_time']=post_time
            
         return item_data

#---運動休閒---

class carousellSpider14(CrawlSpider):
    name='14'
    allowed_domains = ['carousell.com']
    l=[]
    #x=requests.get('https://carousell.com/')
    #x=x.text
    #y=re.findall('<a href="(/categories/.*?/)" title=".*?" data-reactid=".*?">',x)
    #for i in y[0:3]:
    for j in range(1,350):
        l.append('https://carousell.com/categories/sporting-gear-10/?page='+str(j))

    start_urls=l

    #rules=[
    #    Rule(LinkExtractor(allow=('women-s-fashion-4')), callback='parse_list', follow=True)
    #]
    
    def parse(self, response):
        global list_page
        list_page=BeautifulSoup(response.body)
        for item in list_page.select('a.pdt-card-thumbnail'):
            item=str(item)
            item_id=re.search('href="/p/(.*?)/',item,re.S).group(1)
            yield scrapy.Request('https://carousell.com/p/'+ item_id, self.parse_detail)
       
    def parse_detail(self, response):
         
         item_data=CarousellItem()
         
         # --- 以下是商品資訊 ---
         item_data['item_category']='sporting-gear-10'
         item_html= BeautifulSoup(response.body)
         item_id=re.search('app-argument=https://carousell.com/p/(.*?)/',str(item_html),re.S).group(1)
         item_data['item_id']=item_id
         
         item_title=re.search('<title data-react-helmet="true">(.*?)</title>',str(item_html),re.S).group(1)
         item_data['item_title']=item_title
         
         item_keywords=item_html.find("meta", {"name":"keywords"})['content']
         item_data['item_keywords']=item_keywords
         
         item_description=item_html.find("meta", {"name":"description"})['content'].replace("\n", " ").strip()
         item_data['item_description']=item_description
         
         try:
            item_label=item_html.find("span",{"class":"pdt-buy-box-condition label label-info"}).string
         except:
            item_label = None
         item_data['item_label']=item_label
                  
         item_sellerName=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1].string
         item_data['item_sellerName']=item_sellerName
         
         url=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1]['href']
         item_sellerurl='https://carousell.com'+url
         item_data['item_sellerurl']=item_sellerurl

         price=item_html.find("i",{"class":"fa fa-tag"}).parent
         item_price=re.search('-->NT\$(.*?)<!--',str(price)).group(1)
         item_data['item_price']=item_price
              
         loc=item_html.find("i",{"class":"fa fa-map-marker"}).parent.contents[1]
         item_location=re.search('>(.*?), Taiwan',str(loc)).group(1)
         item_data['item_location']=item_location
                  
         try:
            item_face_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-male"}).parent.contents[1].contents[0].string
            item_face_able=1
         except:
            item_face_able=0
         item_data['item_face_able']=item_face_able
            
         try:
            item_truck_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-truck"}).parent.contents[1].contents[0].string
            item_truck_able=1
         except:
            item_truck_able=0
         item_data['item_truck_able']=item_truck_able

         likes=item_html.find("span",{"class":"pdt-buy-box-likes-count"}).parent
         item_likes=re.search('-->(.*?)<!--',str(likes)).group(1)
         item_data['item_likes']=item_likes

         post_time=item_html.find("time",{"class":"text-muted"}).contents[1].string
         item_data['post_time']=post_time
            
         return item_data

#---玩具---

class carousellSpider15(CrawlSpider):
    name='15'
    allowed_domains = ['carousell.com']
    l=[]
    #x=requests.get('https://carousell.com/')
    #x=x.text
    #y=re.findall('<a href="(/categories/.*?/)" title=".*?" data-reactid=".*?">',x)
    #for i in y[0:3]:
    for j in range(1,350):
        l.append('https://carousell.com/categories/toys-board-games-12/?page='+str(j))

    start_urls=l

    #rules=[
    #    Rule(LinkExtractor(allow=('women-s-fashion-4')), callback='parse_list', follow=True)
    #]
    
    def parse(self, response):
        global list_page
        list_page=BeautifulSoup(response.body)
        for item in list_page.select('a.pdt-card-thumbnail'):
            item=str(item)
            item_id=re.search('href="/p/(.*?)/',item,re.S).group(1)
            yield scrapy.Request('https://carousell.com/p/'+ item_id, self.parse_detail)
       
    def parse_detail(self, response):
         
         item_data=CarousellItem()
         
         # --- 以下是商品資訊 ---
         item_data['item_category']='toys-board-games-12'
         item_html= BeautifulSoup(response.body)
         item_id=re.search('app-argument=https://carousell.com/p/(.*?)/',str(item_html),re.S).group(1)
         item_data['item_id']=item_id
         
         item_title=re.search('<title data-react-helmet="true">(.*?)</title>',str(item_html),re.S).group(1)
         item_data['item_title']=item_title
         
         item_keywords=item_html.find("meta", {"name":"keywords"})['content']
         item_data['item_keywords']=item_keywords
         
         item_description=item_html.find("meta", {"name":"description"})['content'].replace("\n", " ").strip()
         item_data['item_description']=item_description
         
         try:
            item_label=item_html.find("span",{"class":"pdt-buy-box-condition label label-info"}).string
         except:
            item_label = None
         item_data['item_label']=item_label
                  
         item_sellerName=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1].string
         item_data['item_sellerName']=item_sellerName
         
         url=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1]['href']
         item_sellerurl='https://carousell.com'+url
         item_data['item_sellerurl']=item_sellerurl

         price=item_html.find("i",{"class":"fa fa-tag"}).parent
         item_price=re.search('-->NT\$(.*?)<!--',str(price)).group(1)
         item_data['item_price']=item_price
              
         loc=item_html.find("i",{"class":"fa fa-map-marker"}).parent.contents[1]
         item_location=re.search('>(.*?), Taiwan',str(loc)).group(1)
         item_data['item_location']=item_location
                  
         try:
            item_face_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-male"}).parent.contents[1].contents[0].string
            item_face_able=1
         except:
            item_face_able=0
         item_data['item_face_able']=item_face_able
            
         try:
            item_truck_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-truck"}).parent.contents[1].contents[0].string
            item_truck_able=1
         except:
            item_truck_able=0
         item_data['item_truck_able']=item_truck_able

         likes=item_html.find("span",{"class":"pdt-buy-box-likes-count"}).parent
         item_likes=re.search('-->(.*?)<!--',str(likes)).group(1)
         item_data['item_likes']=item_likes

         post_time=item_html.find("time",{"class":"text-muted"}).contents[1].string
         item_data['post_time']=post_time
            
         return item_data

#---電玩---

class carousellSpider16(CrawlSpider):
    name='16'
    allowed_domains = ['carousell.com']
    l=[]
    #x=requests.get('https://carousell.com/')
    #x=x.text
    #y=re.findall('<a href="(/categories/.*?/)" title=".*?" data-reactid=".*?">',x)
    #for i in y[0:3]:
    for j in range(1,350):
        l.append('https://carousell.com/categories/video-gaming-1189/?page='+str(j))

    start_urls=l

    #rules=[
    #    Rule(LinkExtractor(allow=('women-s-fashion-4')), callback='parse_list', follow=True)
    #]
    
    def parse(self, response):
        global list_page
        list_page=BeautifulSoup(response.body)
        for item in list_page.select('a.pdt-card-thumbnail'):
            item=str(item)
            item_id=re.search('href="/p/(.*?)/',item,re.S).group(1)
            yield scrapy.Request('https://carousell.com/p/'+ item_id, self.parse_detail)
       
    def parse_detail(self, response):
         
         item_data=CarousellItem()
         
         # --- 以下是商品資訊 ---
         item_data['item_category']='video-gaming-1189'
         item_html= BeautifulSoup(response.body)
         item_id=re.search('app-argument=https://carousell.com/p/(.*?)/',str(item_html),re.S).group(1)
         item_data['item_id']=item_id
         
         item_title=re.search('<title data-react-helmet="true">(.*?)</title>',str(item_html),re.S).group(1)
         item_data['item_title']=item_title
         
         item_keywords=item_html.find("meta", {"name":"keywords"})['content']
         item_data['item_keywords']=item_keywords
         
         item_description=item_html.find("meta", {"name":"description"})['content'].replace("\n", " ").strip()
         item_data['item_description']=item_description
         
         try:
            item_label=item_html.find("span",{"class":"pdt-buy-box-condition label label-info"}).string
         except:
            item_label = None
         item_data['item_label']=item_label
                  
         item_sellerName=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1].string
         item_data['item_sellerName']=item_sellerName
         
         url=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1]['href']
         item_sellerurl='https://carousell.com'+url
         item_data['item_sellerurl']=item_sellerurl

         price=item_html.find("i",{"class":"fa fa-tag"}).parent
         item_price=re.search('-->NT\$(.*?)<!--',str(price)).group(1)
         item_data['item_price']=item_price
              
         loc=item_html.find("i",{"class":"fa fa-map-marker"}).parent.contents[1]
         item_location=re.search('>(.*?), Taiwan',str(loc)).group(1)
         item_data['item_location']=item_location
                  
         try:
            item_face_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-male"}).parent.contents[1].contents[0].string
            item_face_able=1
         except:
            item_face_able=0
         item_data['item_face_able']=item_face_able
            
         try:
            item_truck_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-truck"}).parent.contents[1].contents[0].string
            item_truck_able=1
         except:
            item_truck_able=0
         item_data['item_truck_able']=item_truck_able

         likes=item_html.find("span",{"class":"pdt-buy-box-likes-count"}).parent
         item_likes=re.search('-->(.*?)<!--',str(likes)).group(1)
         item_data['item_likes']=item_likes

         post_time=item_html.find("time",{"class":"text-muted"}).contents[1].string
         item_data['post_time']=post_time
            
         return item_data

#---古董收藏---

class carousellSpider17(CrawlSpider):
    name='17'
    allowed_domains = ['carousell.com']
    l=[]
    #x=requests.get('https://carousell.com/')
    #x=x.text
    #y=re.findall('<a href="(/categories/.*?/)" title=".*?" data-reactid=".*?">',x)
    #for i in y[0:3]:
    for j in range(1,350):
        l.append('https://carousell.com/categories/video-gaming-1189/?page='+str(j))

    start_urls=l

    #rules=[
    #    Rule(LinkExtractor(allow=('women-s-fashion-4')), callback='parse_list', follow=True)
    #]
    
    def parse(self, response):
        global list_page
        list_page=BeautifulSoup(response.body)
        for item in list_page.select('a.pdt-card-thumbnail'):
            item=str(item)
            item_id=re.search('href="/p/(.*?)/',item,re.S).group(1)
            yield scrapy.Request('https://carousell.com/p/'+ item_id, self.parse_detail)
       
    def parse_detail(self, response):
         
         item_data=CarousellItem()
         
         # --- 以下是商品資訊 ---
         item_data['item_category']='video-gaming-1189'
         item_html= BeautifulSoup(response.body)
         item_id=re.search('app-argument=https://carousell.com/p/(.*?)/',str(item_html),re.S).group(1)
         item_data['item_id']=item_id
         
         item_title=re.search('<title data-react-helmet="true">(.*?)</title>',str(item_html),re.S).group(1)
         item_data['item_title']=item_title
         
         item_keywords=item_html.find("meta", {"name":"keywords"})['content']
         item_data['item_keywords']=item_keywords
         
         item_description=item_html.find("meta", {"name":"description"})['content'].replace("\n", " ").strip()
         item_data['item_description']=item_description
         
         try:
            item_label=item_html.find("span",{"class":"pdt-buy-box-condition label label-info"}).string
         except:
            item_label = None
         item_data['item_label']=item_label
                  
         item_sellerName=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1].string
         item_data['item_sellerName']=item_sellerName
         
         url=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1]['href']
         item_sellerurl='https://carousell.com'+url
         item_data['item_sellerurl']=item_sellerurl

         price=item_html.find("i",{"class":"fa fa-tag"}).parent
         item_price=re.search('-->NT\$(.*?)<!--',str(price)).group(1)
         item_data['item_price']=item_price
              
         loc=item_html.find("i",{"class":"fa fa-map-marker"}).parent.contents[1]
         item_location=re.search('>(.*?), Taiwan',str(loc)).group(1)
         item_data['item_location']=item_location
                  
         try:
            item_face_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-male"}).parent.contents[1].contents[0].string
            item_face_able=1
         except:
            item_face_able=0
         item_data['item_face_able']=item_face_able
            
         try:
            item_truck_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-truck"}).parent.contents[1].contents[0].string
            item_truck_able=1
         except:
            item_truck_able=0
         item_data['item_truck_able']=item_truck_able

         likes=item_html.find("span",{"class":"pdt-buy-box-likes-count"}).parent
         item_likes=re.search('-->(.*?)<!--',str(likes)).group(1)
         item_data['item_likes']=item_likes

         post_time=item_html.find("time",{"class":"text-muted"}).contents[1].string
         item_data['post_time']=post_time
            
         return item_data
         
#---日本偶像---

class carousellSpider18(CrawlSpider):
    name='18'
    allowed_domains = ['carousell.com']
    l=[]
    #x=requests.get('https://carousell.com/')
    #x=x.text
    #y=re.findall('<a href="(/categories/.*?/)" title=".*?" data-reactid=".*?">',x)
    #for i in y[0:3]:
    for j in range(1,350):
        l.append('https://carousell.com/categories/video-gaming-1189/?page='+str(j))

    start_urls=l

    #rules=[
    #    Rule(LinkExtractor(allow=('women-s-fashion-4')), callback='parse_list', follow=True)
    #]
    
    def parse(self, response):
        global list_page
        list_page=BeautifulSoup(response.body)
        for item in list_page.select('a.pdt-card-thumbnail'):
            item=str(item)
            item_id=re.search('href="/p/(.*?)/',item,re.S).group(1)
            yield scrapy.Request('https://carousell.com/p/'+ item_id, self.parse_detail)
       
    def parse_detail(self, response):
         
         item_data=CarousellItem()
         
         # --- 以下是商品資訊 ---
         item_data['item_category']='video-gaming-1189'
         item_html= BeautifulSoup(response.body)
         item_id=re.search('app-argument=https://carousell.com/p/(.*?)/',str(item_html),re.S).group(1)
         item_data['item_id']=item_id
         
         item_title=re.search('<title data-react-helmet="true">(.*?)</title>',str(item_html),re.S).group(1)
         item_data['item_title']=item_title
         
         item_keywords=item_html.find("meta", {"name":"keywords"})['content']
         item_data['item_keywords']=item_keywords
         
         item_description=item_html.find("meta", {"name":"description"})['content'].replace("\n", " ").strip()
         item_data['item_description']=item_description
         
         try:
            item_label=item_html.find("span",{"class":"pdt-buy-box-condition label label-info"}).string
         except:
            item_label = None
         item_data['item_label']=item_label
                  
         item_sellerName=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1].string
         item_data['item_sellerName']=item_sellerName
         
         url=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1]['href']
         item_sellerurl='https://carousell.com'+url
         item_data['item_sellerurl']=item_sellerurl

         price=item_html.find("i",{"class":"fa fa-tag"}).parent
         item_price=re.search('-->NT\$(.*?)<!--',str(price)).group(1)
         item_data['item_price']=item_price
              
         loc=item_html.find("i",{"class":"fa fa-map-marker"}).parent.contents[1]
         item_location=re.search('>(.*?), Taiwan',str(loc)).group(1)
         item_data['item_location']=item_location
                  
         try:
            item_face_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-male"}).parent.contents[1].contents[0].string
            item_face_able=1
         except:
            item_face_able=0
         item_data['item_face_able']=item_face_able
            
         try:
            item_truck_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-truck"}).parent.contents[1].contents[0].string
            item_truck_able=1
         except:
            item_truck_able=0
         item_data['item_truck_able']=item_truck_able

         likes=item_html.find("span",{"class":"pdt-buy-box-likes-count"}).parent
         item_likes=re.search('-->(.*?)<!--',str(likes)).group(1)
         item_data['item_likes']=item_likes

         post_time=item_html.find("time",{"class":"text-muted"}).contents[1].string
         item_data['post_time']=post_time
            
         return item_data
         
#---韓流偶像---

class carousellSpider19(CrawlSpider):
    name='19'
    allowed_domains = ['carousell.com']
    l=[]
    #x=requests.get('https://carousell.com/')
    #x=x.text
    #y=re.findall('<a href="(/categories/.*?/)" title=".*?" data-reactid=".*?">',x)
    #for i in y[0:3]:
    for j in range(1,350):
        l.append('https://carousell.com/categories/k-wave-25/?page='+str(j))

    start_urls=l

    #rules=[
    #    Rule(LinkExtractor(allow=('women-s-fashion-4')), callback='parse_list', follow=True)
    #]
    
    def parse(self, response):
        global list_page
        list_page=BeautifulSoup(response.body)
        for item in list_page.select('a.pdt-card-thumbnail'):
            item=str(item)
            item_id=re.search('href="/p/(.*?)/',item,re.S).group(1)
            yield scrapy.Request('https://carousell.com/p/'+ item_id, self.parse_detail)
       
    def parse_detail(self, response):
         
         item_data=CarousellItem()
         
         # --- 以下是商品資訊 ---
         item_data['item_category']='k-wave-25'
         item_html= BeautifulSoup(response.body)
         item_id=re.search('app-argument=https://carousell.com/p/(.*?)/',str(item_html),re.S).group(1)
         item_data['item_id']=item_id
         
         item_title=re.search('<title data-react-helmet="true">(.*?)</title>',str(item_html),re.S).group(1)
         item_data['item_title']=item_title
         
         item_keywords=item_html.find("meta", {"name":"keywords"})['content']
         item_data['item_keywords']=item_keywords
         
         item_description=item_html.find("meta", {"name":"description"})['content'].replace("\n", " ").strip()
         item_data['item_description']=item_description
         
         try:
            item_label=item_html.find("span",{"class":"pdt-buy-box-condition label label-info"}).string
         except:
            item_label = None
         item_data['item_label']=item_label
                  
         item_sellerName=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1].string
         item_data['item_sellerName']=item_sellerName
         
         url=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1]['href']
         item_sellerurl='https://carousell.com'+url
         item_data['item_sellerurl']=item_sellerurl

         price=item_html.find("i",{"class":"fa fa-tag"}).parent
         item_price=re.search('-->NT\$(.*?)<!--',str(price)).group(1)
         item_data['item_price']=item_price
              
         loc=item_html.find("i",{"class":"fa fa-map-marker"}).parent.contents[1]
         item_location=re.search('>(.*?), Taiwan',str(loc)).group(1)
         item_data['item_location']=item_location
                  
         try:
            item_face_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-male"}).parent.contents[1].contents[0].string
            item_face_able=1
         except:
            item_face_able=0
         item_data['item_face_able']=item_face_able
            
         try:
            item_truck_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-truck"}).parent.contents[1].contents[0].string
            item_truck_able=1
         except:
            item_truck_able=0
         item_data['item_truck_able']=item_truck_able

         likes=item_html.find("span",{"class":"pdt-buy-box-likes-count"}).parent
         item_likes=re.search('-->(.*?)<!--',str(likes)).group(1)
         item_data['item_likes']=item_likes

         post_time=item_html.find("time",{"class":"text-muted"}).contents[1].string
         item_data['post_time']=post_time
            
         return item_data
         
#---票券---

class carousellSpider20(CrawlSpider):
    name='20'
    allowed_domains = ['carousell.com']
    l=[]
    #x=requests.get('https://carousell.com/')
    #x=x.text
    #y=re.findall('<a href="(/categories/.*?/)" title=".*?" data-reactid=".*?">',x)
    #for i in y[0:3]:
    for j in range(1,350):
        l.append('https://carousell.com/categories/tickets-vouchers-18/?page='+str(j))

    start_urls=l

    #rules=[
    #    Rule(LinkExtractor(allow=('women-s-fashion-4')), callback='parse_list', follow=True)
    #]
    
    def parse(self, response):
        global list_page
        list_page=BeautifulSoup(response.body)
        for item in list_page.select('a.pdt-card-thumbnail'):
            item=str(item)
            item_id=re.search('href="/p/(.*?)/',item,re.S).group(1)
            yield scrapy.Request('https://carousell.com/p/'+ item_id, self.parse_detail)
       
    def parse_detail(self, response):
         
         item_data=CarousellItem()
         
         # --- 以下是商品資訊 ---
         item_data['item_category']='tickets-vouchers-18'
         item_html= BeautifulSoup(response.body)
         item_id=re.search('app-argument=https://carousell.com/p/(.*?)/',str(item_html),re.S).group(1)
         item_data['item_id']=item_id
         
         item_title=re.search('<title data-react-helmet="true">(.*?)</title>',str(item_html),re.S).group(1)
         item_data['item_title']=item_title
         
         item_keywords=item_html.find("meta", {"name":"keywords"})['content']
         item_data['item_keywords']=item_keywords
         
         item_description=item_html.find("meta", {"name":"description"})['content'].replace("\n", " ").strip()
         item_data['item_description']=item_description
         
         try:
            item_label=item_html.find("span",{"class":"pdt-buy-box-condition label label-info"}).string
         except:
            item_label = None
         item_data['item_label']=item_label
                  
         item_sellerName=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1].string
         item_data['item_sellerName']=item_sellerName
         
         url=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1]['href']
         item_sellerurl='https://carousell.com'+url
         item_data['item_sellerurl']=item_sellerurl

         price=item_html.find("i",{"class":"fa fa-tag"}).parent
         item_price=re.search('-->NT\$(.*?)<!--',str(price)).group(1)
         item_data['item_price']=item_price
              
         loc=item_html.find("i",{"class":"fa fa-map-marker"}).parent.contents[1]
         item_location=re.search('>(.*?), Taiwan',str(loc)).group(1)
         item_data['item_location']=item_location
                  
         try:
            item_face_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-male"}).parent.contents[1].contents[0].string
            item_face_able=1
         except:
            item_face_able=0
         item_data['item_face_able']=item_face_able
            
         try:
            item_truck_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-truck"}).parent.contents[1].contents[0].string
            item_truck_able=1
         except:
            item_truck_able=0
         item_data['item_truck_able']=item_truck_able

         likes=item_html.find("span",{"class":"pdt-buy-box-likes-count"}).parent
         item_likes=re.search('-->(.*?)<!--',str(likes)).group(1)
         item_data['item_likes']=item_likes

         post_time=item_html.find("time",{"class":"text-muted"}).contents[1].string
         item_data['post_time']=post_time
            
         return item_data
         
#---預購---

class carousellSpider21(CrawlSpider):
    name='21'
    allowed_domains = ['carousell.com']
    l=[]
    #x=requests.get('https://carousell.com/')
    #x=x.text
    #y=re.findall('<a href="(/categories/.*?/)" title=".*?" data-reactid=".*?">',x)
    #for i in y[0:3]:
    for j in range(1,350):
        l.append('https://carousell.com/categories/tickets-vouchers-18/?page='+str(j))

    start_urls=l

    #rules=[
    #    Rule(LinkExtractor(allow=('women-s-fashion-4')), callback='parse_list', follow=True)
    #]
    
    def parse(self, response):
        global list_page
        list_page=BeautifulSoup(response.body)
        for item in list_page.select('a.pdt-card-thumbnail'):
            item=str(item)
            item_id=re.search('href="/p/(.*?)/',item,re.S).group(1)
            yield scrapy.Request('https://carousell.com/p/'+ item_id, self.parse_detail)
       
    def parse_detail(self, response):
         
         item_data=CarousellItem()
         
         # --- 以下是商品資訊 ---
         item_data['item_category']='tickets-vouchers-18'
         item_html= BeautifulSoup(response.body)
         item_id=re.search('app-argument=https://carousell.com/p/(.*?)/',str(item_html),re.S).group(1)
         item_data['item_id']=item_id
         
         item_title=re.search('<title data-react-helmet="true">(.*?)</title>',str(item_html),re.S).group(1)
         item_data['item_title']=item_title
         
         item_keywords=item_html.find("meta", {"name":"keywords"})['content']
         item_data['item_keywords']=item_keywords
         
         item_description=item_html.find("meta", {"name":"description"})['content'].replace("\n", " ").strip()
         item_data['item_description']=item_description
         
         try:
            item_label=item_html.find("span",{"class":"pdt-buy-box-condition label label-info"}).string
         except:
            item_label = None
         item_data['item_label']=item_label
                  
         item_sellerName=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1].string
         item_data['item_sellerName']=item_sellerName
         
         url=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1]['href']
         item_sellerurl='https://carousell.com'+url
         item_data['item_sellerurl']=item_sellerurl

         price=item_html.find("i",{"class":"fa fa-tag"}).parent
         item_price=re.search('-->NT\$(.*?)<!--',str(price)).group(1)
         item_data['item_price']=item_price
              
         loc=item_html.find("i",{"class":"fa fa-map-marker"}).parent.contents[1]
         item_location=re.search('>(.*?), Taiwan',str(loc)).group(1)
         item_data['item_location']=item_location
                  
         try:
            item_face_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-male"}).parent.contents[1].contents[0].string
            item_face_able=1
         except:
            item_face_able=0
         item_data['item_face_able']=item_face_able
            
         try:
            item_truck_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-truck"}).parent.contents[1].contents[0].string
            item_truck_able=1
         except:
            item_truck_able=0
         item_data['item_truck_able']=item_truck_able

         likes=item_html.find("span",{"class":"pdt-buy-box-likes-count"}).parent
         item_likes=re.search('-->(.*?)<!--',str(likes)).group(1)
         item_data['item_likes']=item_likes

         post_time=item_html.find("time",{"class":"text-muted"}).contents[1].string
         item_data['post_time']=post_time
            
         return item_data
         
#---教科書---

class carousellSpider22(CrawlSpider):
    name='22'
    allowed_domains = ['carousell.com']
    l=[]
    #x=requests.get('https://carousell.com/')
    #x=x.text
    #y=re.findall('<a href="(/categories/.*?/)" title=".*?" data-reactid=".*?">',x)
    #for i in y[0:3]:
    for j in range(1,350):
        l.append('https://carousell.com/categories/tickets-vouchers-18/?page='+str(j))

    start_urls=l

    #rules=[
    #    Rule(LinkExtractor(allow=('women-s-fashion-4')), callback='parse_list', follow=True)
    #]
    
    def parse(self, response):
        global list_page
        list_page=BeautifulSoup(response.body)
        for item in list_page.select('a.pdt-card-thumbnail'):
            item=str(item)
            item_id=re.search('href="/p/(.*?)/',item,re.S).group(1)
            yield scrapy.Request('https://carousell.com/p/'+ item_id, self.parse_detail)
       
    def parse_detail(self, response):
         
         item_data=CarousellItem()
         
         # --- 以下是商品資訊 ---
         item_data['item_category']='tickets-vouchers-18'
         item_html= BeautifulSoup(response.body)
         item_id=re.search('app-argument=https://carousell.com/p/(.*?)/',str(item_html),re.S).group(1)
         item_data['item_id']=item_id
         
         item_title=re.search('<title data-react-helmet="true">(.*?)</title>',str(item_html),re.S).group(1)
         item_data['item_title']=item_title
         
         item_keywords=item_html.find("meta", {"name":"keywords"})['content']
         item_data['item_keywords']=item_keywords
         
         item_description=item_html.find("meta", {"name":"description"})['content'].replace("\n", " ").strip()
         item_data['item_description']=item_description
         
         try:
            item_label=item_html.find("span",{"class":"pdt-buy-box-condition label label-info"}).string
         except:
            item_label = None
         item_data['item_label']=item_label
                  
         item_sellerName=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1].string
         item_data['item_sellerName']=item_sellerName
         
         url=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1]['href']
         item_sellerurl='https://carousell.com'+url
         item_data['item_sellerurl']=item_sellerurl

         price=item_html.find("i",{"class":"fa fa-tag"}).parent
         item_price=re.search('-->NT\$(.*?)<!--',str(price)).group(1)
         item_data['item_price']=item_price
              
         loc=item_html.find("i",{"class":"fa fa-map-marker"}).parent.contents[1]
         item_location=re.search('>(.*?), Taiwan',str(loc)).group(1)
         item_data['item_location']=item_location
                  
         try:
            item_face_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-male"}).parent.contents[1].contents[0].string
            item_face_able=1
         except:
            item_face_able=0
         item_data['item_face_able']=item_face_able
            
         try:
            item_truck_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-truck"}).parent.contents[1].contents[0].string
            item_truck_able=1
         except:
            item_truck_able=0
         item_data['item_truck_able']=item_truck_able

         likes=item_html.find("span",{"class":"pdt-buy-box-likes-count"}).parent
         item_likes=re.search('-->(.*?)<!--',str(likes)).group(1)
         item_data['item_likes']=item_likes

         post_time=item_html.find("time",{"class":"text-muted"}).contents[1].string
         item_data['post_time']=post_time
            
         return item_data
                                                                                          
#---社群活動---

class carousellSpider23(CrawlSpider):
    name='23'
    allowed_domains = ['carousell.com']
    l=[]
    #x=requests.get('https://carousell.com/')
    #x=x.text
    #y=re.findall('<a href="(/categories/.*?/)" title=".*?" data-reactid=".*?">',x)
    #for i in y[0:3]:
    for j in range(1,350):
        l.append('https://carousell.com/categories/community-26/?page='+str(j))

    start_urls=l

    #rules=[
    #    Rule(LinkExtractor(allow=('women-s-fashion-4')), callback='parse_list', follow=True)
    #]
    
    def parse(self, response):
        global list_page
        list_page=BeautifulSoup(response.body)
        for item in list_page.select('a.pdt-card-thumbnail'):
            item=str(item)
            item_id=re.search('href="/p/(.*?)/',item,re.S).group(1)
            yield scrapy.Request('https://carousell.com/p/'+ item_id, self.parse_detail)
       
    def parse_detail(self, response):
         
         item_data=CarousellItem()
         
         # --- 以下是商品資訊 ---
         item_data['item_category']='community-26'
         item_html= BeautifulSoup(response.body)
         item_id=re.search('app-argument=https://carousell.com/p/(.*?)/',str(item_html),re.S).group(1)
         item_data['item_id']=item_id
         
         item_title=re.search('<title data-react-helmet="true">(.*?)</title>',str(item_html),re.S).group(1)
         item_data['item_title']=item_title
         
         item_keywords=item_html.find("meta", {"name":"keywords"})['content']
         item_data['item_keywords']=item_keywords
         
         item_description=item_html.find("meta", {"name":"description"})['content'].replace("\n", " ").strip()
         item_data['item_description']=item_description
         
         try:
            item_label=item_html.find("span",{"class":"pdt-buy-box-condition label label-info"}).string
         except:
            item_label = None
         item_data['item_label']=item_label
                  
         item_sellerName=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1].string
         item_data['item_sellerName']=item_sellerName
         
         url=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1]['href']
         item_sellerurl='https://carousell.com'+url
         item_data['item_sellerurl']=item_sellerurl

         price=item_html.find("i",{"class":"fa fa-tag"}).parent
         item_price=re.search('-->NT\$(.*?)<!--',str(price)).group(1)
         item_data['item_price']=item_price
              
         loc=item_html.find("i",{"class":"fa fa-map-marker"}).parent.contents[1]
         item_location=re.search('>(.*?), Taiwan',str(loc)).group(1)
         item_data['item_location']=item_location
                  
         try:
            item_face_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-male"}).parent.contents[1].contents[0].string
            item_face_able=1
         except:
            item_face_able=0
         item_data['item_face_able']=item_face_able
            
         try:
            item_truck_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-truck"}).parent.contents[1].contents[0].string
            item_truck_able=1
         except:
            item_truck_able=0
         item_data['item_truck_able']=item_truck_able

         likes=item_html.find("span",{"class":"pdt-buy-box-likes-count"}).parent
         item_likes=re.search('-->(.*?)<!--',str(likes)).group(1)
         item_data['item_likes']=item_likes

         post_time=item_html.find("time",{"class":"text-muted"}).contents[1].string
         item_data['post_time']=post_time
            
         return item_data
                                                                                          
#---哩哩扣扣---

class carousellSpider24(CrawlSpider):
    name='24'
    allowed_domains = ['carousell.com']
    l=[]
    #x=requests.get('https://carousell.com/')
    #x=x.text
    #y=re.findall('<a href="(/categories/.*?/)" title=".*?" data-reactid=".*?">',x)
    #for i in y[0:3]:
    for j in range(1,350):
        l.append('https://carousell.com/categories/everything-else-16/?page='+str(j))

    start_urls=l

    #rules=[
    #    Rule(LinkExtractor(allow=('women-s-fashion-4')), callback='parse_list', follow=True)
    #]
    
    def parse(self, response):
        global list_page
        list_page=BeautifulSoup(response.body)
        for item in list_page.select('a.pdt-card-thumbnail'):
            item=str(item)
            item_id=re.search('href="/p/(.*?)/',item,re.S).group(1)
            yield scrapy.Request('https://carousell.com/p/'+ item_id, self.parse_detail)
       
    def parse_detail(self, response):
         
         item_data=CarousellItem()
         
         # --- 以下是商品資訊 ---
         item_data['item_category']='everything-else-16'
         item_html= BeautifulSoup(response.body)
         item_id=re.search('app-argument=https://carousell.com/p/(.*?)/',str(item_html),re.S).group(1)
         item_data['item_id']=item_id
         
         item_title=re.search('<title data-react-helmet="true">(.*?)</title>',str(item_html),re.S).group(1)
         item_data['item_title']=item_title
         
         item_keywords=item_html.find("meta", {"name":"keywords"})['content']
         item_data['item_keywords']=item_keywords
         
         item_description=item_html.find("meta", {"name":"description"})['content'].replace("\n", " ").strip()
         item_data['item_description']=item_description
         
         try:
            item_label=item_html.find("span",{"class":"pdt-buy-box-condition label label-info"}).string
         except:
            item_label = None
         item_data['item_label']=item_label
                  
         item_sellerName=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1].string
         item_data['item_sellerName']=item_sellerName
         
         url=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1]['href']
         item_sellerurl='https://carousell.com'+url
         item_data['item_sellerurl']=item_sellerurl

         price=item_html.find("i",{"class":"fa fa-tag"}).parent
         item_price=re.search('-->NT\$(.*?)<!--',str(price)).group(1)
         item_data['item_price']=item_price
              
         loc=item_html.find("i",{"class":"fa fa-map-marker"}).parent.contents[1]
         item_location=re.search('>(.*?), Taiwan',str(loc)).group(1)
         item_data['item_location']=item_location
                  
         try:
            item_face_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-male"}).parent.contents[1].contents[0].string
            item_face_able=1
         except:
            item_face_able=0
         item_data['item_face_able']=item_face_able
            
         try:
            item_truck_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-truck"}).parent.contents[1].contents[0].string
            item_truck_able=1
         except:
            item_truck_able=0
         item_data['item_truck_able']=item_truck_able

         likes=item_html.find("span",{"class":"pdt-buy-box-likes-count"}).parent
         item_likes=re.search('-->(.*?)<!--',str(likes)).group(1)
         item_data['item_likes']=item_likes

         post_time=item_html.find("time",{"class":"text-muted"}).contents[1].string
         item_data['post_time']=post_time
            
         return item_data

#---寵物---

class carousellSpider25(CrawlSpider):
    name='25'
    allowed_domains = ['carousell.com']
    l=[]
    #x=requests.get('https://carousell.com/')
    #x=x.text
    #y=re.findall('<a href="(/categories/.*?/)" title=".*?" data-reactid=".*?">',x)
    #for i in y[0:3]:
    for j in range(1,350):
        l.append('https://carousell.com/categories/for-pets-29/?page='+str(j))

    start_urls=l

    #rules=[
    #    Rule(LinkExtractor(allow=('women-s-fashion-4')), callback='parse_list', follow=True)
    #]
    
    def parse(self, response):
        global list_page
        list_page=BeautifulSoup(response.body)
        for item in list_page.select('a.pdt-card-thumbnail'):
            item=str(item)
            item_id=re.search('href="/p/(.*?)/',item,re.S).group(1)
            yield scrapy.Request('https://carousell.com/p/'+ item_id, self.parse_detail)
       
    def parse_detail(self, response):
         
         item_data=CarousellItem()
         
         # --- 以下是商品資訊 ---
         item_data['item_category']='for-pets-29'
         item_html= BeautifulSoup(response.body)
         item_id=re.search('app-argument=https://carousell.com/p/(.*?)/',str(item_html),re.S).group(1)
         item_data['item_id']=item_id
         
         item_title=re.search('<title data-react-helmet="true">(.*?)</title>',str(item_html),re.S).group(1)
         item_data['item_title']=item_title
         
         item_keywords=item_html.find("meta", {"name":"keywords"})['content']
         item_data['item_keywords']=item_keywords
         
         item_description=item_html.find("meta", {"name":"description"})['content'].replace("\n", " ").strip()
         item_data['item_description']=item_description
         
         try:
            item_label=item_html.find("span",{"class":"pdt-buy-box-condition label label-info"}).string
         except:
            item_label = None
         item_data['item_label']=item_label
                  
         item_sellerName=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1].string
         item_data['item_sellerName']=item_sellerName
         
         url=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1]['href']
         item_sellerurl='https://carousell.com'+url
         item_data['item_sellerurl']=item_sellerurl

         price=item_html.find("i",{"class":"fa fa-tag"}).parent
         item_price=re.search('-->NT\$(.*?)<!--',str(price)).group(1)
         item_data['item_price']=item_price
              
         loc=item_html.find("i",{"class":"fa fa-map-marker"}).parent.contents[1]
         item_location=re.search('>(.*?), Taiwan',str(loc)).group(1)
         item_data['item_location']=item_location
                  
         try:
            item_face_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-male"}).parent.contents[1].contents[0].string
            item_face_able=1
         except:
            item_face_able=0
         item_data['item_face_able']=item_face_able
            
         try:
            item_truck_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-truck"}).parent.contents[1].contents[0].string
            item_truck_able=1
         except:
            item_truck_able=0
         item_data['item_truck_able']=item_truck_able

         likes=item_html.find("span",{"class":"pdt-buy-box-likes-count"}).parent
         item_likes=re.search('-->(.*?)<!--',str(likes)).group(1)
         item_data['item_likes']=item_likes

         post_time=item_html.find("time",{"class":"text-muted"}).contents[1].string
         item_data['post_time']=post_time
            
         return item_data                                                                                          
         
#---零食物語---

class carousellSpider26(CrawlSpider):
    name='26'
    allowed_domains = ['carousell.com']
    l=[]
    #x=requests.get('https://carousell.com/')
    #x=x.text
    #y=re.findall('<a href="(/categories/.*?/)" title=".*?" data-reactid=".*?">',x)
    #for i in y[0:3]:
    for j in range(1,350):
        l.append('https://carousell.com/categories/snacks-and-preorders-103/?page='+str(j))

    start_urls=l

    #rules=[
    #    Rule(LinkExtractor(allow=('women-s-fashion-4')), callback='parse_list', follow=True)
    #]
    
    def parse(self, response):
        global list_page
        list_page=BeautifulSoup(response.body)
        for item in list_page.select('a.pdt-card-thumbnail'):
            item=str(item)
            item_id=re.search('href="/p/(.*?)/',item,re.S).group(1)
            yield scrapy.Request('https://carousell.com/p/'+ item_id, self.parse_detail)
       
    def parse_detail(self, response):
         
         item_data=CarousellItem()
         
         # --- 以下是商品資訊 ---
         item_data['item_category']='snacks-and-preorders-103'
         item_html= BeautifulSoup(response.body)
         item_id=re.search('app-argument=https://carousell.com/p/(.*?)/',str(item_html),re.S).group(1)
         item_data['item_id']=item_id
         
         item_title=re.search('<title data-react-helmet="true">(.*?)</title>',str(item_html),re.S).group(1)
         item_data['item_title']=item_title
         
         item_keywords=item_html.find("meta", {"name":"keywords"})['content']
         item_data['item_keywords']=item_keywords
         
         item_description=item_html.find("meta", {"name":"description"})['content'].replace("\n", " ").strip()
         item_data['item_description']=item_description
         
         try:
            item_label=item_html.find("span",{"class":"pdt-buy-box-condition label label-info"}).string
         except:
            item_label = None
         item_data['item_label']=item_label
                  
         item_sellerName=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1].string
         item_data['item_sellerName']=item_sellerName
         
         url=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1]['href']
         item_sellerurl='https://carousell.com'+url
         item_data['item_sellerurl']=item_sellerurl

         price=item_html.find("i",{"class":"fa fa-tag"}).parent
         item_price=re.search('-->NT\$(.*?)<!--',str(price)).group(1)
         item_data['item_price']=item_price
              
         loc=item_html.find("i",{"class":"fa fa-map-marker"}).parent.contents[1]
         item_location=re.search('>(.*?), Taiwan',str(loc)).group(1)
         item_data['item_location']=item_location
                  
         try:
            item_face_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-male"}).parent.contents[1].contents[0].string
            item_face_able=1
         except:
            item_face_able=0
         item_data['item_face_able']=item_face_able
            
         try:
            item_truck_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-truck"}).parent.contents[1].contents[0].string
            item_truck_able=1
         except:
            item_truck_able=0
         item_data['item_truck_able']=item_truck_able

         likes=item_html.find("span",{"class":"pdt-buy-box-likes-count"}).parent
         item_likes=re.search('-->(.*?)<!--',str(likes)).group(1)
         item_data['item_likes']=item_likes

         post_time=item_html.find("time",{"class":"text-muted"}).contents[1].string
         item_data['post_time']=post_time
            
         return item_data                                                                                          

#---圖書---

class carousellSpider27(CrawlSpider):
    name='27'
    allowed_domains = ['carousell.com']
    l=[]
    #x=requests.get('https://carousell.com/')
    #x=x.text
    #y=re.findall('<a href="(/categories/.*?/)" title=".*?" data-reactid=".*?">',x)
    #for i in y[0:3]:
    for j in range(1,350):
        l.append('https://carousell.com/categories/books-stationery-5/?page='+str(j))

    start_urls=l

    #rules=[
    #    Rule(LinkExtractor(allow=('women-s-fashion-4')), callback='parse_list', follow=True)
    #]
    
    def parse(self, response):
        global list_page
        list_page=BeautifulSoup(response.body)
        for item in list_page.select('a.pdt-card-thumbnail'):
            item=str(item)
            item_id=re.search('href="/p/(.*?)/',item,re.S).group(1)
            yield scrapy.Request('https://carousell.com/p/'+ item_id, self.parse_detail)
       
    def parse_detail(self, response):
         
         item_data=CarousellItem()
         
         # --- 以下是商品資訊 ---
         item_data['item_category']='books-stationery-5'
         item_html= BeautifulSoup(response.body)
         item_id=re.search('app-argument=https://carousell.com/p/(.*?)/',str(item_html),re.S).group(1)
         item_data['item_id']=item_id
         
         item_title=re.search('<title data-react-helmet="true">(.*?)</title>',str(item_html),re.S).group(1)
         item_data['item_title']=item_title
         
         item_keywords=item_html.find("meta", {"name":"keywords"})['content']
         item_data['item_keywords']=item_keywords
         
         item_description=item_html.find("meta", {"name":"description"})['content'].replace("\n", " ").strip()
         item_data['item_description']=item_description
         
         try:
            item_label=item_html.find("span",{"class":"pdt-buy-box-condition label label-info"}).string
         except:
            item_label = None
         item_data['item_label']=item_label
                  
         item_sellerName=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1].string
         item_data['item_sellerName']=item_sellerName
         
         url=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1]['href']
         item_sellerurl='https://carousell.com'+url
         item_data['item_sellerurl']=item_sellerurl

         price=item_html.find("i",{"class":"fa fa-tag"}).parent
         item_price=re.search('-->NT\$(.*?)<!--',str(price)).group(1)
         item_data['item_price']=item_price
              
         loc=item_html.find("i",{"class":"fa fa-map-marker"}).parent.contents[1]
         item_location=re.search('>(.*?), Taiwan',str(loc)).group(1)
         item_data['item_location']=item_location
                  
         try:
            item_face_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-male"}).parent.contents[1].contents[0].string
            item_face_able=1
         except:
            item_face_able=0
         item_data['item_face_able']=item_face_able
            
         try:
            item_truck_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-truck"}).parent.contents[1].contents[0].string
            item_truck_able=1
         except:
            item_truck_able=0
         item_data['item_truck_able']=item_truck_able

         likes=item_html.find("span",{"class":"pdt-buy-box-likes-count"}).parent
         item_likes=re.search('-->(.*?)<!--',str(likes)).group(1)
         item_data['item_likes']=item_likes

         post_time=item_html.find("time",{"class":"text-muted"}).contents[1].string
         item_data['post_time']=post_time
            
         return item_data                                                                                          

#---機車---

class carousellSpider28(CrawlSpider):
    name='28'
    allowed_domains = ['carousell.com']
    l=[]
    #x=requests.get('https://carousell.com/')
    #x=x.text
    #y=re.findall('<a href="(/categories/.*?/)" title=".*?" data-reactid=".*?">',x)
    #for i in y[0:3]:
    for j in range(1,350):
        l.append('https://carousell.com/categories/motorbikes-108/?page='+str(j))

    start_urls=l

    #rules=[
    #    Rule(LinkExtractor(allow=('women-s-fashion-4')), callback='parse_list', follow=True)
    #]
    
    def parse(self, response):
        global list_page
        list_page=BeautifulSoup(response.body)
        for item in list_page.select('a.pdt-card-thumbnail'):
            item=str(item)
            item_id=re.search('href="/p/(.*?)/',item,re.S).group(1)
            yield scrapy.Request('https://carousell.com/p/'+ item_id, self.parse_detail)
       
    def parse_detail(self, response):
         
         item_data=CarousellItem()
         
         # --- 以下是商品資訊 ---
         item_data['item_category']='motorbikes-108'
         item_html= BeautifulSoup(response.body)
         item_id=re.search('app-argument=https://carousell.com/p/(.*?)/',str(item_html),re.S).group(1)
         item_data['item_id']=item_id
         
         item_title=re.search('<title data-react-helmet="true">(.*?)</title>',str(item_html),re.S).group(1)
         item_data['item_title']=item_title
         
         item_keywords=item_html.find("meta", {"name":"keywords"})['content']
         item_data['item_keywords']=item_keywords
         
         item_description=item_html.find("meta", {"name":"description"})['content'].replace("\n", " ").strip()
         item_data['item_description']=item_description
         
         try:
            item_label=item_html.find("span",{"class":"pdt-buy-box-condition label label-info"}).string
         except:
            item_label = None
         item_data['item_label']=item_label
                  
         item_sellerName=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1].string
         item_data['item_sellerName']=item_sellerName
         
         url=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1]['href']
         item_sellerurl='https://carousell.com'+url
         item_data['item_sellerurl']=item_sellerurl

         price=item_html.find("i",{"class":"fa fa-tag"}).parent
         item_price=re.search('-->NT\$(.*?)<!--',str(price)).group(1)
         item_data['item_price']=item_price
              
         loc=item_html.find("i",{"class":"fa fa-map-marker"}).parent.contents[1]
         item_location=re.search('>(.*?), Taiwan',str(loc)).group(1)
         item_data['item_location']=item_location
                  
         try:
            item_face_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-male"}).parent.contents[1].contents[0].string
            item_face_able=1
         except:
            item_face_able=0
         item_data['item_face_able']=item_face_able
            
         try:
            item_truck_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-truck"}).parent.contents[1].contents[0].string
            item_truck_able=1
         except:
            item_truck_able=0
         item_data['item_truck_able']=item_truck_able

         likes=item_html.find("span",{"class":"pdt-buy-box-likes-count"}).parent
         item_likes=re.search('-->(.*?)<!--',str(likes)).group(1)
         item_data['item_likes']=item_likes

         post_time=item_html.find("time",{"class":"text-muted"}).contents[1].string
         item_data['post_time']=post_time
            
         return item_data                                                                                          

#---汽機車零配件---

class carousellSpider29(CrawlSpider):
    name='29'
    allowed_domains = ['carousell.com']
    l=[]
    #x=requests.get('https://carousell.com/')
    #x=x.text
    #y=re.findall('<a href="(/categories/.*?/)" title=".*?" data-reactid=".*?">',x)
    #for i in y[0:3]:
    for j in range(1,350):
        l.append('https://carousell.com/categories/auto-accessories-others-109/?page='+str(j))

    start_urls=l

    #rules=[
    #    Rule(LinkExtractor(allow=('women-s-fashion-4')), callback='parse_list', follow=True)
    #]
    
    def parse(self, response):
        global list_page
        list_page=BeautifulSoup(response.body)
        for item in list_page.select('a.pdt-card-thumbnail'):
            item=str(item)
            item_id=re.search('href="/p/(.*?)/',item,re.S).group(1)
            yield scrapy.Request('https://carousell.com/p/'+ item_id, self.parse_detail)
       
    def parse_detail(self, response):
         
         item_data=CarousellItem()
         
         # --- 以下是商品資訊 ---
         item_data['item_category']='auto-accessories-others-109'
         item_html= BeautifulSoup(response.body)
         item_id=re.search('app-argument=https://carousell.com/p/(.*?)/',str(item_html),re.S).group(1)
         item_data['item_id']=item_id
         
         item_title=re.search('<title data-react-helmet="true">(.*?)</title>',str(item_html),re.S).group(1)
         item_data['item_title']=item_title
         
         item_keywords=item_html.find("meta", {"name":"keywords"})['content']
         item_data['item_keywords']=item_keywords
         
         item_description=item_html.find("meta", {"name":"description"})['content'].replace("\n", " ").strip()
         item_data['item_description']=item_description
         
         try:
            item_label=item_html.find("span",{"class":"pdt-buy-box-condition label label-info"}).string
         except:
            item_label = None
         item_data['item_label']=item_label
                  
         item_sellerName=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1].string
         item_data['item_sellerName']=item_sellerName
         
         url=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1]['href']
         item_sellerurl='https://carousell.com'+url
         item_data['item_sellerurl']=item_sellerurl

         price=item_html.find("i",{"class":"fa fa-tag"}).parent
         item_price=re.search('-->NT\$(.*?)<!--',str(price)).group(1)
         item_data['item_price']=item_price
              
         loc=item_html.find("i",{"class":"fa fa-map-marker"}).parent.contents[1]
         item_location=re.search('>(.*?), Taiwan',str(loc)).group(1)
         item_data['item_location']=item_location
                  
         try:
            item_face_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-male"}).parent.contents[1].contents[0].string
            item_face_able=1
         except:
            item_face_able=0
         item_data['item_face_able']=item_face_able
            
         try:
            item_truck_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-truck"}).parent.contents[1].contents[0].string
            item_truck_able=1
         except:
            item_truck_able=0
         item_data['item_truck_able']=item_truck_able

         likes=item_html.find("span",{"class":"pdt-buy-box-likes-count"}).parent
         item_likes=re.search('-->(.*?)<!--',str(likes)).group(1)
         item_data['item_likes']=item_likes

         post_time=item_html.find("time",{"class":"text-muted"}).contents[1].string
         item_data['post_time']=post_time
            
         return item_data                                                                                          
         
#---徵收好物---

class carousellSpider30(CrawlSpider):
    name='30'
    allowed_domains = ['carousell.com']
    l=[]
    #x=requests.get('https://carousell.com/')
    #x=x.text
    #y=re.findall('<a href="(/categories/.*?/)" title=".*?" data-reactid=".*?">',x)
    #for i in y[0:3]:
    for j in range(1,350):
        l.append('https://carousell.com/categories/looking-for-21/?page='+str(j))

    start_urls=l

    #rules=[
    #    Rule(LinkExtractor(allow=('women-s-fashion-4')), callback='parse_list', follow=True)
    #]
    
    def parse(self, response):
        global list_page
        list_page=BeautifulSoup(response.body)
        for item in list_page.select('a.pdt-card-thumbnail'):
            item=str(item)
            item_id=re.search('href="/p/(.*?)/',item,re.S).group(1)
            yield scrapy.Request('https://carousell.com/p/'+ item_id, self.parse_detail)
       
    def parse_detail(self, response):
         
         item_data=CarousellItem()
         
         # --- 以下是商品資訊 ---
         item_data['item_category']='looking-for-21'
         item_html= BeautifulSoup(response.body)
         item_id=re.search('app-argument=https://carousell.com/p/(.*?)/',str(item_html),re.S).group(1)
         item_data['item_id']=item_id
         
         item_title=re.search('<title data-react-helmet="true">(.*?)</title>',str(item_html),re.S).group(1)
         item_data['item_title']=item_title
         
         item_keywords=item_html.find("meta", {"name":"keywords"})['content']
         item_data['item_keywords']=item_keywords
         
         item_description=item_html.find("meta", {"name":"description"})['content'].replace("\n", " ").strip()
         item_data['item_description']=item_description
         
         try:
            item_label=item_html.find("span",{"class":"pdt-buy-box-condition label label-info"}).string
         except:
            item_label = None
         item_data['item_label']=item_label
                  
         item_sellerName=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1].string
         item_data['item_sellerName']=item_sellerName
         
         url=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1]['href']
         item_sellerurl='https://carousell.com'+url
         item_data['item_sellerurl']=item_sellerurl

         price=item_html.find("i",{"class":"fa fa-tag"}).parent
         item_price=re.search('-->NT\$(.*?)<!--',str(price)).group(1)
         item_data['item_price']=item_price
              
         loc=item_html.find("i",{"class":"fa fa-map-marker"}).parent.contents[1]
         item_location=re.search('>(.*?), Taiwan',str(loc)).group(1)
         item_data['item_location']=item_location
                  
         try:
            item_face_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-male"}).parent.contents[1].contents[0].string
            item_face_able=1
         except:
            item_face_able=0
         item_data['item_face_able']=item_face_able
            
         try:
            item_truck_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-truck"}).parent.contents[1].contents[0].string
            item_truck_able=1
         except:
            item_truck_able=0
         item_data['item_truck_able']=item_truck_able

         likes=item_html.find("span",{"class":"pdt-buy-box-likes-count"}).parent
         item_likes=re.search('-->(.*?)<!--',str(likes)).group(1)
         item_data['item_likes']=item_likes

         post_time=item_html.find("time",{"class":"text-muted"}).contents[1].string
         item_data['post_time']=post_time
            
         return item_data                                                                                          
         
#---汽車---

class carousellSpider31(CrawlSpider):
    name='31'
    allowed_domains = ['carousell.com']
    l=[]
    #x=requests.get('https://carousell.com/')
    #x=x.text
    #y=re.findall('<a href="(/categories/.*?/)" title=".*?" data-reactid=".*?">',x)
    #for i in y[0:3]:
    for j in range(1,350):
        l.append('https://carousell.com/categories/cars-32/?page='+str(j))

    start_urls=l

    #rules=[
    #    Rule(LinkExtractor(allow=('women-s-fashion-4')), callback='parse_list', follow=True)
    #]
    
    def parse(self, response):
        global list_page
        list_page=BeautifulSoup(response.body)
        for item in list_page.select('a.pdt-card-thumbnail'):
            item=str(item)
            item_id=re.search('href="/p/(.*?)/',item,re.S).group(1)
            yield scrapy.Request('https://carousell.com/p/'+ item_id, self.parse_detail)
       
    def parse_detail(self, response):
         
         item_data=CarousellItem()
         
         # --- 以下是商品資訊 ---
         item_data['item_category']='cars-32'
         item_html= BeautifulSoup(response.body)
         item_id=re.search('app-argument=https://carousell.com/p/(.*?)/',str(item_html),re.S).group(1)
         item_data['item_id']=item_id
         
         item_title=re.search('<title data-react-helmet="true">(.*?)</title>',str(item_html),re.S).group(1)
         item_data['item_title']=item_title
         
         item_keywords=item_html.find("meta", {"name":"keywords"})['content']
         item_data['item_keywords']=item_keywords
         
         item_description=item_html.find("meta", {"name":"description"})['content'].replace("\n", " ").strip()
         item_data['item_description']=item_description
         
         try:
            item_label=item_html.find("span",{"class":"pdt-buy-box-condition label label-info"}).string
         except:
            item_label = None
         item_data['item_label']=item_label
                  
         item_sellerName=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1].string
         item_data['item_sellerName']=item_sellerName
         
         url=item_html.find("p",{"class":"pdt-buy-box-attributes"}).contents[1]['href']
         item_sellerurl='https://carousell.com'+url
         item_data['item_sellerurl']=item_sellerurl

         price=item_html.find("i",{"class":"fa fa-tag"}).parent
         item_price=re.search('-->NT\$(.*?)<!--',str(price)).group(1)
         item_data['item_price']=item_price
              
         loc=item_html.find("i",{"class":"fa fa-map-marker"}).parent.contents[1]
         item_location=re.search('>(.*?), Taiwan',str(loc)).group(1)
         item_data['item_location']=item_location
                  
         try:
            item_face_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-male"}).parent.contents[1].contents[0].string
            item_face_able=1
         except:
            item_face_able=0
         item_data['item_face_able']=item_face_able
            
         try:
            item_truck_able=item_html.find("i",{"class":"pdt-buy-box-delivery-option-link-icon fa fa-truck"}).parent.contents[1].contents[0].string
            item_truck_able=1
         except:
            item_truck_able=0
         item_data['item_truck_able']=item_truck_able

         likes=item_html.find("span",{"class":"pdt-buy-box-likes-count"}).parent
         item_likes=re.search('-->(.*?)<!--',str(likes)).group(1)
         item_data['item_likes']=item_likes

         post_time=item_html.find("time",{"class":"text-muted"}).contents[1].string
         item_data['post_time']=post_time
            
         return item_data                                                                                          
         