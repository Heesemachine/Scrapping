import scrapy
from modulnakr.items import ModulnakrItem
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from modulnakr.SeleniumRequest import SeleniumRequest

class EkSpider(scrapy.Spider):
    name = "ek"
    allowed_domains = ["ek.ua"]
    start_urls = ["https://ek.ua/ua/list/30/"]

    driver = webdriver.Chrome('/path/to/chromedriver')

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=10,
                wait_until=expected_conditions.element_to_be_clickable(
                    (By.CSS_SELECTOR,
                     ".model-shop-name .sn-div")
                ),
            )

    def parse(self, response):
        self.driver.get(response.url)
        self.driver.maximize_window()

        soup = BeautifulSoup(response.text, 'html.parser')

        laptops = soup.find(id="list_form1").find_all(class_="model-short-div list-item--goods")

        for laptop in laptops:
            model = laptop.find(class_="u").getText()
            img_url = laptop.find("img")["src"]

            price = laptop.find('td', class_="model-shop-price").find("a").getText()

            print(price)
            

            configs = laptop.find(class_="model-short-info").findAll("u")

            i = 1
            for config in configs:
                config = config.getText()
                yield ModulnakrItem(
                    model=model,
                    img_url=img_url,
                    price=price,
                    config=config,
                )

                i += 1
                if i > 7:
                    break

    def close(self, reason):
        self.driver.quit()
