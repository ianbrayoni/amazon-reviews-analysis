# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem
from review_analysis.apps.crawler.models import Review


class AmazonCrawlerItem(DjangoItem):
    django_model = Review
