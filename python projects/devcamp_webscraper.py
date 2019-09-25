import requests
from bs4 import BeautifulSoup as bs

def titles_gen(links):
    titles = []

    def formatter(url):
        if "/posts/" in url:
            url = url.replace("/posts/","")
            url = url.replace("-", " ")
            url = url.title()
            titles.append(url)
            
        

    for link in links:
        formatter(link["href"])

    return titles
#scraping data from site    
r = requests.get("https://www.dailysmarty.com/topics/python")
#creating soup object to work with in html format
soup = bs(r.text,"html.parser")
#finding and collecting all links on the page
links = soup.find_all("a")
#call method to format all the titles of the links
titles = titles_gen(links)
#display titles formated corectley
for title in titles:
    print (title)


