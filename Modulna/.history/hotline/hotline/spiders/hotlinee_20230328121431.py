import scrapy
from bs4 import BeautifulSoup
import csv

class HotlineSpider(scrapy.Spider):
    name = 'hotline'
    allowed_domains = ['hotline.ua']
    start_urls = ['https://hotline.ua/ua/bt/kuhonnye-plity-i-poverhnosti/']

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        products = soup.find_all('div', class_='product-item')

        for product in products:
            name = product.find('a', class_='item-title').text.strip()
            url = product.find('a', class_='item-title')['href']
            price = product.find('div', class_='price-md').text.strip()

            stores = product.find('div', class_='price-md').find_all('a')
            store_count = len(stores)

            if store_count > 10:
                yield {
                    'name': name,
                    'url': url,
                    'price': price,
                    'store_count': store_count
                }

                # Запис даних у CSV файл
                with open('hotline.csv', mode='a', encoding='utf-8', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([name, url, price, store_count])
