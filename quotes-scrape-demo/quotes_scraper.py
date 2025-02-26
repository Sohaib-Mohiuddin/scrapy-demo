import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/tag/humor/',
    ]
    
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.xpath('span/small/text()').get()
            }
        
        next_page = response.css('li.next a::attr("href")').get()
        
        if (next_page is not None):
            yield response.follow(next_page, self.parse)
    
    def closed(self, reason):
        """Ensure JSONL file is written with Unicode characters"""
        with open("quotes.jsonl", "r", encoding="utf-8") as file:
            lines = file.readlines()

        with open("quotes_unicode.jsonl", "w", encoding="utf-8") as file:
            for line in lines:
                json_obj = json.loads(line)  # Load JSON line
                file.write(json.dumps(json_obj, ensure_ascii=False) + "\n")  # Save with decoded Unicode