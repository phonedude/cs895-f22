#!/usr/bin/env python3

from bs4 import BeautifulSoup
from urllib.parse import urlparse

def scrape(soup,cat,g):	
	td = soup.find("td", id=f"{cat}")				
	a_tags = td.find_all('a', href=True)
	#urls = []
	for tag in a_tags:
		link = tag['href']
		url = urlparse(link)
		hostname = url.hostname
		desc = tag.text
		desc = desc.replace('\n',' ')
		#print(desc)
		a = (link,desc)
		g.write(f"{cat},{link},{hostname},{desc}\n")

if __name__ == "__main__":
	with open('oneworld.html', 'r') as f:
		html = f.read()	
	with open('oneworld.csv', 'w') as g:
		g.write("category,url,hostname,discription\n")
		categories = ["Environment","History","Government","News","Culture","Business","Education"]
		soup = BeautifulSoup(html, 'lxml')
		for cat in categories:			
			scrape(soup,cat,g)
			#break




