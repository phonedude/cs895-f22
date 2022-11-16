import pandas as pd
#import numpy as np

urls = pd.read_csv('counted_urls.txt')

for i, url in urls.iterrows():
    #print(url['captured url - 0'])
    #print(url['final captured url - t'])
    if pd.isna(urls.iloc[i,2]) or pd.isna(urls.iloc[i,5]):
        print(url['url - o'])
    #if i > 1000:
    #    break