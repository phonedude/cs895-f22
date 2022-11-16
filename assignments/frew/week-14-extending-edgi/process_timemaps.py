import os
import pandas as pd
from datetime import datetime

date16 = datetime(2016, 7, 1,  0,  0,  2)
date16begin = datetime(2015,12,31,23,59,59)
date20 = datetime(2020, 7, 1, 0, 0, 2)
date20begin = datetime(2019,12,31,23,59,59)

#for x in range(0,3):
x = 0
for timemap in os.listdir('timemaps'+ str(x)):
    try:
        jso = pd.read_json("timemaps" + str(x) + "/" + timemap)
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
    find20 = []
    for memento in mementos:
        mdate = memento['datetime'].split('-')
        mdt = datetime(int(mdate[0]), int(mdate[1]), int(mdate[2][0:2]),  0,  0,  1)
        if mdt > date16begin and mdt < date16 and len(find16) == 0:
            find16 = memento
        if mdt > date20begin and mdt < date20 and len(find20) == 0:
            find20 = memento  
        if len(find16) > 0 and len(find20) > 0:
            print('{',find16, ',',find20,'},')
            break
    