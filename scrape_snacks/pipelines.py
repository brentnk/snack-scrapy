# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient


class ScrapeSnacksPipeline(object):
    def __init__(self, mongo_host, mongo_port, mongo_db, mongo_collection):
        connection = MongoClient(mongo_host, mongo_port)
        db = connection[mongo_db]
        db.drop_collection(mongo_collection)
        self.collection = db[mongo_collection]

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
                mongo_host = crawler.settings.get('MONGO_HOST', '127.0.0.1'),
                mongo_port = crawler.settings.getint('MONGO_PORT', 27017),
                mongo_db  = crawler.settings.get('MONGO_DB', 'snacker'),
                mongo_collection = crawler.settings.get('MONGO_COLLECTION', 'snacks')
                )


    def process_item(self, item, spider):
        self.collection.insert(dict(item))

        return item
