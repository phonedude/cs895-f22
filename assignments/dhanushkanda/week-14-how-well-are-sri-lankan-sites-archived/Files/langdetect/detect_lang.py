#!/usr/bin/env python3

from bs4 import BeautifulSoup
import detectlanguage


def remove_tags(html):
	soup = BeautifulSoup(html, "html.parser")
	for data in soup(['style', 'script']):
		data.decompose()
	return ' '.join(soup.stripped_strings)

if __name__ == "__main__":
	#read file
	detectlanguage.configuration.api_key = "167b351ef02456a85057df3dd58a84f0"

	with open("473_200_ok.txt",'r') as f:
		sites = f.readlines()
	with open('lang_out_1.csv', 'w') as g:
		g.write("url,top_lang,n_lang,all_langs\n")	
		num = 1
		for url in sites:
			try:
				url = url.strip("\n")
				print(str(num) + " " + url)
				num = num+1
				file_loc = "liveweb_html/" + url + ".html"
				html_content = open(file_loc, "r").read() 
				html_withouttags = remove_tags(html_content)
				lang = detectlanguage.detect(html_withouttags)
				n_lang = len(lang)
				top = lang[0]["language"]		
				lang_list = []
				for item in lang:
					lang_list.append(item["language"])
				langs = "-".join(lang_list)
				g.write(f"{url},{top},{n_lang},{langs}\n")
				g.flush()
			except Exception as e:
				g.write(f"{url},-,-,-\n")
				print("error")







	# #list = ["/home/marsh/Documents/Skanda/sl_archive/language/aruna.lk.html","/home/marsh/Documents/Skanda/sl_archive/language/thamilan.lk.html"]
	# with open('lang_out.csv', 'w') as g:
	# 	g.write("url,top_lang,n_lang,all_lang\n")
	# 	for file_loc in lst:
	# 		html_content = open(file_loc, "r").read() 
	# 		html_withouttags = remove_tags(html_content)
	# 		lang = detectlanguage.detect(html_withouttags)
	# 		n_lang = len(lang)
	# 		for item in lang:







