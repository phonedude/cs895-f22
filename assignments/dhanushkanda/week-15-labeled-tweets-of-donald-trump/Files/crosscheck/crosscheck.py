filename1 = "tweetidsfull.txt"
filename2 = "vtr.txt"
filename3 = "fc.txt"
filename4 = "overlap.csv"

str1 = "vtr"
str2 = "fc"

idlist_vtr = []
idlist_fc = []
idlist_full = []

with open(filename1, "r") as g:
	twitterids = g.readlines()
	for twitterid in twitterids:
		twitterid = twitterid.strip("\n")
		idlist_full.append(twitterid)

with open(filename2, "r") as f:
	twitterids = f.readlines()
	for twitterid in twitterids:
		twitterid = twitterid.strip("\n")
		idlist_vtr.append(twitterid)

with open(filename3, "r") as k:
	twitterids = k.readlines()
	for twitterid in twitterids:
		twitterid = twitterid.strip("\n")
		idlist_fc.append(twitterid)

for item in idlist_full:
	if item in idlist_vtr:
		print(item, str1)
		idlist_vtr.remove(item)
	elif item in idlist_fc:
		print(item, str2)
		#print(type(item))
		#item = int(item)
		idlist_fc.remove(item)

print(idlist_fc)


