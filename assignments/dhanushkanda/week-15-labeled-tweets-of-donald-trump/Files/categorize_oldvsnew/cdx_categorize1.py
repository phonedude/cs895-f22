#!/usr/bin/env python3

import os
import json
import datetime
from datetime import date
import io
import csv
import re
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from csv import writer
from csv import reader
import sys
import base64
from collections import Counter
import gzip


suspended_date = datetime.strptime("08 Jan 2021", '%d %b %Y')
reinstated_date = datetime.strptime("19 Nov 2022", '%d %b %Y')

def check_category(date):
	if date < suspended_date:
		category = "active"
	elif date > reinstated_date:
		category = "reinstated"
	elif suspended_date < date < reinstated_date:
		category = "suspended"
	return category


def separateOldUI_NewUI(clen):
	if int(clen) < 50000:
		UI = "newUI"
	else:
		UI = "oldUI"
	return UI

# g.write(f"{tid}\t{label}\t{archive}\t{date1}\t{category}\t{urim}\t{size1}\t{size2}\t{ui}\n")

def datetime_from_URIM(urim):
	#print(urim)
	date_seg = urim.split("/")[4]
	date = datetime.strptime(date_seg, '%Y%m%d%H%M%S')
	return date

if __name__ == "__main__":
		filename1 = "vtr.txt"
		filename_out = "final_URIMs_categorization_CDX.tsv"
		with open(filename1, "r") as f:
			tids = f.readlines()
		with open(filename_out, "w") as g:
			num = 1
			for tid in tids:
				try:
					tid = tid.strip("\n")
					print(num,tid)
					filename_read = f"cdx_results_vtr/{tid}.txt.gz"
					with gzip.open(filename_read, "rb") as h:
						urims = h.readlines()
					for urim in urims:
						urim,clen = urim.decode().strip("\n").rsplit(",",1)
						try:
							UI = separateOldUI_NewUI(clen)
							date = datetime_from_URIM(urim)
							category = check_category(date)
							# print(f"{tid}\tfc\t{urim}\t{date}\t{category}\t{clen}\t{UI}\n")
							g.write(f"{tid}\tvtr\t{urim}\t{date}\t{category}\t{clen}\t{UI}\n")
						except Exception as a:
							# print(a)
							pass
				except Exception as e:
					#print(tid, e)
					pass
				#break
				num = num + 1


