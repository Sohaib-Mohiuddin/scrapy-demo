# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherDataApiScraperItem(scrapy.Item):
    location = scrapy.Field()
    temperature = scrapy.Field()
    condition = scrapy.Field()
    feels_like = scrapy.Field()
    forecast = scrapy.Field()
    humidity = scrapy.Field()
    url = scrapy.Field()
    
