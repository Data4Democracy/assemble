# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


import scrapy

class Article(scrapy.Item):
    """
    Scraped news article
    """
    # Required
    language = scrapy.Field()
    url = scrapy.Field()
    text_blob = scrapy.Field()
    source = scrapy.Field()

    # Optional
    authors = scrapy.Field()
    pub_date = scrapy.Field()
    pub_time = scrapy.Field()
    title = scrapy.Field()
    lead = scrapy.Field()
    hrefs = scrapy.Field()
    meta = scrapy.Field()
    num_shares = scrapy.Field()
    num_comments = scrapy.Field()
    comment_hrefs = scrapy.Field()


class Record(scrapy.Item):
    date = scrapy.Field()
    category = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    text_blob = scrapy.Field()
    hrefs = scrapy.Field()
    meta = scrapy.Field()

