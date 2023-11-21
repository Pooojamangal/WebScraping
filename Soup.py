import requests
from bs4 import BeautifulSoup
res = requests.get("https://news.ycombinator.com/")
Soup = BeautifulSoup(res.text, 'html.parser')

print(Soup.select('#score_38331097'))
links = Soup.select('.age')


