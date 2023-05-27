# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ModulnakrItem(scrapy.Item):
    model = scrapy.Field()
    img_url = scrapy.Field()
    config = scrapy.Field()
    price = scrapy.Field()