#!/usr/bin/env python3

import os
import json
import datetime
from datetime import date
import io
import csv
import re
import requests
from bs4 import BeautifulSoup
from csv import writer
from csv import reader
import sys
import base64
import time
from collections import Counter


if __name__ == "__main__":
		filename1 = "error1.txt"
		filename2 = "live-web-status_error.csv"
		with open(filename1, "r") as f:
			urls = f.readlines()
		with open(filename2, "w") as g:
			g.write("url,status_code\n")
			num = 1
			for url in urls:
				try:
					url = url.strip("\n")
					filename_out = f"liveweb_html_3/{url}.html"
					#url = "http://" + url	
					#url = "http://airport.lk"
					
					headers = {
					'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
						}
					r = requests.get(url,headers=headers, timeout=10)
					status_code = r.status_code
					html = r.text
					print(str(num) + ", " + url + ", " + str(status_code))
					num = num+1	
					#print(status_code)

					with open(filename_out, "w") as h:
						h.write(html)

					
				except Exception as e:
					status_code = "error"
					print(url, e)
					pass

				g.write(f"{url},{status_code}\n")
				g.flush()