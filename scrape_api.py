
import requests
from fake_useragent import UserAgent

ua = UserAgent()
user_agent = ua.random
if "mobile" in user_agent or "iphone" in user_agent or "android" in user_agent :
    user_agent = ua.chrome
else :
    user_agent = user_agent    


api_url = "https://api.nike.com/search/suggestions/v1?country=IN&language=en-gb&count=20"


headers = {"User-Agent" : user_agent}


response = requests.get(api_url,headers=headers)
data = response.json()

for items in data["searchTerms"] :
    display_item = items["displayText"]
    print(display_item)
    