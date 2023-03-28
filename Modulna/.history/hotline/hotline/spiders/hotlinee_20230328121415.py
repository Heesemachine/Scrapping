import scrapy


class HotlineeSpider(scrapy.Spider):
    name = "hotlinee"
    allowed_domains = ["hotline.ua"]
    start_urls = ["http://hotline.ua/"]

    def parse(self, response):
        pass
