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
        # get the last page number on the page
        last_page_num = self.last_page_numerical(response)

        if last_page_num < 1:
            # abort the search if there are no results
            return
        else:
            # otherwise loop over all pages and scrape
            page_urls = [response.url + "pageNumber=" + str(pageNumber)
            for pageNumber in xrange(1,last_page_num + 1)]

            for page_url in page_urls:
                yield scrapy.Request(page_url, callback=self.parse_reviews)

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
        pass