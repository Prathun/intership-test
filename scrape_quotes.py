import requests
from bs4 import BeautifulSoup

base_url = "http://quotes.toscrape.com/"
html = requests.get(base_url)

data = BeautifulSoup(html.text,"html.parser")


#.........................................only quotes.........................................

#quotes_data = data.select("body div.container div.col-md-8 div.quote span.text")
#for quotes in quotes_data:
 #   print(quotes.get_text(strip=True))
    
#.........................................boath quotes-author name............................

quotes_data = data.select("body div.container div.col-md-8 div.quote")

for quote_block in quotes_data:
    quote_text = quote_block.select_one("span.text").get_text(strip=True)
    author_name = quote_block.select_one("small.author").get_text(strip=True)
    print(f"{quote_text} — {author_name}")

