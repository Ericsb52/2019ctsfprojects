import requests
from bs4 import BeautifulSoup as bs
from collections import Counter
import statistics

def get_data(file):
    clean_urls =[]
    text_file = open(file, "r")
    urls = text_file.readlines()
    text_file.close()
    for url in urls:
        clean_urls.append(url.split("\n")[0])
    return clean_urls

def scraper(url, tag):
    print("collecting Data")
    r = requests.get(url)
    soup = bs(r.text,"html.parser")
    links = soup.find_all("a")
    titles = titles_gen(links)
    return titles
    

def titles_gen(links):
    titles = []   

    def data_formater(url):
        if "https://" in url:
            url = url.split("https://")[-1]
            url = url.split("www.")[-1]
            url = url.split(".")[0]
            titles.append(url)


        
    for link in links:
        data_formater(link["href"])



    return titles


def stats(links):
    print(len(links))
    alllinks = set()
    for link in links:
        alllinks.add(link)
    print(len(alllinks))
    counts = Counter(links)
    counts_sorted = sorted(counts.items(), key=lambda x: x[1])
    
    def find_median(data):
        if len(data)%2 == 0:
           median = len(data)/2
    print(median)
    


    

def main():
    file = "test_url_list.txt"
    #data = get_data(file)
    data = "http://www.microsoft.com"
    links = scraper(data,"a")
    stats(links)

    
   








main()
input("press enter to exit")
