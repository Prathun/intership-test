import requests
from bs4 import BeautifulSoup

base_url = "https://books.toscrape.com/"
html = requests.get(base_url).text

data = BeautifulSoup(html,"html.parser")
books_data = data.select("article.product_pod .product_price .price_color")

#........................................to get books name...................................................

#for books_title in books_data:
 #   print(books_title["title"])

#........................................to get books price with oreder.......................................


#for i, books_price in enumerate(books_data, start=1):
 #   price_text = books_price.get_text(strip=True)
  #  print(f"Book {i}: {price_text}")
  
#.........................................to get books price only.............................................

for books_price in books_data:
    print(books_price.get_text(strip=True))
