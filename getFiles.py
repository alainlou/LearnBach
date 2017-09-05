from bs4 import BeautifulSoup as bs
import requests
import urllib.request

url = "http://www.jsbach.net/midi/"
sub =  "midi_wtc2.html"

r = requests.get(url + sub)
soup = bs(r.text)

links = []
names = []

for i, link in enumerate(soup.findAll('a')):
    if link.get('href').endswith('.mid'):
        links.append(url+link.get('href'))
        names.append(soup.select('a')[i].attrs['href'])

names_links = zip(names,links)

for name,link in names_links:
    rq = urllib.request.Request(link)
    try:
        res = urllib.request.urlopen(rq)
        file = open("midi/" + name, "wb")
        file.write(res.read())
        file.close()
        print(link)
    except:
        print(link + " did not work")
