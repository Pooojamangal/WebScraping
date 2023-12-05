import requests
from bs4 import BeautifulSoup
import pprint
res = requests.get("https://news.ycombinator.com/")
Soup = BeautifulSoup(res.text, 'html.parser')

print(Soup.select('#score_38331097'))
links = Soup.select('.titleline > a')
votes = Soup.select('.score')
subtext = Soup.select('.subtext')
def Sort_Stories_by_votes(hnlist):
    return sorted(hnlist, key = lambda k:k['votes'], reverse= True)
def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(votes[idx].getText().replace('points'," "))
            hn.append({'title': title, 'link' :href, 'votes': points })
    return Sort_Stories_by_votes(hn)
pprint.pprint(create_custom_hn(links, subtext))


















