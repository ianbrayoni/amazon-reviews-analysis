# -*- coding: utf-8 -*-

import scrapy
import re
from amazon_crawler.items import AmazonCrawlerItem


class AmazonSpiderSpider(scrapy.Spider):
    """ spider to crawl product reviews from amazon.com"""
    name = "amazon_spider"
    
    def __init__(self, *args, **kwargs): 
        super(AmazonSpiderSpider, self).__init__(*args, **kwargs) 

        self.start_urls = [kwargs.get('start_url')] 

    def parse(self, response):
        yield scrapy.Request(self.start_urls[0], callback=self.parse_reviews)
           

    def parse_reviews(self, response):
        # retrieve reviews
        try:            
            reviews = response.css('.review-text').xpath('string()').extract()
            
            for review in reviews:
                item = AmazonCrawlerItem()
                item['asin'] = ((self.start_urls[0]).split('product-reviews')[1]).strip('/')
                item['review_text'] = review 
                yield item            

            nextPage = response.css("ul.a-pagination >li.a-last > a::attr('href')")

            if nextPage:
                url = response.urljoin(nextPage[0].extract())
                yield scrapy.Request(url, self.parse_reviews)

        except Exception, e:
            raise e
        