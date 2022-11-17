import requests


#i = 1
with open('get_statuscodes.txt') as urls:
  
  for url in urls:
  
      linespt = url.split()

      urir = linespt[0]
      dt1 = linespt[1]
      dt2 = linespt[2]

      res = requests.get('https://web.archive.org/cdx/search/cdx?url=' + urir) #&showResumeKey=true
      text = res.text
      text_arr = text.split("\n")

      st1 = []
      st2 = []
      prevst = ''

      for line in text_arr:
          data = line.split(" ")
          if len(data) < 4:
              continue
          if data[1] == dt1:
              if data[4] == '-':
                  st1.append(data[4] + ":" + prevst)
              else:
                  st1.append(data[4])
          elif data[1] == dt2:
              if data[4] == '-':
                  st2.append(data[4] + ":" + prevst)
              else:
                  st2.append(data[4])
          #data[4] status code
          #data[1] datetime
          if data[4] != '-' and data[4] != '302':
              prevst = data[4]
      print(url.strip(),','.join(st1), ','.join(st2))
      
      #i = i + 1
      
      #if i > 50:
      #    break