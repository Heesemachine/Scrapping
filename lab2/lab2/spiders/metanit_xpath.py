import scrapy
from lab2.items import MetanitItem


class MetanitXpathSpider(scrapy.Spider):
    name = "metanit_xpath"
    allowed_domains = ["metanit.com"]
    start_urls = ["https://metanit.com/python/tutorial/"]

    def parse(self, response):
        tutor_list = response.xpath('//ol[contains(@class, "content")]').xpath('.//li')

        for tutor in tutor_list:
            name = tutor.xpath('.//a/text()').get()
            url = tutor.xpath('.//a/@href').get()
            yield MetanitItem(
                name=name,
                url=url
            )