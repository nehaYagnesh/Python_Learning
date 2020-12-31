""" Web Scraping
When a program or script pretends to be a browser and retrieves
web pages,looks at those web pages, extracts information, and then looks at more web pages

Search engines scrape web pages - we can this 'spidering the web' or 'web crawling' 

Why Scrape ?
    1. Pull data - particularly social data - who links to who?
    2. Get your own data back out of some system that has no 'export capability'
    3. Monitor a site for new information
    4. Spider the web to make a database for a search engine """

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter the URL: ')  
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html,'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href',None))