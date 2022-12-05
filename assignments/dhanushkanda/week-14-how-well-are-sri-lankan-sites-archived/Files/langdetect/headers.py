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
		filename1 = "lksites.txt"
		#filename2 = "memgator_summary.csv"
		with open(filename1, "r") as f:
			urls = f.readlines()
		with open(filename2, "w") as g:
			g.write("url,archive,copies\n")
			num = 1
			for url in urls:
				url = url.strip("\n")
				filename_out = f"memgator_results/{url}.txt"
				req = "https://memgator.cs.odu.edu/timemap/link/" + url + "/"
				print(str(num) + " " + url)
				num = num+1
				req = '"' + req + '"'
				awk1 = '{print $1}'
				awk2 = '{print $3}'
				#cmd = f"curl -s {req} | grep datetime | awk '{awk1}'| awk -v FS=/ '{awk2}' | sort"
				cmd = f"curl -s {req} | grep datetime | awk '{awk1}'"
				b = os.popen(cmd)
				out = b.read()
				with open(filename_out, "w") as h:
					h.write(out)

				lst = list(out.split("\n"))
				del lst[-1]
				out2 = []
				for i in lst:
					archive = i.split("/")[2]
					out2.append(archive)
				#out2 = out.split("\n")
				out3 = [x for x in out2 if x]

				for item in Counter(out3):
					copies = Counter(out3)[item]
					g.write(f"{url},{item},{copies}\n")
					g.flush()				