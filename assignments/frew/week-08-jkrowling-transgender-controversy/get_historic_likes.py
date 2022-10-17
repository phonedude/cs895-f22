# get_historic_likes.py
#   Input: a timemap of a tweet
#   Output: redirect to a file, CSV format for historic tweet likes
# Lesley Frew
# October 5, 2022
# 1. Run memgator in JSON format to generate timemap.json
#    memgator-windows-amd64 --format=JSON https://twitter.com/jk_rowling/status/1207646162813100033 > timemap.json
# 2. Run get_historic_likes.py and redirect to a file

import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
import pandas as pd

jso = pd.read_json('timemap.json')
print ('memento-datetime,likes')

for memento in reversed(jso.loc['list']['mementos']):
  urim = memento['uri']
  
  #need tweet id for 2022 layout scraping
  urim2 = re.sub(r".*/status/","", urim)
  tweet_id = re.sub(r"[^0-9].*$", "", urim2)
  
  #get the http response for each memento
  try:
    resp = requests.get(urim)
  except:
    continue
  if 'memento-datetime' not in resp.headers:
    continue
    
  #Re-format memento-datetime - code from Shawn Jones/Hypercane
  mdt_date = datetime.strptime(resp.headers['memento-datetime'], 
                          "%a, %d %b %Y %H:%M:%S GMT")
  mdt = mdt_date.strftime('%Y-%m-%dT%H:%M:%SZ')
  
  #get the HTML tree for each memento
  soup = BeautifulSoup(resp.text, features="lxml")
  
  #Try both the 2022 layout and pre-2022 layout to scrape likes
  found_count = False
  for div in soup.find_all('div'):
    #2022 layout
    if 'itemtype' in div.attrs and div['itemtype'] == 'https://schema.org/InteractionCounter':
        if len(div.contents) > 3:
            child = div.contents[0]
            if child.name == 'meta' and 'content' in child.attrs and child['content'] == 'https://schema.org/LikeAction':
                child2 = div.contents[1]
                if 'content' in child2.attrs and child2['content'] == 'Likes':
                    child3 = div.contents[2]
                    if 'content' in child3.attrs and tweet_id in child3['content']:
                        child4 = div.contents[3]
                        if 'content' in child4.attrs:
                            print(mdt + "," + child4['content'])
                            found_count = True
  if not found_count:
    for ul in soup.find_all('ul'):
      #pre-2022 layout - English only
      if 'aria-label' in ul.attrs and ul['aria-label'] == 'Retweeted and favorited by':
        for li in ul.contents:
            if li is None:
              continue
            li2 = str(li).replace("\n", "")
            if 'likes' in li2 and 'data-tweet-stat-count' in li2:
              #This did not parse into beautifulsoup as its own element
              #Remove everything but the numeric like value
              dtsc = re.sub(".*data-tweet-stat-count=\"", "", li2)
              dtsc = re.sub("[^0-9].*$", "", dtsc)
              print(mdt + "," + dtsc)
              found_count = True
    
