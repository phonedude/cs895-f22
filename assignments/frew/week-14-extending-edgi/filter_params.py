from urllib.parse import urlparse
import pandas as pd
import json
import sys
import os
from surt import handyurl

def alphabetize_params(url):
    o = urlparse(url)
    params = sorted(o.query.split('&'))
    return '&'.join(params)

def filter_timemap(timemap):
    try:
        jso = pd.read_json(timemap)
    except:
        return ""
    
    urif = alphabetize_params(jso.loc['first']['original_uri'])
    
    mementos = jso.loc['list']['mementos']
    mementos2 = []
    for memento in mementos:
        uric = alphabetize_params(memento['uri'])
        if uric == urif:
            mementos2.append(memento)
    
    if len(mementos2) == 0:
        return ""
    
    json2 = {}
    json2['original_url'] = jso.loc['first']['original_uri']
    json2['self'] = jso.loc['first']['self']
    json2['mementos'] = {}
    json2['mementos']['list'] = mementos2
    json2['mementos']['first'] = mementos2[0]
    json2['mementos']['last'] = mementos2[-1]
    json2['timemap_uri'] = {}
    
    prefix = json2['self'].replace('json/' + json2['original_url'], '')
    json2['timemap_uri']['link_format'] = prefix + 'link/' + json2['original_url']
    json2['timemap_uri']['json_format'] = json2['self']
    json2['timemap_uri']['cdxj_format'] = prefix + 'cdxj/' + json2['original_url']
    json2['timegate_uri'] = jso.loc['first']['timegate_uri']
    
    return json.dumps(json2, indent = 2)

i = 1
query_urirs = []
with open('get_timemaps.txt') as urls:
  for line in urls:
        urir = handyurl.parse(line.strip()).geturl()
        if '?' in urir or '&' in urir:
            url_form = '{:0>5}'.format(i) + '.json'
            query_urirs.append(url_form)
        i = i + 1

original_stdout = sys.stdout
x = 1

for timemap in os.listdir('timemaps'+ str(x)):
  #timemap = '00051.json'
  if timemap in query_urirs:
    tmap2 = filter_timemap("timemaps" + str(x) + "/" + timemap)
    with open("filtered-timemaps/" + timemap, 'w') as f:
      sys.stdout = f # Change the standard output to the file we created.
      if tmap2:
          print(tmap2)
      sys.stdout = original_stdout # Reset the standard output to its original value

    