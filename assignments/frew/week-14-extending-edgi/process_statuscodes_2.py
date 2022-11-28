codect = {}

with open('stat_2.txt') as codes:
  for line in codes:
      linespl = line.split()
      if len(linespl) < 7:
          continue
      codekey16 = linespl[3]
      codekey20 = linespl[6]
      codekey = codekey16 + "," + codekey20
      
      codect.setdefault(codekey, 0)
      codect[codekey] = codect[codekey] + 1

print(codect)
#{'200,301': 2025, '200,200': 7350, '200,302': 766, '200,403': 104, '302,301': 17, '302,302': 5, '200,404': 77, '200,503': 176, '301,200': 1, '301,301': 35, '301,503': 2, '200,-': 54, '500,302': 1, '503,302': 1, '301,302': 3, '200,502': 2, '302,200': 1, '404,301': 14, '307,301': 4, '301,-': 1, '301,502': 1}
