import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
headers = {"User-Agent": ua.chrome}

base_url = "https://www.flipkart.com/search?q=samsung+phone+under+60000&page={}"

pages = 5
for page in range(1, pages + 1):
    print(f"\n--- Page {page} ---")

    url = base_url.format(page)
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Failed to retrieve page")
        continue

    soup = BeautifulSoup(response.text, "html.parser")

    names = soup.find_all("div", class_="KzDlHZ")
    prices = soup.find_all("div", class_="Nx9bqj _4b5DiR")

    print(f"Found {len(names)} product names and {len(prices)} prices.\n")

    for name, price in zip(names, prices):
        print(f"{name.get_text(strip=True)} - {price.get_text(strip=True)}")
