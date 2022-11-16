import subprocess
from surt import handyurl
import os

i = 1
with open('get_timemaps.txt') as urls:
  
  for line in urls:
        urir = handyurl.parse(line.strip()).geturl()
        if '?' in urir or '&' in urir:
            i = i + 1
print(i)
#4646