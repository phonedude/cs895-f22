import pandas as pd
#import numpy as np
import re

urls = pd.read_csv('counted_urls.txt')

for i, url in urls.iterrows():
    #print(url['captured url - 0'])
    #print(url['final captured url - t'])
    if pd.isna(urls.iloc[i,2]) or pd.isna(urls.iloc[i,5]):
        #print(url['url - o']) #for timemaps
        pass
    else:
        datetime1 = re.match(".*([0-9]{14}).*", url['captured url - 0'])
        datetime2 = re.match(".*([0-9]{14}).*", url['final captured url - t'])
        print(url['url - o'], datetime1.groups()[0], datetime2.groups()[0]) #for status codes
    #if i > 1000:
    #    break