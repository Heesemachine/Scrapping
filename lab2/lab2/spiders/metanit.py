import scrapy
from bs4 import BeautifulSoup
from lab2.items import MetanitItem


class MetanitSpider(scrapy.Spider):
    name = "metanit"
    allowed_domains = ["metanit.com"]
    start_urls = ["https://metanit.com/python/tutorial/"]
    def parse(self, response):
        soup = BeautifulSoup(response.body,  "html.parser")
        tutor_list = soup.find(class_="content")
        for li in tutor_list.find_all("li"):
            a = li.find("a")
            tutor_list_name = a.find(string=True, recursive=False)
            tutor_list_url = f"https://metanit.com/{a.get('href')}"
            yield MetanitItem(
                name=tutor_list_name,
                url=tutor_list_url
            )
