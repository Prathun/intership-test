
import requests

from bs4 import BeautifulSoup

from fake_useragent import UserAgent

import time

ua = UserAgent()

headers = {"User-Agent": ua.random}


base_url = "https://www.flipkart.com/search?q=samsung+mobile+&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={}"


pages = 10
for page in range(1,pages+1):

    url = base_url.format(page)

    response = requests.get(url,headers=headers)

    data = BeautifulSoup(response.text,"html.parser")

    products = data.find_all("div", class_="_1AtVbE col-12-12")



    for item in products:
        name_tag = item.find("div", class_="KzDlHZ") 
        price_tag = item.find("div", class_="Nx9bqj _4b5DiR")

        if name_tag and price_tag:
            mobile_name = name_tag.get_text(strip=True)
            mobile_price = price_tag.get_text(strip=True)
            print(f"{mobile_name} - {mobile_price}")


    time.sleep(1)