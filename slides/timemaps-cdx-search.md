# An API Primer for Web Archives

In these examples we'll use [@SputnikNewsUS](https://twitter.com/SputnikNewsUS), which is no longer on the live web.  This account was for the US version of [Sputnik](https://en.wikipedia.org/wiki/Sputnik_(news_agency)), a Russian state-affiliated news outlet.  Note that other accounts, like [@SputnikInt](https://twitter.com/@SputnikInt), still exist.

## Memento TimeGates and TimeMaps

Memento operates on the granularity of complete URIs and does not support a search function with wildcards.  

To redirect via a TimeGate to the latest copy via IA's Memento TimeGate (no Accept-Datetime value defaults to the most recent archived version):

```
curl -I https://web.archive.org/web/https://twitter.com/SputnikNewsUS
HTTP/2 302 
server: nginx/1.15.8
date: Thu, 01 Oct 2020 14:47:59 GMT
content-type: text/plain; charset=utf-8
content-length: 0
x-archive-redirect-reason: found capture at 20190909021456
location: https://web.archive.org/web/20190909021456/https://twitter.com/SputnikNewsUS
server-timing: exclusion.robots;dur=0.319822, CDXLines.iter;dur=42.558700, exclusion.robots.policy;dur=0.299640, RedisCDXSource;dur=5.515767, PetaboxLoader3.resolve;dur=218.289064, captures_list;dur=558.760971, PetaboxLoader3.datanode;dur=166.256127, esindex;dur=0.021259, LoadShardBlock;dur=450.095835
x-app-server: wwwb-app43
x-ts: 302
x-location: All
x-cache-key: httpsweb.archive.org/web/https://twitter.com/SputnikNewsUSUS
x-page-cache: MISS
x-archive-screenname: 0
```

To redirect to the version closest to 2016-07-09:

```
curl -I -H "Accept-Datetime: Sat, 09 Jul 2016 00:00:00 GMT" https://web.archive.org/web/https://twitter.com/SputnikNewsUS
HTTP/2 302 
server: nginx/1.15.8
date: Thu, 01 Oct 2020 14:50:34 GMT
content-type: text/plain; charset=utf-8
content-length: 0
x-archive-redirect-reason: found capture at 20160717053407
location: https://web.archive.org/web/20160717053407/https://twitter.com/SputnikNewsUS
vary: accept-datetime
link: <https://twitter.com/SputnikNewsUS>; rel="original", <https://web.archive.org/web/20160717053407/https://twitter.com/SputnikNewsUS>; rel="memento"; datetime="Sun, 17 Jul 2016 05:34:07 GMT", <https://web.archive.org/web/timemap/link/https://twitter.com/SputnikNewsUS>; rel="timemap"; type="application/link-format"
server-timing: CDXLines.iter;dur=28.929049, esindex;dur=0.015949, RedisCDXSource;dur=730.270472, exclusion.robots.policy;dur=0.164821, captures_list;dur=2053.976284, exclusion.robots;dur=0.176671, PetaboxLoader3.resolve;dur=369.631420, PetaboxLoader3.datanode;dur=600.823699, LoadShardBlock;dur=1262.924289
x-app-server: wwwb-app56
x-ts: 302
x-location: All
x-cache-key: httpsweb.archive.org/web/https://twitter.com/SputnikNewsUSSat, 09 Jul 2016 00:00:00 GMTUS
x-page-cache: MISS
x-archive-screenname: 0
```

To retrieve a TimeMap from IA (note only the first 10 lines are shown via the `head` command):

```
curl -s https://web.archive.org/web/timemap/link/https://twitter.com/SputnikNewsUS | head -10
<https://twitter.com/SputnikNewsUS>; rel="original",
<https://web.archive.org/web/timemap/link/https://twitter.com/SputnikNewsUS>; rel="self"; type="application/link-format"; from="Wed, 03 Dec 2014 23:45:50 GMT",
<https://web.archive.org>; rel="timegate",
<https://web.archive.org/web/20141203234550/https://twitter.com/SputnikNewsUS>; rel="first memento"; datetime="Wed, 03 Dec 2014 23:45:50 GMT",
<https://web.archive.org/web/20141216130302/http://twitter.com/SputnikNewsUS>; rel="memento"; datetime="Tue, 16 Dec 2014 13:03:02 GMT",
<https://web.archive.org/web/20141216130304/https://twitter.com/SputnikNewsUS>; rel="memento"; datetime="Tue, 16 Dec 2014 13:03:04 GMT",
<https://web.archive.org/web/20141220182702/https://twitter.com/SputnikNewsUS>; rel="memento"; datetime="Sat, 20 Dec 2014 18:27:02 GMT",
<https://web.archive.org/web/20141228222618/https://twitter.com/SputnikNewsUS>; rel="memento"; datetime="Sun, 28 Dec 2014 22:26:18 GMT",
<https://web.archive.org/web/20141231233757/http://twitter.com:80/SputnikNewsUS>; rel="memento"; datetime="Wed, 31 Dec 2014 23:37:57 GMT",
<https://web.archive.org/web/20150109163639/https://twitter.com/SputnikNewsUS>; rel="memento"; datetime="Fri, 09 Jan 2015 16:36:39 GMT",
```

Using `grep` and `wc`, we can find out how many mementos in the IA's TimeMap:

```
curl -s https://web.archive.org/web/timemap/link/https://twitter.com/SputnikNewsUS | grep "rel=.*memento" | wc -l
73
```

But IA is not the only archive.  archive.is has one copy in its TimeMap:

```
curl https://archive.is/timemap/https://twitter.com/SputnikNewsUS
<https://twitter.com/SputnikNewsUS>; rel="original",
<http://archive.md/timegate/https://twitter.com/SputnikNewsUS>; rel="timegate",
<http://archive.md/20150531154001/https://twitter.com/SputnikNewsUS>; rel="first last memento"; datetime="Sun, 31 May 2015 15:40:01 GMT",
<http://archive.md/timemap/https://twitter.com/SputnikNewsUS>; rel="self"; type="application/link-format"; from="Sun, 31 May 2015 15:40:01 GMT"; until="Sun, 31 May 2015 15:40:01 GMT"
```

And here is a request to [MemGator](http://memgator.cs.odu.edu/), which aggregates access to 16 different public web archives:

```
curl -s http://memgator.cs.odu.edu/timemap/link/https://twitter.com/SputnikNewsUS | head 
<https://twitter.com/SputnikNewsUS>; rel="original",
<https://memgator.cs.odu.edu/timemap/link/https://twitter.com/SputnikNewsUS>; rel="self"; type="application/link-format",
<https://wayback.archive-it.org/all/20141203234550/https://twitter.com/SputnikNewsUS>; rel="first memento"; datetime="Wed, 03 Dec 2014 23:45:50 GMT",
<https://web.archive.org/web/20141203234550/https://twitter.com/SputnikNewsUS>; rel="memento"; datetime="Wed, 03 Dec 2014 23:45:50 GMT",
<https://wayback.archive-it.org/all/20141216130302/http://twitter.com/SputnikNewsUS>; rel="memento"; datetime="Tue, 16 Dec 2014 13:03:02 GMT",
<https://web.archive.org/web/20141216130302/http://twitter.com/SputnikNewsUS>; rel="memento"; datetime="Tue, 16 Dec 2014 13:03:02 GMT",
<https://wayback.archive-it.org/all/20141216130304/https://twitter.com/SputnikNewsUS>; rel="memento"; datetime="Tue, 16 Dec 2014 13:03:04 GMT",
<https://web.archive.org/web/20141216130304/https://twitter.com/SputnikNewsUS>; rel="memento"; datetime="Tue, 16 Dec 2014 13:03:04 GMT",
<https://wayback.archive-it.org/all/20141220182702/https://twitter.com/SputnikNewsUS>; rel="memento"; datetime="Sat, 20 Dec 2014 18:27:02 GMT",
<https://web.archive.org/web/20141220182702/https://twitter.com/SputnikNewsUS>; rel="memento"; datetime="Sat, 20 Dec 2014 18:27:02 GMT",
```

This request shows only the versions *not* at the IA (`grep datetime` selects only memento lines (no `rel="self"` etc. lines), and `grep -v web.archive.org` filters out IA mementos):

```
curl -s http://memgator.cs.odu.edu/timemap/link/https://twitter.com/SputnikNewsUS | grep datetime | grep -v web.archive.org | head
<https://wayback.archive-it.org/all/20141203234550/https://twitter.com/SputnikNewsUS>; rel="first memento"; datetime="Wed, 03 Dec 2014 23:45:50 GMT",
<https://wayback.archive-it.org/all/20141216130302/http://twitter.com/SputnikNewsUS>; rel="memento"; datetime="Tue, 16 Dec 2014 13:03:02 GMT",
<https://wayback.archive-it.org/all/20141216130304/https://twitter.com/SputnikNewsUS>; rel="memento"; datetime="Tue, 16 Dec 2014 13:03:04 GMT",
<https://wayback.archive-it.org/all/20141220182702/https://twitter.com/SputnikNewsUS>; rel="memento"; datetime="Sat, 20 Dec 2014 18:27:02 GMT",
<https://wayback.archive-it.org/all/20141228222618/https://twitter.com/SputnikNewsUS>; rel="memento"; datetime="Sun, 28 Dec 2014 22:26:18 GMT",
<https://wayback.archive-it.org/all/20150109163639/https://twitter.com/SputnikNewsUS>; rel="memento"; datetime="Fri, 09 Jan 2015 16:36:39 GMT",
<https://wayback.archive-it.org/all/20150413074447/https://twitter.com/SputnikNewsUS>; rel="memento"; datetime="Mon, 13 Apr 2015 07:44:47 GMT",
<https://wayback.archive-it.org/all/20150513075443/https://twitter.com/SputnikNewsUS>; rel="memento"; datetime="Wed, 13 May 2015 07:54:43 GMT",
<http://archive.md/20150531154001/https://twitter.com/SputnikNewsUS>; rel="memento"; datetime="Sun, 31 May 2015 15:40:01 GMT",
<https://wayback.archive-it.org/all/20150807052214/https://twitter.com/SputnikNewsUS>; rel="memento"; datetime="Fri, 07 Aug 2015 05:22:14 GMT",
```

This request shows how many copies are in which archives:

```
curl -s http://memgator.cs.odu.edu/timemap/link/https://twitter.com/SputnikNewsUS | grep datetime | awk '{print $1}' | awk -v FS=/ '{print $3}' | sort | uniq -c | sort -n
      1 archive.md
      1 www.webarchive.org.uk
     27 wayback.archive-it.org
     73 web.archive.org
```

Note that MemGator supports other formats, such as json:

```
curl -s http://memgator.cs.odu.edu/timemap/json/https://twitter.com/SputnikNewsUS | head -17
{
  "original_uri": "https://twitter.com/SputnikNewsUS",
  "self": "https://memgator.cs.odu.edu/timemap/json/https://twitter.com/SputnikNewsUS",
  "mementos": {
    "list": [
      {
        "datetime": "2014-12-03T23:45:50Z",
        "uri": "https://wayback.archive-it.org/all/20141203234550/https://twitter.com/SputnikNewsUS"
      },
      {
        "datetime": "2014-12-03T23:45:50Z",
        "uri": "https://web.archive.org/web/20141203234550/https://twitter.com/SputnikNewsUS"
      },
      {
        "datetime": "2014-12-16T13:03:02Z",
        "uri": "https://wayback.archive-it.org/all/20141216130302/http://twitter.com/SputnikNewsUS"
      },
```


## CDX API

Memento TimeGates and TimeMaps only work on full URIs and do not support wild card searching.  This can be a problem with Twitter, which [supports multiple languages via arguments](https://ws-dl.blogspot.com/2019/03/2019-03-18-cookie-violations-cause.html) (e.g., `?lang=ru`).  Technically, these are different URIs, even though they produce the same results:

```
https://twitter.com/SputnikNewsUS
```

and 

```
https://twitter.com/SputnikNewsUS?lang=en
```

Since the individual web archives do not know to canonicalize the two above URIs into a single URI, they are indexed differently, leading to different TimeMaps.  In fact, Twitter has support for 47 different languages, meaning we have to dereference many different TimeMap URIs to find all the copies:

```
curl -s "http://memgator.cs.odu.edu/timemap/link/https://twitter.com/SputnikNewsUS" | grep datetime | wc -l
102
curl -s "http://memgator.cs.odu.edu/timemap/link/https://twitter.com/SputnikNewsUS?lang=en" | grep datetime | wc -l
7
curl -s "http://memgator.cs.odu.edu/timemap/link/https://twitter.com/SputnikNewsUS?lang=fr" | grep datetime | wc -l
6
curl -s "http://memgator.cs.odu.edu/timemap/link/https://twitter.com/SputnikNewsUS?lang=de" | grep datetime | wc -l
5
```

Furthermore, deep links to individual Tweets are all but impossible to guess if you don't already have a link for that tweet.  And since @SputnikNewsUS is no longer live, the Twitter API won't help us.  For example, if you did not already know this URI:

```
https://twitter.com/SputnikNewsUS/status/1020522510494789632
```

You would not know to make this request for its TimeMap:

```
curl https://web.archive.org/web/timemap/link/https://twitter.com/SputnikNewsUS/status/1020522510494789632
<https://twitter.com/SputnikNewsUS/status/1020522510494789632>; rel="original",
<https://web.archive.org/web/timemap/link/https://twitter.com/SputnikNewsUS/status/1020522510494789632>; rel="self"; type="application/link-format"; from="Sat, 21 Jul 2018 15:11:49 GMT",
<https://web.archive.org>; rel="timegate",
<https://web.archive.org/web/20180721151149/https://twitter.com/SputnikNewsUS/status/1020522510494789632>; rel="first memento"; datetime="Sat, 21 Jul 2018 15:11:49 GMT",
<https://web.archive.org/web/20180722190624/https://twitter.com/SputnikNewsUS/status/1020522510494789632>; rel="memento"; datetime="Sun, 22 Jul 2018 19:06:24 GMT",
<https://web.archive.org/web/20180723093657/https://twitter.com/SputnikNewsUS/status/1020522510494789632>; rel="memento"; datetime="Mon, 23 Jul 2018 09:36:57 GMT",
<https://web.archive.org/web/20180723210247/https://twitter.com/SputnikNewsUS/status/1020522510494789632>; rel="memento"; datetime="Mon, 23 Jul 2018 21:02:47 GMT",
<https://web.archive.org/web/20180724081409/https://twitter.com/SputnikNewsUS/status/1020522510494789632>; rel="memento"; datetime="Tue, 24 Jul 2018 08:14:09 GMT",
<https://web.archive.org/web/20180724210741/https://twitter.com/SputnikNewsUS/status/1020522510494789632>; rel="memento"; datetime="Tue, 24 Jul 2018 21:07:41 GMT",
<https://web.archive.org/web/20180725214008/https://twitter.com/SputnikNewsUS/status/1020522510494789632>; rel="memento"; datetime="Wed, 25 Jul 2018 21:40:08 GMT",
<https://web.archive.org/web/20180726094059/https://twitter.com/SputnikNewsUS/status/1020522510494789632>; rel="memento"; datetime="Thu, 26 Jul 2018 09:40:59 GMT",
<https://web.archive.org/web/20180818090236/https://twitter.com/SputnikNewsUS/status/1020522510494789632>; rel="memento"; datetime="Sat, 18 Aug 2018 09:02:36 GMT",
```

Fortunately, 1) Twitter builds its URIs left-to-right, and 2) the IA CDX API supports a "prefix" search.  Here's a query to the IA CDX API, looking for deep links (i.e., with `status` in the URI):

```
curl -s "http://web.archive.org/cdx/search/cdx?url=https://twitter.com/SputnikNewsUS&matchType=prefix" | grep status | head -10
com,twitter)/sputniknewsus/status/1003746968508731394 20180604211500 https://twitter.com/SputnikNewsUS/status/1003746968508731394 application/json - X2H6DAZULNEZH47OFUXYOGXYEE2CNTNI 1665
com,twitter)/sputniknewsus/status/1004120685155844097 20180605220001 https://twitter.com/SputnikNewsUS/status/1004120685155844097 application/json - PVEEB322COQSVHJXUWMWGWTOCAJS53HT 1592
com,twitter)/sputniknewsus/status/1005200294840373249 20180608213000 https://twitter.com/SputnikNewsUS/status/1005200294840373249 application/json - VOD4ZTVTXWVFJGEJTLWYQBHYFDU74HI5 1600
com,twitter)/sputniknewsus/status/1007884228946776064 20180616071944 http://twitter.com/SputnikNewsUS/status/1007884228946776064 unk 301 3I42H3S6NNFQ2MSVX7XZKYAYSCX5QBYJ 452
com,twitter)/sputniknewsus/status/1007884228946776064 20180616071945 https://twitter.com/SputnikNewsUS/status/1007884228946776064 text/html 200 KCNLECFYWHP234OZCH3USGRSAHMYOUMB 42576
com,twitter)/sputniknewsus/status/1014056148289241088 20180703080000 https://twitter.com/SputnikNewsUS/status/1014056148289241088 application/json - BGA6NUORC6TAOCSJZ2FONHJVQTFVXLUG 1670
com,twitter)/sputniknewsus/status/1014056148289241088 20180703080000 https://twitter.com/SputnikNewsUS/status/1014056148289241088 application/json - BGA6NUORC6TAOCSJZ2FONHJVQTFVXLUG 1670
com,twitter)/sputniknewsus/status/1017513932490182657 20180712210000 https://twitter.com/SputnikNewsUS/status/1017513932490182657 application/json - XYB7BJZ6IFOZMR35F5FY3XFUHVITDKWI 1546
com,twitter)/sputniknewsus/status/1017929168602923008 20180714003000 https://twitter.com/SputnikNewsUS/status/1017929168602923008 application/json - NRDJJYZHQYEHG4GUHCWBN63JI7MP2QAT 1559
com,twitter)/sputniknewsus/status/1017929168602923008 20180714003000 https://twitter.com/SputnikNewsUS/status/1017929168602923008 application/json - NRDJJYZHQYEHG4GUHCWBN63JI7MP2QAT 1559
```

This returns raw [CDX format](https://iipc.github.io/warc-specifications/specifications/cdx-format/cdx-2015/), which is sometimes desirable, but sometimes you just want a clickable URI-M.  The following command converts the CDX format into URI-Ms (and this time showing the *last* 30 entries via the `tail` command):

```
curl -s "http://web.archive.org/cdx/search/cdx?url=https://twitter.com/SputnikNewsUS&matchType=prefix" | awk '{print "https://web.archive.org/web/" $2 "/" $3};' | tail -30
https://web.archive.org/web/20141216130353/https://twitter.com/sputniknewsus?lang=th
https://web.archive.org/web/20150124113106/https://twitter.com/sputniknewsus?lang=th
https://web.archive.org/web/20150425130739/https://twitter.com/sputniknewsus?lang=th
https://web.archive.org/web/20150811111010/https://twitter.com/sputniknewsus?lang=th
https://web.archive.org/web/20190528162343/https://twitter.com/SputnikNewsUS?lang=th
https://web.archive.org/web/20190528162343/https://twitter.com/SputnikNewsUS?lang=th
https://web.archive.org/web/20141216130324/https://twitter.com/sputniknewsus?lang=tr
https://web.archive.org/web/20150124113037/https://twitter.com/sputniknewsus?lang=tr
https://web.archive.org/web/20150427081220/https://twitter.com/sputniknewsus?lang=tr
https://web.archive.org/web/20150811114611/https://twitter.com/sputniknewsus?lang=tr
https://web.archive.org/web/20190528162331/https://twitter.com/SputnikNewsUS?lang=tr
https://web.archive.org/web/20141216130354/https://twitter.com/sputniknewsus?lang=uk
https://web.archive.org/web/20150124113108/https://twitter.com/sputniknewsus?lang=uk
https://web.archive.org/web/20150811115142/https://twitter.com/sputniknewsus?lang=uk
https://web.archive.org/web/20190528162349/https://twitter.com/SputnikNewsUS?lang=uk
https://web.archive.org/web/20141216130351/https://twitter.com/sputniknewsus?lang=ur
https://web.archive.org/web/20150124113105/https://twitter.com/sputniknewsus?lang=ur
https://web.archive.org/web/20150811112651/https://twitter.com/sputniknewsus?lang=ur
https://web.archive.org/web/20141216130407/https://twitter.com/sputniknewsus?lang=vi
https://web.archive.org/web/20150124113121/https://twitter.com/sputniknewsus?lang=vi
https://web.archive.org/web/20150811113533/https://twitter.com/sputniknewsus?lang=vi
https://web.archive.org/web/20190528162332/https://twitter.com/SputnikNewsUS?lang=vi
https://web.archive.org/web/20141216130336/https://twitter.com/sputniknewsus?lang=zh-cn
https://web.archive.org/web/20150124113048/https://twitter.com/sputniknewsus?lang=zh-cn
https://web.archive.org/web/20150811114306/https://twitter.com/sputniknewsus?lang=zh-cn
https://web.archive.org/web/20190528162355/https://twitter.com/SputnikNewsUS?lang=zh-cn
https://web.archive.org/web/20141216130332/https://twitter.com/sputniknewsus?lang=zh-tw
https://web.archive.org/web/20150124113046/https://twitter.com/sputniknewsus?lang=zh-tw
https://web.archive.org/web/20150811110151/https://twitter.com/sputniknewsus?lang=zh-tw
https://web.archive.org/web/20190528162425/https://twitter.com/SputnikNewsUS?lang=zh-tw
```

Here's a command for just the deep links (i.e., with `status` in the URIs):

```
curl -s "http://web.archive.org/cdx/search/cdx?url=https://twitter.com/SputnikNewsUS/status&matchType=prefix" | awk '{print "https://web.archive.org/web/" $2 "/" $3};' | head
https://web.archive.org/web/20180604211500/https://twitter.com/SputnikNewsUS/status/1003746968508731394
https://web.archive.org/web/20180605220001/https://twitter.com/SputnikNewsUS/status/1004120685155844097
https://web.archive.org/web/20180608213000/https://twitter.com/SputnikNewsUS/status/1005200294840373249
https://web.archive.org/web/20180616071944/http://twitter.com/SputnikNewsUS/status/1007884228946776064
https://web.archive.org/web/20180616071945/https://twitter.com/SputnikNewsUS/status/1007884228946776064
https://web.archive.org/web/20180703080000/https://twitter.com/SputnikNewsUS/status/1014056148289241088
https://web.archive.org/web/20180703080000/https://twitter.com/SputnikNewsUS/status/1014056148289241088
https://web.archive.org/web/20180712210000/https://twitter.com/SputnikNewsUS/status/1017513932490182657
https://web.archive.org/web/20180714003000/https://twitter.com/SputnikNewsUS/status/1017929168602923008
https://web.archive.org/web/20180714003000/https://twitter.com/SputnikNewsUS/status/1017929168602923008
```

In the above, we have two different copies of the tweet id `1007884228946776064`, archived just one second apart.  That might not be what we want.  This command sorts and uniques on the tweet id (CDX key=3) so we only get one copy, then transforms into URI-Ms:

```
curl -s "http://web.archive.org/cdx/search/cdx?url=https://twitter.com/SputnikNewsUS/status&matchType=prefix" | sort -u -k 3 | awk '{print "https://web.archive.org/web/" $2 "/" $3};' | head
https://web.archive.org/web/20180604211500/https://twitter.com/SputnikNewsUS/status/1003746968508731394
https://web.archive.org/web/20180605220001/https://twitter.com/SputnikNewsUS/status/1004120685155844097
https://web.archive.org/web/20180608213000/https://twitter.com/SputnikNewsUS/status/1005200294840373249
https://web.archive.org/web/20180616071945/https://twitter.com/SputnikNewsUS/status/1007884228946776064
https://web.archive.org/web/20180703080000/https://twitter.com/SputnikNewsUS/status/1014056148289241088
https://web.archive.org/web/20180712210000/https://twitter.com/SputnikNewsUS/status/1017513932490182657
https://web.archive.org/web/20180714003000/https://twitter.com/SputnikNewsUS/status/1017929168602923008
https://web.archive.org/web/20180720043000/https://twitter.com/SputnikNewsUS/status/1020163893765734400
https://web.archive.org/web/20180720050000/https://twitter.com/SputnikNewsUS/status/1020171443542339585
https://web.archive.org/web/20180818091851/https://twitter.com/SputnikNewsUS/status/1020401709993078786
```

This command sorts and unqiues on status id, then resorts on Memento-Datetime (key=2), so the URI-Ms are arranged in chronological order:

```
curl -s "http://web.archive.org/cdx/search/cdx?url=https://twitter.com/SputnikNewsUS/status&matchType=prefix" | sort -u -k 3 | sort -k 2 | awk '{print "https://web.archive.org/web/" $2 "/" $3};' | head
https://web.archive.org/web/20141203234552/https://twitter.com/SputnikNewsUS/status/537301020997873664
https://web.archive.org/web/20141204040305/https://twitter.com/SputnikNewsUS/status/537391233141059584
https://web.archive.org/web/20141204050148/https://twitter.com/SputnikNewsUS/status/537302466648608768
https://web.archive.org/web/20141220182712/https://twitter.com/SputnikNewsUS/status/546358360204128257
https://web.archive.org/web/20141220182714/https://twitter.com/SputnikNewsUS/status/546358360204128257?screen_name=SputnikNewsUS&id=546358360204128257
https://web.archive.org/web/20141220182717/https://twitter.com/sputniknewsus/status/546358360204128257?screen_name=SputnikNewsUS&id=546358360204128257&lang=en
https://web.archive.org/web/20141220182718/https://twitter.com/sputniknewsus/status/546358360204128257?screen_name=SputnikNewsUS&id=546358360204128257&lang=en-gb
https://web.archive.org/web/20141221001633/https://twitter.com/SputnikNewsUS/status/546051957627305984
https://web.archive.org/web/20141221001634/https://twitter.com/SputnikNewsUS/status/546047732771983360
https://web.archive.org/web/20141221001636/https://twitter.com/SputnikNewsUS/status/546043993105391616
```

Note some of the additional arguments (`screen_name` and `lang`) that appear for tweet id `546358360204128257`.  If you don't want those to be considered, use `sed` to strip off the URI arguments while still in the CDX format and then process as above:

```
curl -s "http://web.archive.org/cdx/search/cdx?url=https://twitter.com/SputnikNewsUS/status&matchType=prefix" | sed 's/?.*//' | sort -u -k 3 | sort -k 2 | awk '{print "https://web.archive.org/web/" $2 "/" $3};' | head 
https://web.archive.org/web//
https://web.archive.org/web/20141203234552/https://twitter.com/SputnikNewsUS/status/537301020997873664
https://web.archive.org/web/20141204040305/https://twitter.com/SputnikNewsUS/status/537391233141059584
https://web.archive.org/web/20141204050148/https://twitter.com/SputnikNewsUS/status/537302466648608768
https://web.archive.org/web/20141220182712/https://twitter.com/SputnikNewsUS/status/546358360204128257
https://web.archive.org/web/20141221001633/https://twitter.com/SputnikNewsUS/status/546051957627305984
https://web.archive.org/web/20141221001634/https://twitter.com/SputnikNewsUS/status/546047732771983360
https://web.archive.org/web/20141221001636/https://twitter.com/SputnikNewsUS/status/546043993105391616
https://web.archive.org/web/20141221001637/https://twitter.com/SputnikNewsUS/status/546042786848706560
https://web.archive.org/web/20141221001638/https://twitter.com/SputnikNewsUS/status/546041062943649792
```

Note the `https://web.archive.org/web//` entry above -- I think this snuck in because the CDX file has some malformed URI entries.  Or it could be that I've made some bad assumptions about all the lines in the CDX formats or applied an overly aggressive regular expression.  Rather than chase down the culprit, I'll leave it as a cautionary tale.  


## archive.is URI search

Note that archive.is has a similar prefix search, though I'm unsure if they support a machine readable (e.g., link or json format) of these URIs:

[http://archive.is/https://twitter.com/SputnikNewsUS*](http://archive.is/https://twitter.com/SputnikNewsUS*)

[http://archive.is/https://twitter.com/SputnikNewsUS/status/*](http://archive.is/https://twitter.com/SputnikNewsUS/status/*)
`
