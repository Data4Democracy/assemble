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
    time_rem = scrapy.Field()

    # List of Actual Contributions
    contributions = scrapy.Field()

    # About - Text Fields, may contain links
    goal = scrapy.Field()
    why = scrapy.Field()
    requirements = scrapy.Field()

    # List of Updates
    updates = scrapy.Field()

    # List of Links within About Fields,
    # Updates, and Contribution Comments
    content_links = scrapy.Field()
