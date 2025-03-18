import scrapy


class ImagespiderSpider(scrapy.Spider):
    name = "imagespider"
    # allowed_domains = [wikipedia.org]
    start_urls = ["https://en.wikipedia.org/wiki/Eiffel_Tower"]

    def parse(self, response):
        raw_image_urls = response.css('img ::attr(src)').getall()
        clean_image_urls = []
        for img_url in raw_image_urls:
            clean_image_urls.append(response.urljoin(img_url))
        
        yield {"image_urls": clean_image_urls}
