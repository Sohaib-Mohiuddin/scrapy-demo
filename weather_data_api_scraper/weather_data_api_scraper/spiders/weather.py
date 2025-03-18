import scrapy
from ..items import WeatherDataApiScraperItem

class WeatherSpider(scrapy.Spider):
    name = "weather"
    allowed_domains = ["www.timeanddate.com"]
    start_urls = ["https://www.timeanddate.com/weather/"]

    def parse(self, response):
        country = getattr(self, 'country', 'canada') 
        city = getattr(self, 'city', 'toronto')
        
        country_url = f'https://www.timeanddate.com/weather/{country}/{city}'
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36"
        }
        
        yield scrapy.Request(url=country_url, callback=self.parse_weather, headers=headers)
    
    def parse_weather(self, response):
        item = WeatherDataApiScraperItem()
        
        item['location'] = response.css("h1::text").get(default="N/A").strip()
        item['temperature'] = response.css("div.h2::text").get(default="N/A").strip()
        item['condition'] = response.css("div.h2 + p::text").get(default="N/A").strip()
        item['feels_like'] = response.xpath("//p[contains(text(),'Feels Like')]/span/text()").get(default="N/A").strip()
        item['forecast'] = response.xpath("//p[contains(text(),'Forecast')]/span/text()").get(default="N/A").strip()
        item['humidity'] = response.xpath("//tr[th[contains(text(),'Humidity')]]/td/text()").get(default="N/A").strip()
        item['url'] = response.url

        yield item