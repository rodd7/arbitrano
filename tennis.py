import requests
from bs4 import BeautifulSoup

TAB = "https://www.tab.com.au/sports/betting/Tennis" # POSITION 0

soup = BeautifulSoup(requests.get(TAB).text, "html.parser")
player = soup.find('span', class_='participant')
print(soup.prettify())


# https://marktheballot.blogspot.com/2018/06/the-dramas-of-daily-web-scraper.html