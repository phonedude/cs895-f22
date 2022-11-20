from urllib.parse import urlparse
import json

def get_archive(urim):
  o = urlparse(urim)
  return o.hostname

with open('aggregf.txt') as f:
    s = f.read()

#my ugly json
s = s.replace("'", '"')
s = s.strip()
s = s[0:-1] #trailing comma
s = "{ \"list\": [" + s + "]}"
add = json.loads(s)

archives = {}

for pair in add['list']:
    key = get_archive(pair['urim_2016']['uri'])
    if key != 'web.archive.org':
      archives.setdefault(key, 0)
      archives[key] = archives[key] + 1
    key = get_archive(pair['urim_2020']['uri'])
    if key != 'web.archive.org':
      archives.setdefault(key, 0)
      archives[key] = archives[key] + 1

print(archives)

#{'arquivo.pt': 22, 'wayback.archive-it.org': 8, 'webarchive.loc.gov': 14, 'waext.banq.qc.ca': 1}
#{'arquivo.pt': 25, 'webarchive.loc.gov': 3490, 'archive.md': 1, 'wayback.archive-it.org': 2, 'perma.cc': 1}
#{'webarchive.loc.gov': 774, 'arquivo.pt': 162, 'wayback.archive-it.org': 21}
#{'webarchive.loc.gov': 721, 'arquivo.pt': 4}