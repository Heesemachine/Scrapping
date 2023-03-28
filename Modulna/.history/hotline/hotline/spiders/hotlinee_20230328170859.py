import scrapy
from bs4 import BeautifulSoup

class HotlineSpider(scrapy.Spider):
    name = 'hotline'
    allowed_domains = ['hotline.ua']
    start_urls = ['https://hotline.ua/ua/bt/kuhonnye-plity-i-poverhnosti/']

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        products = soup.find(
            name="div", class_="list-body__content").find_all(class_="list-item")

        with open("products.txt", "a", encoding="utf-8") as file:
            for product in products:
                name = product.find(name="a", class_="list-item__title").find(
                    string=True, recursive=False).strip()
                url = product.find(name="a", class_="list-item__title").get("href")
                price = product.find(class_="price__value").find(
                    string=True, recursive=False)
                stores = product.find_all("a", class_="shop__title")
                
                # записуємо дані в файл
                file.write(f"{name} - {price}\n")
                for store in stores:
                    file.write(f"\t{store.text.strip()}\n")
                file.write("\n")
