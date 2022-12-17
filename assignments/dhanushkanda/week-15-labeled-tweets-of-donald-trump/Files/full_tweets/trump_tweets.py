#!/usr/bin/env python3

from bs4 import BeautifulSoup
import csv
import sys

html_content = open("trumptwitterarchive.html", "r")
filename1 = "tweet.csv"
filename2 = "vtr.txt"
filename4 = "fc.txt"
filename3 = "overlap.csv"
 
str1 = "vtr"
str2 = "fc"

idlist_vtr = []
idlist_fc = []

with open(filename2, "r") as f:
	twitterids = f.readlines()
	for twitterid in twitterids:
		twitterid = twitterid.strip("\n")
		idlist_vtr.append(twitterid)

with open(filename4, "r") as k:
	twitterids = k.readlines()
	for twitterid in twitterids:
		twitterid = twitterid.strip("\n")
		idlist_fc.append(twitterid)

#print(idlist_vtr)
#print("\n")
#print(idlist_fc)
# print(len(idlist_vtr))
# print(len(idlist_fc))


soup = BeautifulSoup(html_content, "html.parser")

#print(soup)

content = soup.find_all("tr")	
#print(content)

f = open(filename1, 'w')
writer = csv.writer(f)

for item in content:
	#print(item)
	tds = item.find_all("td")
	#print(tds)
	#print("\n")

	try:
		tid = tds[0].text
		# for td in tds:
		# 	print(td.text)
		datetime = tds[1].text
		tweet = tds[2].text
		device = tds[3].text
		num = int(tds[0].text)
		#print(type(num))
		roww = [tds[0].text, tds[1].text, tds[2].text, tds[3].text]


		if num in idlist_vtr:
			with open(filename3, "a") as l:
				roww += str1
				l.write(roww)
				l.flush()

		if num in idlist_fc:
			with open(filename3, "a") as m:
				roww += str2
				m.write(roww)
				m.flush()

		#jj = f"{tid}, {datetime}, '{tweet}', '{device}'"
		#print(jj)
		writer.writerow(roww)
	except Exception as e:
		print("gibberish")

f.close()

		


