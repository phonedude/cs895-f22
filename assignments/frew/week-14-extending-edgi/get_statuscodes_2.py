import requests

with open('get_statuscodes.txt') as urls:
  
  for url in urls:
  
      linespt = url.split()

      urir = linespt[0]

      try:
          res = requests.get('https://web.archive.org/cdx/search/cdx?url=' + urir) #&showResumeKey=true
      except:
          print("error: skipping " + urir)
          continue
      text = res.text
      text_arr = text.split("\n")
      good_2016 = ""
      good_2020 = ""
      bad_2016 = ""
      bad_2020 = ""
      temp_2020 = ""
      for line in text_arr:
          data = line.split(" ")
          if len(data) < 4:
              continue
          line2 = data[1] + ' https://web.archive.org/web/' + data[1] + '/' + data[2] + ' ' + data[4]
          if data[4] == '200':
              if data[1][0:4] == '2016' and not good_2016:
                  good_2016 = line2
              if data[1][0:4] == '2020' and not good_2020:
                  good_2020 = line2
              if good_2016 and good_2020:
                  break
              if data[1][0:4] == '2021':
                  break
          else:
              if data[1][0:4] == '2016' and not bad_2016 and data[4] != '-':
                  bad_2016 = line2
              if data[1][0:4] == '2020' and not bad_2020:
                      if data[4] != '-':
                          bad_2020 = line2
                      elif not temp_2020:
                          temp_2020 = line2

      if not bad_2020:
          bad_2020 = temp_2020

      if good_2016 and good_2020:
          print(urir, good_2016, good_2020)
      else:
          if good_2016:
              print(urir, good_2016, bad_2020)
          elif good_2020:
              print(urir, bad_2016, good_2020)
          else:
              print(urir, bad_2016, bad_2020)