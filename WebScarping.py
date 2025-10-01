import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com')
res2 = requests.get('https://news.ycombinator.com/?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links = soup.select('.titleline')
links2 = soup2.select('.titleline')
votes = soup.select('.score')
votes2 = soup2.select('.score')

mega_links = links + links2
mega_votes = votes + votes2

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key = lambda k:k['votes'], reverse = True)

def create_custom_hm(links, votes):
    hn = []
    for i, item in enumerate(links):
        a_tag = item.find('a')
        title = a_tag.getText()
        href = a_tag.get('href')
        if i < len(votes):
            points = int(votes[i].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link':href, 'votes': points})
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hm(mega_links, mega_votes))

#Moze i sa petljom, cistije

'''
import requests
from bs4 import BeautifulSoup
import pprint

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)

def create_custom_hm(links, votes):
    hn = []
    for i, item in enumerate(links):
        a_tag = item.find('a')
        title = a_tag.getText()
        href = a_tag.get('href')
        if i < len(votes):
            points = int(votes[i].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return hn

all_links = []
all_votes = []

num_pages = 3   # koliko stranica želiš da skineš

for page in range(1, num_pages + 1):
    res = requests.get(f'https://news.ycombinator.com/news?p={page}')
    soup = BeautifulSoup(res.text, 'html.parser')
    all_links.extend(soup.select('.titleline'))
    all_votes.extend(soup.select('.score'))

hn = create_custom_hm(all_links, all_votes)
sorted_hn = sort_stories_by_votes(hn)

pprint.pprint(sorted_hn)

'''
