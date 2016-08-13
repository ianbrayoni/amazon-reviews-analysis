# -*- coding: utf-8 -*-

"""
 https://www.amazon.com/Samsung-UN40H5003-40-Inch-Measured-Diagonally/
 product-reviews/B00MYBR75O/pageNumber=2

"""

import scrapy
from amazon_crawler.items import AmazonCrawlerItem


class AmazonSpiderSpider(scrapy.Spider):
    name = "amazon_spider"
    allowed_domains = ["amazon.com"]
    start_urls = (
        'https://www.amazon.com/',
        'https://www.amazon.com/Sony-KDL40R510C-40-Inch-1080p-Smart/product-reviews/B00V0K0Y00'
    )

    def parse(self, response):
        # get the last page number on the page
        page_num = self.last_page_numerical(response)

        if page_num < 1:
            # abort the search if there are no results
            return
        else:
            url = 'https://www.amazon.com/Sony-KDL40R510C-40-Inch-1080p-Smart/product-reviews/B00V0K0Y00'
            yield scrapy.Request(url, callback=self.parse_reviews)
           

    def last_page_numerical(self, response):
    	# retrieve last page number from the pagination
    	try:
    	 	last_page_num = int(response
    	 		.xpath('//ul[@class="a-pagination"]/li[last()-1]/a/@href')
    	 		.extract()[0]
    	 		.split('pageNumber=')[1])
    	 	return last_page_num
    	except Exception, e:
    	 	raise e 

    def parse_reviews(self, response):
        # retrieve reviews
        try:
            item = AmazonCrawlerItem()
            reviews = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "review-text", " " ))]/text()').extract()
            
            for review in reviews:
                item['review_text'] = review
                yield item

            nextPage = response.css("ul.a-pagination >li.a-last > a::attr('href')")

            if nextPage:
                url = response.urljoin(nextPage[0].extract())
                yield scrapy.Request(url, self.parse_reviews)

        except Exception, e:
            raise e
        