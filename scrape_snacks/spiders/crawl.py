# -*- coding: utf-8 -*-
import scrapy
# from scrapy import Item, Field
from pymongo import MongoClient
from items import ScrapeSnacksItem
from datetime import datetime
import re

months = 'january febuary march april may june july august september october november december'.split()

class CrawlSpider(scrapy.Spider):
    name = "crawl"
    allowed_domains = ["snackdata.com"]
    start_urls = (
        'http://www.snackdata.com/',
    )

    def parse(self, response):
        links = response.css('ol li a::attr(href)').extract()

        for link in links:
            yield scrapy.Request(response.urljoin(link), self.parse_fruits)

    def parse_fruits(self, response):
        data = response.css('#middlestuff')
        item = ScrapeSnacksItem()
        item['number'] = data.css('.header em::text')[0].extract()
        item['flavor'] = data.css('dl dd:nth-of-type(1) a::text').extract()
        item['cuisine'] = data.css('dl dd:nth-of-type(2) a::text').extract()
        item['series'] = data.css('dl dd:nth-of-type(3) a::text').extract()
        item['composition'] = data.css('dl dd:nth-of-type(4) a img::attr(alt)').extract()

        item['name'] = response.css('#rightstuff h1::text')[0].extract()
        dt = re.sub('[\s.]+', ' ', '.'.join(response.css('#rightstuff::text').extract())).strip().split()[-3:]
        try:
            month = int(months.index(dt[0]) + 1)
            day   = int(re.sub('\w*', '', dt[1]))
            year  = int(dt[2])
            item['start_date'] = datetime(year, month, day) 
        except:
            pass
        item['description'] = ''
        item['taste'] = ''

        yield item
