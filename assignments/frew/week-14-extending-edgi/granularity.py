import subprocess
import pandas as pd
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import re

def dt_obj(mdt):
   mdt = mdt.replace("T", " ")
   mdt = mdt.replace("Z", " ")
   datetime_object = datetime.strptime(mdt, '%Y-%m-%d %H:%M:%S ')
   return datetime_object

def binsearch(mlist, dateobj):
   sidx = 0
   eidx = len(mlist)-1

   cidx = len(mlist) // 2
   curr_date = dt_obj(mlist[cidx]['datetime'])
   while(curr_date != dateobj):
      if (curr_date < dateobj):
         sidx = cidx + 1
      else:
         eidx = cidx - 1
      cidx = (sidx + eidx) // 2
      curr_date = dt_obj(mlist[cidx]['datetime'])
        
   return(cidx)

#https://github.com/edgi-govdata-archiving/web_monitoring_research/blob/main/ctrl-f.py
def extract_body(contents):
   body=contents.find('body')
   d=[s.extract() for s in body('footer')]
   d=[s.extract() for s in body('header')]
   d=[s.extract() for s in body('nav')]
   d=[s.extract() for s in body('script')]
   d=[s.extract() for s in body('style')]
   d=[s.extract() for s in body.select('div > #menuh')] # FWS
   d=[s.extract() for s in body.select('div > #siteFooter')] # FWS
   d=[s.extract() for s in body.select('div.primary-nav')] # DOE
   d=[s.extract() for s in body.select('div > #nav-homepage-header')] # OSHA
   d=[s.extract() for s in body.select('div > #footer-two')] # OSHA
   del d
   body=[text for text in body.stripped_strings]
   return ' '.join(body).replace("\n", " ")
   
def binsearch_delterm(mlist, term, sidx, eidx):
  termre = get_termre(term)
  cidx = (sidx + eidx) // 2
  while(True):
    #to do: refactor when done debugging
    res = requests.get(mlist[cidx]['uri'])
    #print(cidx, res.status_code)
    #to do: if redirect figure that out
    #problem: https://webarchive.loc.gov/all/20170220132206/http://www.esrl.noaa.gov/gmd/obop/thd/
    #it's a soft 302
    text = BeautifulSoup(res.content, 'lxml')
    textbody = extract_body(text)
    y = re.search(termre, textbody)
    if y is not None:
      sidx = cidx + 1
    else:
      eidx = cidx - 1
    cidx2 = (sidx + eidx) // 2
    if cidx2 == cidx:
      cidx = cidx2
      if y is None:
         cidx = cidx - 1
      break
    else:
      cidx = cidx2
        
  #print(cidx)
  print("The term " + term + " was deleted between these two mementos: ")
  print(mlist[cidx])
  print(mlist[cidx + 1])
  #https://web.archive.org/web/diff/20190910181030/20190911183507/https://www.cdc.gov/climateandhealth/

def binsearch_addterm(mlist, term, sidx, eidx):
  termre = get_termre(term)
  y = termsearch(mlist, sidx, termre)
  if y is not None:
    print("The term " + term + " was added in this memento: ")
    print(mlist[sidx])
  else:
    #print('here')
    cidx = (sidx + eidx) // 2
    while(True):
      #to do: refactor when done debugging
      res = requests.get(mlist[cidx]['uri'])
      #print(res.status_code, mlist[cidx]['uri'])
      text = BeautifulSoup(res.content, 'lxml')
      textbody = extract_body(text)
      y = re.search(termre, textbody)
      #print(cidx, y)
      #print(textbody)
      if y is None:
         sidx = cidx + 1
      else:
         eidx = cidx - 1
      cidx2 = (sidx + eidx) // 2
      #print(sidx, eidx, cidx2)
      if cidx2 == cidx:
         cidx = cidx2
         if y is None:
            cidx = cidx + 1
         break
      else:
         cidx = cidx2

    print("The term " + term + " was added in this memento: ")
    print(mlist[cidx])
    
def termsearch(mlist, idx, termre):
  res = requests.get(mlist[idx]['uri'])
  text = BeautifulSoup(res.content, 'lxml')
  textbody = extract_body(text)
  y = re.search(termre, textbody)
  return y
  
def get_termre(term):
  return re.compile(r'\b' + term + r'\b', re.I)

def main():

  #to do parse input
  #urir = 'http://www.cdc.gov/climateandhealth/'
  #start = '2016-04-22 18:30:04 '
  #end = '2020-04-30 02:11:35 '
  #term = 'pollution'
  urir = 'http://www.esrl.noaa.gov/gmd/obop/thd/'
  start = '2016-04-23 15:33:43 '
  end = '2020-04-30 00:50:31 '
  term = 'anthropogenic'
  termre = get_termre(term)

  #to do suppress output
  #f = open('temptimemap.json', "w")
  #subprocess.run(["memgator-windows-amd64.exe", "--format=JSON", urir], stdout=f)

  jso = pd.read_json('temptimemap.json')
  mlist = jso.loc['list']['mementos']


  sdate = dt_obj(start)
  edate = dt_obj(end)

  sidx = binsearch(mlist, sdate)
  sidx_or = sidx
  eidx = binsearch(mlist, edate)

  y1 = termsearch(mlist, sidx, termre)
  y2 = termsearch(mlist, eidx, termre)
  if y1 is not None and y2 is None:
    binsearch_delterm(mlist, term, sidx, eidx)

    eidx = sidx_or
    sidx = 0
    binsearch_addterm(mlist, term, sidx, eidx)
  else:
    print('Input error: term should be present in start memento and absent in end memento')

if __name__ == "__main__":
    main()