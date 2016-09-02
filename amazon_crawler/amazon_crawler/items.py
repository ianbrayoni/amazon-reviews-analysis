# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy_djangoitem import DjangoItem
from crawler.models import Reviews

class AmazonCrawlerItem(DjangoItem):
	django_model = Reviews   
    
