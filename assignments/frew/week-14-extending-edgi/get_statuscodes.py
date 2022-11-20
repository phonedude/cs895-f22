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
      wrv2016 = ''
      wrv2020 = ''

      for line in text_arr:
          data = line.split(" ")
          if len(data) < 4:
              continue
          if data[1] == dt1:
              if data[4] == '-':
                  st1.append(data[4])
                  wrv2016 = data[5]
              else:
                  st1.append(data[4])
          elif data[1] == dt2:
              if data[4] == '-':
                  st2.append(data[4])
                  wrv2020 = data[5]
              else:
                  st2.append(data[4])
          #data[4] status code
          #data[1] datetime
              
      if wrv2016 or wrv2020:
          for line in text_arr:
              data = line.split(" ")
              if len(data) < 4:
                  continue
              if wrv2016 and data[4] != '-' and data[5] == wrv2016:
                  st1.append(data[4])
                  if not wrv2020:
                      break
                  wrv2016 = ''
              if wrv2020 and data[4] != '-' and data[5] == wrv2020:
                  st2.append(data[4])
                  if not wrv2016:
                      break
                  wrv2020 = ''
              if not wrv2016 and not wrv2020:
                  break
      
      print(url.strip(),','.join(st1), ','.join(st2))
      
      #i = i + 1
      
      #if i > 50:
      #    break