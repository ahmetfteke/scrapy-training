# -*- coding: utf-8 -*-
from scrapy import Spider
# from scrapy.http import Request
from scrapy.http import FormRequest
from scrapy.loader import ItemLoader
from scrapy.utils.response import open_in_browser

from quotes_spider.items import QuotesSpiderItem

class QuotesSpider(Spider):
	name = "quotes"
	# allowed_domains = ["quotes.toscrape.com"]
	# start_urls = ['http://quotes.toscrape.com/']
	start_urls = ['http://quotes.toscrape.com/login']

	def scrape_home_page(self, response):
		open_in_browser(response)
		l = ItemLoader(item=QuotesSpiderItem(), response=response)
		h1_tag = response.xpath("//h1/a/text()").extract_first()
		tags = response.xpath("//*[@class='tag-item']/a/text()").extract()

		l.add_value('h1_tag', h1_tag)
		l.add_value('tags', tags)

		return l.load_item()

	def parse(self, response):
		token = response.xpath('//*[@name="csrf_token"]/@value').extract_first()
		return FormRequest.from_response(response,
										formdata={'csrf_token': token,
												  'password' : 'foo',
												  'username' : 'foo'},
										callback=self.scrape_home_page)

		# h1_tag = response.xpath('//h1/a/text()').extract_first()
		# print(h1_tag)
		# tags = response.xpath('//*[@class="tag-item"]/a/text()').extract()
		# print(tags)


		## her sayfayi scrape etme
		# quotes = response.xpath('//*[@class="quote"]')
		# for quote in quotes:
		# 	text = quote.xpath('.//*[@class="text"]/text()').extract_first()
		# 	author = quote.xpath('.//*[@class="author"]/text()').extract_first()
		# 	tags = quote.xpath('.//*[@class="tag"]/text()').extract()
			
		# 	yield {
		# 		'Text' : text,
		# 		'Author' : author,
		# 		'Tags' : tags
		# 	}
		# next_page = response.xpath('//*[@class="next"]/a/@href').extract_first()
		# absolute_next_page = response.urljoin(next_page)
		# yield Request(absolute_next_page)

		## login
