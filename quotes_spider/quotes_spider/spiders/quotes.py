# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request

class QuotesSpider(Spider):
	name = "quotes"
	allowed_domains = ["quotes.toscrape.com"]
	start_urls = ['http://quotes.toscrape.com/']

	def parse(self, response):
		# h1_tag = response.xpath('//h1/a/text()').extract_first()
		# print(h1_tag)
		# tags = response.xpath('//*[@class="tag-item"]/a/text()').extract()
		# print(tags)

		quotes = response.xpath('//*[@class="quote"]')
		for quote in quotes:
			text = quote.xpath('.//*[@class="text"]/text()').extract_first()
			author = quote.xpath('.//*[@class="author"]/text()').extract_first()
			tags = quote.xpath('.//*[@class="tag"]/text()').extract()
			
			yield {
				'Text' : text,
				'Author' : author,
				'Tags' : tags
			}
		next_page = response.xpath('//*[@class="next"]/a/@href').extract_first()
		absolute_next_page = response.urljoin(next_page)
		yield Request(absolute_next_page)