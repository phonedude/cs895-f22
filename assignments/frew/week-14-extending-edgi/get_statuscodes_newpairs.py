from urllib.parse import urlparse
import json
import re

def get_archive(urim):
  o = urlparse(urim)
  return o.hostname

with open('proc2.txt') as f:
    s = f.read()

#my ugly json
s = s.replace("'", '"')
s = s.strip()
s = s[0:-1] #trailing comma
s = "{ \"list\": [" + s + "]}"
add = json.loads(s)

for pair in add['list']:
    if '?' in pair['original_uri']:
        continue #process separately
    key1 = get_archive(pair['urim_2016']['uri'])
    key2 = get_archive(pair['urim_2020']['uri'])
    if key1 == 'web.archive.org' and key2 == 'web.archive.org':
      datetime1 = re.match(".*([0-9]{14}).*", pair['urim_2016']['uri'])
      datetime2 = re.match(".*([0-9]{14}).*", pair['urim_2020']['uri'])
      print(pair['original_uri'], datetime1.groups()[0], datetime2.groups()[0])

