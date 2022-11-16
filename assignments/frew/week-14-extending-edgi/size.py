import os

count = 0

for x in range(0,3):
  for timemap in os.listdir('timemaps' + str(x)):
    if os.path.getsize("timemaps" + str(x) + "/" + timemap) == 0:
        count = count + 1
print(count)
#1706