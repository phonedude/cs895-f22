filename1 = "fc.txt"
filename2 = "chart1from2017.csv"
filename3 = "abcd.tsv"

with open(filename2, "r") as g:
	idtimes = g.readlines()
	#print(idtimes)

with open(filename1, "r") as f:
	tids = f.readlines()
	#print(tids)
	for tid in tids:
		tid = tid.strip("\n")
		#print(tid)
		for idtime in idtimes:
			idtime = idtime.strip("\n")
			#print(idtime)
			i, time = idtime.split(",")
			print(i)
			if tid == i:
				with open(filename3, "a") as h:
					h.write(idtime+"\n")