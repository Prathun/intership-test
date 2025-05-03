import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent



base_url = "https://www.flipkart.com/search?q=samsung+mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={}"

ua = UserAgent()

header = {
    "User-Agent": ua.random
}

pages = 10
for page in range(1,pages+1):
    url=base_url.format(page)


    response = requests.get(url, headers=header)


    data = BeautifulSoup(response.text, "html.parser")



    items = data.find_all("div", class_="KzDlHZ")

    for mobile_name in items:
         
         print(mobile_name.get_text(strip=True))
