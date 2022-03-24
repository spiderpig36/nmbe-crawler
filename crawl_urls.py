import sys
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

top_url = sys.argv[1]
top_url_parse = urlparse(top_url)
 
urls = { top_url: False }
new_urls = urls
while len(new_urls) > 0:
    new_urls = {}
    for url in urls:
        if not urls[url]:
            print("Processing url: " + url)
            reqs = requests.get(url)
            soup = BeautifulSoup(reqs.text, 'html.parser')
            for link in soup.find_all('a'):
                linkUrl = str(link.get('href'))
                if linkUrl.startswith(top_url) and not linkUrl in urls.keys() and not linkUrl in new_urls.keys():
                    if not "?share=" in linkUrl and not "?ical=" in linkUrl and not linkUrl.endswith("#respond") and not "#more-" in linkUrl and not "#comment" in linkUrl and not "wp-content" in linkUrl:
                        print("New url: " + linkUrl)
                        new_urls[linkUrl] = False
        urls[url] = True
    urls.update(new_urls)

url_list = list(urls.keys())
url_list.sort()

with open('crawl_' + top_url_parse.netloc + '.txt', 'w') as f:
    for url in url_list:
        f.write(url + "\n")