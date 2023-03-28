import scrapy
from bs4 import BeautifulSoup
import csv
from hotline.items import HotlineItem

class HotlineSpider(scrapy.Spider):
    name = 'hotline'
    allowed_domains = ['hotline.ua']
    start_urls = ['https://hotline.ua/ua/bt/kuhonnye-plity-i-poverhnosti/']

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        products = soup.find(
            name="div", class_="list-body__content").find_all(class_="list-item")

        for product in products:
            name = product.find(name="a", class_="list-item__title").find(
                string=True, recursive=False).strip()
            url = product.find(name="a", class_="list-item__title").get("href")
            price = product.find(class_="price__value").find(
                string=True, recursive=False)
            stores = product.find_all("a", class_="shop__title")
            
            # перевіряємо, чи продається продукт в більше ніж 10 магазинах
            if len(stores) > 10:
                yield HotlineItem(
                    name=name,
                    url=url,
                    price=price,
                )