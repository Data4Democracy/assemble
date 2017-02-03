from congress.items import record


class Congress(scrapy.Spider):
    # TODO: Docstring

    # spider name should be name of website/source
    name = 'congress'

    def start_requests(self):
        # list of URL(s) to start crawl
        urls = [
            'https://www.congress.gov/congressional-record/browse-by-date/'

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_date_summary_page)

    def parse_date_summary_page(self, response):
        '''
        This function will collect all links found in digest/senate/house/extensions
        Ex : https://www.congress.gov/congressional-record/2017/02/01/senate-section
        the first link would find "Senate" then "Prayer" etc.
        '''

        # TODO for each category --
            # approach 1 follow first link and keep clicking "next" until done
            # approach 2 get all links and submit each link to be parsed.
                # EX for link in links call parse_congressional_record()

    def parse_congressional_record(self, response):
        '''
        Process a congressional record
        ex: https://www.congress.gov/congressional-record/2017/2/1/senate-section/article/S541-2
        '''

        # TODO date (congressional date of record) (YYYY-MM-DD format)
        date = None

        # TODO Title
        title = None

        # TODO url (current url)
        url = None

        # TODO category: (daily digest, senate, house, extensions)
        category = None

        # TODO hrefs: any references in text (EX: pages numbers)
        hrefs = None

        # TODO text_blob: (what was actually said)
        text_blob = None

        # TODO parse this "115th Congress, 1st Session<br />Issue: Vol. 163, No. 17"
            '''
            # Congress
            # Session
            # Issue
            # Volume
            # Number
            '''
        # TODO needs better name
        meta = dict {
            'congress': None,
            'session': None,
            'Issue': None,
            'Volume': None,
            'Number': None
        }

        item = Record(
            #TODO build item
            # date = date
            # url = url
            # etc. etc.
        )

        yield item
