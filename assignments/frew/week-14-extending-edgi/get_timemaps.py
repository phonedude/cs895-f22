import subprocess
from surt import handyurl
import os

i = 1
with open('get_timemaps.txt') as urls:
  
  for line in urls:
      filename = '{:0>5}'.format(i)
      path = 'timemaps' + filename[0] + '/' + filename + '.json'
      
      if not (os.path.isfile(path)):
        urir = handyurl.parse(line.strip()).geturl()
        f = open(path, "w")
        subprocess.run(["memgator-windows-amd64.exe", "--format=JSON", urir], stdout=f, stderr=subprocess.DEVNULL)
        f.close()
        print('wrote timemap ' + line.strip())
      
      i = i + 1