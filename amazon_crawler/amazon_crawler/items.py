# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

# https://www.amazon.com/Samsung-UN40H5003-40-Inch-Measured-Diagonally/product-reviews/B00MYBR75O

import scrapy

from scrapy_djangoitem import DjangoItem
from crawler.models import Reviews

class AmazonCrawlerItem(DjangoItem):
    # define the fields for your item here like:
    # name = scrapy.Field() 
    django_model = Reviews   
    
