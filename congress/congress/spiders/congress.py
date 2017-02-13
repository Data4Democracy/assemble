import scrapy
from congress.items import Record
from datetime import datetime


class Congress(scrapy.Spider):
    '''Congressional record spider

    This spider will start at the congressional record website and pull the most recent
    daily record for Senate, House and Extension of Remarks.

    Currently it does not parse historic dates.

    Example Command: scrapy crawl congress -o <outputfile.json> --logfile <logfile.txt>
    '''

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
        This function will collect all links found in senate/house/extensions
        Ex : https://www.congress.gov/congressional-record/2017/02/01/senate-section
        the first link would find "Senate" then "Prayer" etc.
        '''

        tables = response.selector.xpath('//table')
        hrefs = tables.select('//a[contains(@href,"congressional-record/2017")]/@href').extract()[1:4]
        for href in hrefs:
            yield scrapy.Request(url='https://www.congress.gov/{}/'.format(href),
                                 callback=self.collect_links)

    def collect_links(self, response):
        '''Get links to each entry in the record and pass them to be parsed'''

        rows = response.xpath('//tr')
        record_entries = []

        for row in rows:
            href = row.xpath('.//a/@href').extract_first()
            if href:
                url = 'https://www.congress.gov{}'.format(href)
                yield scrapy.Request(url=url, callback=self.parse_congressional_record)


    def parse_congressional_record(self, response):
        '''
        Process a congressional record
        ex: https://www.congress.gov/congressional-record/2017/2/1/senate-section/article/S541-2
        '''

        date = response.xpath('//div[@class="cr-issue"]/h3/text()').extract_first().strip()
        date = datetime.strptime(date, '%B %d, %Y').isoformat()

        title = response.xpath('//div[@class="wrapper_std"]/h2/text()').extract_first()

        url = response.xpath('//link[contains(@href,"congressional-record/2017")]/@href').extract_first()

        category = response.xpath('//span[@class="quiet"]/text()').extract_first().strip().split()[0][1:]

        main_body = response.xpath('//pre[@class="styled"]')
        text_blob = " ".join(main_body.xpath('.//text()').extract())

        hrefs = main_body.xpath('.//@href').extract()

        # EX: ['115th Congress, 1st Session', 'Issue: Vol. 163, No. 20 — Daily Edition']
        doc_info = response.xpath('//div[@class="cr-issue"]/h4/text()').extract()

        congress, session = doc_info[0].split(',')

        # EX ['Issue: Vol. 163', ' No. 20 — Daily Edition']
        vol_no = doc_info[1].split(',')
        vol = vol_no[0].split(':')[1].split('.')[-1].strip()
        no = vol_no[1].split('.')[1].split('—')[0].strip()


        item = Record(
            date=date,
            title=title.strip(),
            url=url,
            category=category.strip(),
            text_blob=text_blob,
            meta=doc_info,
            hrefs=hrefs,
            congress=congress.strip(),
            session=session.strip(),
            Volume=vol.strip(),
            Number=no.strip()
        )

        yield item
