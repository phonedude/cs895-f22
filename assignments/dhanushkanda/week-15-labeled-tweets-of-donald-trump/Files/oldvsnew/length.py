import requests

filename1 = "all_mementos.tsv"
filename2 = "content_length.tsv"

with open(filename1, "r") as f:
	lines = f.readlines()

with open(filename2, "w") as g:
	for line in lines:
		line.strip("\n")
		tid,label,archive,date1,category,urim = line.split("\t")
		urim = urim.strip("\n")
		print(tid)
		#elements = values.split("/")
		#print(values[2])
		
		headers = {'Accept-Encoding': None}
		try:
			res = requests.get(urim,headers=headers, timeout=30)
			headers = res.headers
			clength = headers["Content-Length"]
			#print(headers["Content-Length"])
		except Exception as e:
			clength = "error"
		g.write(f"{tid}\t{label}\t{archive}\t{date1}\t{category}\t{urim}\t{clength}\n")
		g.flush()
		
	