import scrapy
from congress.items import Record


class Congress(scrapy.Spider):
    # TODO: Docstring

    # spider name should be name of website/source
    name = 'congress'

    def start_requests(self):
        # list of URL(s) to start crawl
        urls = [
            'https://www.congress.gov/congressional-record/browse-by-date/'
            ]

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
        date = response.xpath('//div[@class="cr-issue"]/h3/text()').extract_first()
        #Processing steps needed: Proper datetime formatting

        # TODO Title
        title = response.xpath('//div[@class="wrapper_std"]/h2/text()').extract()

        # TODO url (current url)
        url = response.xpath('//link[contains(@href,"congressional-record/2017")]/@href').extract_first()
	
        # TODO category: (daily digest, senate, house, extensions)
        raw_category = response.xpath('//span[@class="quiet"]/text()').extract_first()
        raw_category_rmdate = raw_category.split('-')[0]
        raw_category_rmpar = raw_category_rmdate.split('(')[1]
        category = raw_category_rmpar.strip()

        # TODO hrefs: any references in text (EX: pages numbers)
        hrefs = None

        # TODO text_blob: (what was actually said)
        text_blob = response.xpath('//pre[@class="styled"]/text()').extract()
        #Processing steps needed: Remove trailing spaces and line breaks

        # TODO parse this "115th Congress, 1st Session<br />Issue: Vol. 163, No. 17"
        doc_info = response.xpath('//div[@class="cr-issue"]/h4/text()').extract()
        congress_session = doc_info[0].split(',')
		congress = congress_session[0]
		session = congress_session[1]
		vol_no = doc_info[1].split(',')
		vol = vol_no[0].split(':')[1]
		no = vol_no[1]
        '''
        # Congress
        # Session
        # Issue -- is comprised of Volume and Number
        # Volume
        # Number
        '''
        doc_info = dict {
             'congress': congress,
             'session': session,
             'Volume': vol,
             'Number': no
         }

        item = Record{

            'date' = date
            'title' = title
            'url' = url
            'category' = category
            'text'= text_blob
            'doc_info'= doc_info
            
        }

        yield item
