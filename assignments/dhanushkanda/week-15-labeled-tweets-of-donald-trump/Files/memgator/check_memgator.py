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

label = sys.argv[1]

if __name__ == "__main__":
		filename1 = f"{label}.txt"
		filename2 = f"memgator_summary_{label}.csv"
		filename3 = "all_mementos.csv"
		with open(filename1, "r") as f:
			tids = f.readlines()
		with open(filename3, "a") as file:
			#file.write("tid,label,archive,urim\n")
			with open(filename2, "w") as g:
				g.write("tid,archive,copies\n")
				num = 1
				for tid in tids:
					tid = tid.strip("\n")
					filename_out = f"memgator_results_{label}/{tid}.txt"
					req = "https://memgator.cs.odu.edu/timemap/link/twitter.com/realDonaldTrump/status/" + tid
					print(str(num) + " " + tid)
					num = num+1
					req = '"' + req + '"'
					awk1 = '{print $1}'
					awk2 = '{print $3}'
					#cmd = f"curl -s {req} | grep datetime | awk '{awk1}'| awk -v FS=/ '{awk2}' | sort"
					cmd = f"curl -s {req} | grep datetime | awk '{awk1}'"
					b = os.popen(cmd)
					out = b.read()
					# with open(filename_out, "w") as h:
					# 	h.write(out)

					lst = list(out.split("\n"))
					out4 = []
					del lst[-1]
					with open(filename_out, "w") as h:
						for item in lst:
							urim = item[1:-2]+"\n"
							#print(urim)
							h.write(urim)
							archive = item.split("/")[2]
							out4.append(archive)
							file.write(f"{tid},{label},{archive},{urim}")
					
					# out2 = []
					# for i in lst:
					# 	archive = i.split("/")[2]
					# 	out2.append(archive)
					#out2 = out.split("\n")
					out3 = [x for x in out4 if x]

					for item in Counter(out3):
						copies = Counter(out3)[item]
						g.write(f"{tid},{item},{copies}\n")
						g.flush()				