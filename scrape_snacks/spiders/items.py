# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy import Item, Field

class ScrapeSnacksItem(Item):
    name = Field()
    number = Field()
    flavor = Field()
    cuisine = Field()
    series = Field()
    composition = Field()
    start_date = Field()
    description = Field()
    taste = Field()
