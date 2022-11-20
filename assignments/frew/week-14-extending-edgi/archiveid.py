from urllib.parse import urlparse
import os
import pandas as pd
from datetime import datetime

def get_archive(urim):
  #url = 'https://web.archive.org/web/20100226083132/http://climate.nasa.gov:80/news/index.cfm?NewsID=271'
  o = urlparse(urim)
  return o.hostname


date16 = datetime(2016, 7, 1,  0,  0,  2)
date16begin = datetime(2015,12,31,23,59,59)
date20 = datetime(2020, 7, 1, 0, 0, 2)
date20begin = datetime(2019,12,31,23,59,59)

#for x in range(0,3):
#x = 2
for timemap in os.listdir('filtered-timemaps'):
#for timemap in os.listdir('timemaps'+ str(x)):
    try:
        #jso = pd.read_json("timemaps" + str(x) + "/" + timemap)
        jso = pd.read_json("filtered-timemaps"+ "/" + timemap)
    except:
        continue #empty timemap
    
    firstd = jso.loc['first']['mementos']['datetime']
    first = firstd.split('-')
    f_date = datetime(int(first[0]), int(first[1]), int(first[2][0:2]),  0,  0,  1)
    if (f_date > date16):
        continue
        
    #print(jso.head())
    mementos = jso.loc['list']['mementos']
    find16 = []
    find16a = 0
    find20 = []
    find20a = 0
    for memento in mementos:
    
        if '?' in memento['uri'] or '&' in memento['uri']:
            break #process separately from filtered folder
    
        mdate = memento['datetime'].split('-')
        mdt = datetime(int(mdate[0]), int(mdate[1]), int(mdate[2][0:2]),  0,  0,  1)
        if mdt > date16begin and mdt < date16:
            if len(find16) == 0:
               find16 = memento
            if get_archive(memento['uri']) == 'web.archive.org' and find16a == 0:
               find16a = find16a + 1
        if mdt > date20begin and mdt < date20:
            if len(find20) == 0:
               find20 = memento
            if get_archive(memento['uri']) == 'web.archive.org' and find20a == 0:
               find20a = find20a + 1
    if find16a == 0 or find20a == 0:
        if len(find16) > 0 and len(find20) > 0:
            #print('{',"'id':","'" + timemap[:-5] + "'",", 'original_uri':","'"+jso.loc['first']['original_uri']+"'",", 'urim_2016':",find16, ", 'urim_2020':",find20,'},')
            print('{',"'id':","'" + timemap[:-5] + "'",", 'original_uri':","'"+jso.loc['first']['original_url']+"'",", 'urim_2016':",find16, ", 'urim_2020':",find20,'},')
            
