#!/usr/bin/env python3
import sys
import requests

def separateOldUI_NewUI(clength):
	if clength < 200000:
		UI = "newUI"
	else:
		UI = "oldUI"
	return UI

# input_file = sys.argv[1]
# output_file = sys.argv[2]

input_file = "content_length.tsv"
output_file = "categorization.tsv"

if __name__ == "__main__":
	with open(input_file, "r") as f:
		all_list = f.readlines()
		#print(all_list)
		with open(output_file, "a") as g:
			for item in all_list:
				item.strip("\n")
				try:
					tid,label,archive,date1,category,urim,size1,size2 = item.split("\t")			
					size2 = size2.strip("\n")
					#print(size2)
					size2 = int(size2)
					#print(size2)
					ui = separateOldUI_NewUI(size2)
					print(urim, size2, ui)
					g.write(f"{tid}\t{label}\t{archive}\t{date1}\t{category}\t{urim}\t{clength}\n")
					g.flush()
				except Exception as e:
					#print(e)
					pass


	#for item in all_list:
		#print(item.strip("\n"))
		#blah blah
		##UI = separateOldUI_NewUI(clength)
		#add UI to our file