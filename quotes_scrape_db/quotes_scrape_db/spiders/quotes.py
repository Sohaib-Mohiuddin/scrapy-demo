import scrapy
from ..items import QuotesScrapeDbItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/tag/humor/',
    ]
    
    def parse(self, response):
        
        quote_items = QuotesScrapeDbItem()
        
        for quote in response.css('div.quote'):
            
            quote_items['text'] = quote.css('span.text::text').get()
            quote_items['author'] = quote.xpath('span/small/text()').get()
            
            yield quote_items
        
        next_page = response.css('li.next a::attr("href")').get()
        
        if (next_page is not None):
            yield response.follow(next_page, self.parse)

    # def parse_quote(self, response):
    #     pass