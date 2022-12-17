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
import gzip

if __name__ == "__main__":
		filename1 = "vtr.txt"
		#filename2 = "urims.csv"
		with open(filename1, "r") as f:
			tids = f.readlines()
		#with open(filename2, "w") as g:
			#g.write("url,archive,copies\n")
			num = 1
			for tid in tids:
				try:
					tid = tid.strip("\n")
					filename_out = f"cdx_results_vtr/{tid}.txt.gz"
					url = "https://twitter.com/realDonaldTrump/status/" + tid

					#req = "https://memgator.cs.odu.edu/timemap/link/" + url + "/"
					print(str(num) + " " + tid)
					num = num+1
					url =  "http://web.archive.org/cdx/search/cdx?url=%s&matchType=prefix" % url
					#prefix = "https://web.archive.org/web/"
					awk = '{print "https://web.archive.org/web/" $2 "/" $3};'
					cmd = "curl -s '%s' | awk '%s'" % (url,awk)
					out = os.popen(cmd)
					urims = out.read()
					#urims = bytes(urims,'utf-8')
					with gzip.open(filename_out, "wb") as h:
							h.write(urims.encode())
							h.flush()
					
				except Exception as e:
					print(tid, e)
					with open(filename_out, "w") as h:
							h.write("error")
							h.flush()


