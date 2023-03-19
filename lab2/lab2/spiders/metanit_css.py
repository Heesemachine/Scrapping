import scrapy
from lab2.items import MetanitItem


class MetanitCssSpider(scrapy.Spider):
    name = "metanit_css"
    allowed_domains = ["metanit.com"]
    start_urls = ["https://metanit.com/python/tutorial/"]

    def parse(self, response):
        tutor_list = response.css('ol.content').css('li')

        for tutor in tutor_list:
            name = tutor.css('a::text').get()
            url = tutor.css('a::attr(href)').get()
            yield MetanitItem(
                name=name,
                url=url
            )