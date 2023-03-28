from requests import get
from bs4 import BeautifulSoup

BASE_URL = "https://metanit.com"
URL = BASE_URL + "/python/tutorial/"


HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}
page = get(URL, headers=HEADERS)
soup = BeautifulSoup(page.content,  "html.parser")
tutor_list = soup.find(class_="content")


categories = []
for li in tutor_list.find_all("li"):
    a = li.find("a")
    tutor_name = a.find(text=True, recursive=False)
    tutor_link = URL + a.get("href")
    categories.append((tutor_name, tutor_link))


categories = sorted(categories, key=lambda x: x[0])


with open("tutorials.txt", "w", encoding="utf-8") as file:
    for category in categories:
        file.write(f"Категорія: {category[0]}\n")
        file.write(f"URL: {category[1]}\n")

        print(f"Категорія: {category[0]}")
        print(f"URL: {category[1]}")
