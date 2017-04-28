# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["http://quotes.toscrape.com/"]
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        h1_tag = response.xpath('//h1/a/text()').extract_first()
        print(h1_tag)
        tags = response.xpath('//*[@class="tag-item"]/a/text()').extract()
        print(tags)
