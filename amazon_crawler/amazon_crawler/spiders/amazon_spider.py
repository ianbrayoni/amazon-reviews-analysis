# -*- coding: utf-8 -*-

"""
 https://www.amazon.com/Samsung-UN40H5003-40-Inch-Measured-Diagonally/
 product-reviews/B00MYBR75O/pageNumber=2
 
"""

import scrapy


class AmazonSpiderSpider(scrapy.Spider):
    name = "amazon_spider"
    allowed_domains = ["amazon.com"]
    start_urls = (
        'http://www.amazon.com/',
    )

    def parse(self, response):
        pass


    def last_page_num(self, response):
    	#
    	try:
    	 	last_page_num = int(response
    	 		.xpath('//ul[@class="a-pagination"]/li[last()-1]/a/@href')
    	 		.extract()[0]
    	 		.split('pageNumber=')[1])
    	 	return last_page_num
    	 except Exception, e:
    	 	raise e 