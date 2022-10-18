# J.K. Rowling Transgender-Comments Controversy

## Slides

[CS 895 JKR Transgender Comments Controversy.pdf](CS%20895%20JKR%20Transgender%20Comments%20Controversy.pdf)

## Data and Code

Were 60,000 likes removed from [J.K. Rowling’s tweet about Maya](https://twitter.com/jk_rowling/status/1207646162813100033)? (claim from [Medium.com](https://medium.com/@notCursedE/likes-are-being-removed-from-jk-rowling-s-transphobic-tweet-1fc81e961cd8))

### Extract Historic Like Data

Because the tweet is well archived, historic like data can be extracted from mementos.

* timemap.json - result of running `memgator-windows-amd64 --format=JSON https://twitter.com/jk_rowling/status/1207646162813100033 > timemap.json` on October 5, 2022
* get_historic_likes.py - Input is a timemap, output is a csv with historic like data
* out1.csv - Output of get_historic_likes.py

### Chart Historic Likes

There is no evidence that 60,000 likes were removed from the tweet.

* chart_historic_likes.py - Input is a csv of historic like data, output is a chart of likes over time
* historic_likes.png - Output of running chart_historic_likes.py with out1.csv as input

### Fill in Gap Period

There was a gap period between February 8, 2020 and March 11, 2020 in the original run of the scripts.
The gap period was filled in using prefix memento search and screenshots from Tweets in the gap period.

* cdxout.txt - result of running `curl -s "http://web.archive.org/cdx/search/cdx?url=https://twitter.com/jk_rowling/status/1207646162813100033&matchType=prefix" | awk '{print "https://web.archive.org/web/" $2 "/" $3};' > cdxout.txt`
* cdxout2.txt - result of running `cat cdxout.txt | grep "/20210[23].*[^3]$" | sort > cdxout2.txt`
* gap-tweets-screenshots-list.txt - list of Twitter posts with screenshots containing Like data during the gap period
* out2.csv - historic like data from screenshots, datetime is the time of each tweet containing a screenshot, like count is from screenshot
* out3merge.csv - merge out1.csv and out2.csv
* historic_likes_nogap.png - Output of running chart_historic_likes.py with out3merge.csv as input
