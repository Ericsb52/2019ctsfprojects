import requests
from bs4 import BeautifulSoup as bs
def get_data(file):
    clean_urls =[]
    text_file = open(file, "r")
    urls = text_file.readlines()
    text_file.close()
    for url in urls:
        clean_urls.append(url.split("\n")[0])
    return clean_urls

def scraper(urls, tag):
    print("collecting Data")
    clean_links = []
    results = []
    for url in urls:
        results.append(requests.get(url))
    html_soup = []
    print(results)
    for result in results:
        html_soup.append(bs(result.text,"html.parser"))
    print(html_soup)
    links = []
    for x in html_soup:
        links.append(x.find_all(tag))
    print(links)
    

    def data_formater(url):
        if "www." in url:
##            url = url.split("www.")[-1]
##            url = url.split(".com")[0]
            clean_links.append(url)
            print(url)

        
    for link in links:
        try:
            data_formater(link["href"])
        except:
            continue
    return clean_links

    
def main():
    file = "test_url_list.txt"
    data = get_data(file)
    links = scraper(data,"a")
    print(links)
    
   








main()
input("press enter to exit")
