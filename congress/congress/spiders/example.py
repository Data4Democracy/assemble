import scrapy
from congress.items import Article


class Example(scrapy.Spider):
    '''Modeled after scrapy tutorial here:

    https://doc.scrapy.org/en/latest/intro/tutorial.html
    '''

    # spider name should be name of website/source
    name = 'example'

    def start_requests(self):
        # list of URLs or single URL to start carwl
        urls = [
            'http://quotes.toscrape.com/page/1/'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        '''to learn more about xpath selectors:

        https://doc.scrapy.org/en/latest/topics/selectors.html
        '''

        language = response.xpath('//html/@lang').extract_first()
        url = response.url
        source = 'example'  # spider name

        # Select all quotes
        quotes = response.xpath('//div[@class="quote"]')

        for quote in quotes:
            # Each quote is itself a selector xpath.
            # To dig deeper inside this path use ".//" syntax
            text_blob = quote.xpath('.//span/text()').extract_first()

            # Using [contains@class] for illustrative purposes. We could have used
            # @class="author" as well.  This will return any small tag with class
            # that contains the word "author"
            author = quote.xpath('.//small[contains(@class, "author")]').extract_first()

            # now we create our article item for a list of available fields see items.py
            article = Article(
                    # Required fields
                    language=language,
                    url=url,
                    source=source,
                    text_blob=text_blob,
                    # Optional field (add anything your site provides)
                    authors=author
            )

            # Sends our article off to the pipeline for validation!

            yield article
