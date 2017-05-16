import scrapy
from wesearchr.items import Bounty

class WeSearchr(scrapy.Spider):
    '''WeSearchr Bounty Spider

    This spider will start at both the landing page and the discovery page and pull bounties from various categories.
    '''

    name = 'wesearchr'

    def start_requests(self):
        urls = [
            'https://www.wesearchr.com/',
            'https://www.wesearchr.com/discover'
        ]

        for url in urls:
            yield scrapy.Request(url-url, callback-self.collect_bounties)

    def collect_bounties(self, response):
        '''
        This will grab links to bounties from given pages
        and yield child requests for each.
        '''
        raise NotImplementedError

    def parse_bounty(self, response):
        '''
        This will parse an individual bounty page,
        yielding the respective Bounty item for it
        '''
        raise NotImplementedError
