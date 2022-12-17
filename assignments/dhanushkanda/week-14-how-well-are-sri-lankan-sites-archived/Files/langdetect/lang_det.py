#!/usr/bin/env python3

from bs4 import BeautifulSoup

html_content = open("/home/marsh/Documents/Skanda/sl_archive/language/aruna.lk.html", "r")
 
def remove_tags(html):
	soup = BeautifulSoup(html, "html.parser")
	for data in soup(['style', 'script']):
		data.decompose()
	return ' '.join(soup.stripped_strings)
  
html_withouttags = remove_tags(html_content)

detectlanguage.detect(html_withouttags)


html_content_ta = open("/home/marsh/Documents/Skanda/sl_archive/language/thamilan.lk.html", "r")
html_withouttags_ta = remove_tags(html_content_ta)
detectlanguage.detect(html_withouttags_ta)