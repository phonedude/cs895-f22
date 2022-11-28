def calc_code(codeline):
      codearr = codeline.split(',')
      while '-' in codearr:
          codearr.remove("-")
      codemerge = ','.join(codearr)
      codekey = codemerge
      if ',' in codemerge:
         #2020: {'200,301': 6, '301,301': 1, '301,404': 2, '200,302': 1, '301,200': 5, '200,200': 3, '302,200': 2}
         #2016: {'301,200': 376, '200,301': 6, '200,200': 57, '301,301,200,200': 4, '301,301': 3, '301,200,302': 3, '301,301,200,200,302,302': 2, '200,302': 10, '200,200,302,302': 2, '302,200': 21, '301,200,301': 1, '307,200': 114}
         if '200' in codemerge:
             codekey = '200'
         elif '404' in codemerge:
             codekey = '404'
         else:
             codekey = '301'
         #codect.setdefault(codemerge, 0)
         #codect[codemerge] = codect[codemerge] + 1
      return codekey

codect = {}

with open('statc_merge.txt') as codes:
  for line in codes:
      linespl = line.split()
      if len(linespl) < 5:
          continue
      codekey16 = calc_code(linespl[3])
      codekey20 = calc_code(linespl[4])
      codekey = codekey16 + "," + codekey20
      
      codect.setdefault(codekey, 0)
      codect[codekey] = codect[codekey] + 1

print(codect)

#{'200,301': 2004, '200,200': 7399, '200,404': 397, ',301': 28, '302,301': 5, '404,301': 14, ',200': 16, '200,302': 779, '302,200': 3, '301,200': 9, '301,301': 63, '301,404': 3, ',302': 6, '200,403': 14, '200,303': 1, '200,': 4, '301,302': 3, '302,404': 1, '200,500': 7, '200,503': 1, '302,302': 9, '404,404': 1, '307,301': 4}
