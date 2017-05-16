# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Bounty(scrapy.Item):
    """
    Scraped WeSearchr Bounty
    """
    # General
    url = scrapy.Field()
    title = scrapy.Field()

    # Contributions
    min_bounty = scrapy.Field()
    cur_bounty = scrapy.Field()
    num_contrib = scrapy.Field()
    time_rem = scrapy.Field()

    # About
    goal = scrapy.Field()
    why = scrapy.Field()
    requirements = scrapy.Field()

    # Lists
    updates = scrapy.Field()
    contributions = scrapy.Field()
    content_links = scrapy.Field()
