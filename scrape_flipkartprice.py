
import requests

from bs4 import BeautifulSoup

from fake_useragent import UserAgent

ua = UserAgent()
user_agent = ua.random

if "mobile" in user_agent or "iphone" in user_agent or "android" in user_agent :
    user_agent = ua.chrome
else :
    user_agent = user_agent   


headers = {"User-Agent": user_agent}


base_url = "https://www.flipkart.com/search?q=samsung+mobile+&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={}"

pages = 10
for page in range(1, pages + 1):

    url = base_url.format(page)

    response = requests.get(url, headers=headers)

    data = BeautifulSoup(response.text, "html.parser")

    items = data.find_all("div", class_="Nx9bqj _4b5DiR")

    for mobile_price in items:
        print(mobile_price.get_text(strip=True))





