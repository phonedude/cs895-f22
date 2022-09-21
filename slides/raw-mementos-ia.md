# Raw (unwritten) Mementos from IA

Although aproaches for formalizing support for "raw" (or "unwritten" or "original") mementos -- pages with no to minimal transformation -- have been proposed ([separate URL paths](https://ws-dl.blogspot.com/2016/04/2016-04-27-mementos-in-raw.html) or [using the `Prefer` HTTP request header](https://ws-dl.blogspot.com/2016/08/2016-08-15-mementos-in-raw-take-two.html), the window of opportunity may have closed for standardizing these approaches.  Instead, we're left with the conventions established by the Internet Archive's Wayback Machine where the format is concatenated to 14 digit datetime string.  

There are [multiple modifiers](https://iipc.github.io/openwayback/2.1.0.RC.1/administrator_manual.html), but here we'll focus only on the `id_` ("identity") modifier for having the archive return untransformed HTML (no rewritten links, no archival metadata banner).  

## Default playback is tranformed 

Here's a big chunk of a replayed web page:

```
% curl -i https://web.archive.org/web/19971010044705/http://www.dlib.org/dlib/July95/07arms.html
HTTP/2 200 
server: nginx/1.15.8
date: Wed, 07 Oct 2020 17:18:19 GMT
content-type: text/html; charset=utf-8
content-length: 18666
x-archive-orig-date: Fri, 10 Oct 1997 04:49:13 GMT
x-archive-orig-server: Apache/1.1.3
x-archive-orig-content-length: 16459
x-archive-orig-last-modified: Mon, 07 Oct 1996 14:45:49 GMT
x-archive-guessed-content-type: text/html
x-archive-guessed-charset: utf-8
memento-datetime: Fri, 10 Oct 1997 04:47:05 GMT
link: <http://www.dlib.org:80/dlib/July95/07arms.html>; rel="original", <https://web.archive.org/web/timemap/link/http://www.dlib.org:80/dlib/July95/07arms.html>; rel="timemap"; type="application/link-format", <https://web.archive.org/web/http://www.dlib.org:80/dlib/July95/07arms.html>; rel="timegate", <https://web.archive.org/web/19971010044705/http://www.dlib.org:80/dlib/July95/07arms.html>; rel="first memento"; datetime="Fri, 10 Oct 1997 04:47:05 GMT", <https://web.archive.org/web/19971010044705/http://www.dlib.org:80/dlib/July95/07arms.html>; rel="memento"; datetime="Fri, 10 Oct 1997 04:47:05 GMT", <https://web.archive.org/web/19971210081027/http://www.dlib.org:80/dlib/July95/07arms.html>; rel="next memento"; datetime="Wed, 10 Dec 1997 08:10:27 GMT", <https://web.archive.org/web/20200208020611/http://www.dlib.org/dlib/July95/07arms.html>; rel="last memento"; datetime="Sat, 08 Feb 2020 02:06:11 GMT"
content-security-policy: default-src 'self' 'unsafe-eval' 'unsafe-inline' data: blob: archive.org web.archive.org analytics.archive.org pragma.archivelab.org
x-archive-src: FS-195284-c/FS-195470.arc.gz
server-timing: captures_list;dur=649.266491, exclusion.robots.policy;dur=0.177984, RedisCDXSource;dur=10.983081, esindex;dur=0.015423, load_resource;dur=734.353078, PetaboxLoader3.resolve;dur=200.948998, PetaboxLoader3.datanode;dur=1082.751587, CDXLines.iter;dur=21.455310, exclusion.robots;dur=0.192170, LoadShardBlock;dur=608.209326
x-app-server: wwwb-app100
x-ts: 200
x-location: All
x-cache-key: httpsweb.archive.org/web/19971010044705/http://www.dlib.org/dlib/July95/07arms.htmlUS
x-page-cache: MISS
x-archive-screenname: 0

<html>

<head><script src="//archive.org/includes/analytics.js?v=cf34f82" type="text/javascript"></script>
<script type="text/javascript">window.addEventListener('DOMContentLoaded',function(){var v=archive_analytics.values;v.service='wb';v.server_name='wwwb-app100.us.archive.org';v.server_ms=1394;archive_analytics.send_pageview({});});</script><script type="text/javascript" src="/_static/js/playback.bundle.js?v=BsQ6byDz" charset="utf-8"></script>
<script type="text/javascript" src="/_static/js/wombat.js?v=cRqOKCOw" charset="utf-8"></script>
<script type="text/javascript">
  __wm.init("https://web.archive.org/web");
  __wm.wombat("http://www.dlib.org:80/dlib/July95/07arms.html","19971010044705","https://web.archive.org/","web","/_static/",
	      "876458825");
</script>
<link rel="stylesheet" type="text/css" href="/_static/css/banner-styles.css?v=NHuXCfBH" />
<link rel="stylesheet" type="text/css" href="/_static/css/iconochive.css?v=qtvMKcIJ" />
<!-- End Wayback Rewrite JS Include -->


<meta name="author" content="William Y. Arms">
<meta name="title" content="Key Concepts in the Architecture of the Digital Library">
<meta name="date" content="July 1995">
<meta name="identifier" content="hdl:cnri.dlib/july95-arms">

<title>Digital library concepts</title>

<meta name="VERSION" content="Author final">
<meta name="CHANGE" content="Metadata added 5/24/96">

</head>

<body>

<h1><center>  
<img src="/web/19971010044705im_/http://www.dlib.org/dlib/July95/dlib_header.gif" border="0">
</h1>

<h1>Key Concepts in the Architecture of the Digital Library</h1>

[deletia]
```

In addition to adding the banner and rewriting links, HTML comments are inserted with replay datetimes and metadata about the specific replay itself.  Obviously, this will change on each replay; here is the same request as above, but only looking at the end of the HTML file:

```
% curl -i -s https://web.archive.org/web/19971010044705/http://www.dlib.org/dlib/July95/07arms.ht| tail -25
<i>hdl:cnri.dlib/july95-arms</i>
</body>

</html>
<!--
     FILE ARCHIVED ON 04:47:05 Oct 10, 1997 AND RETRIEVED FROM THE
     INTERNET ARCHIVE ON 17:18:19 Oct 07, 2020.
     JAVASCRIPT APPENDED BY WAYBACK MACHINE, COPYRIGHT INTERNET ARCHIVE.

     ALL OTHER CONTENT MAY ALSO BE PROTECTED BY COPYRIGHT (17 U.S.C.
     SECTION 108(a)(3)).
-->
<!--
playback timings (ms):
  LoadShardBlock: 608.209 (3)
  captures_list: 649.266
  RedisCDXSource: 10.983
  exclusion.robots.policy: 0.177
  PetaboxLoader3.resolve: 200.948 (2)
  load_resource: 734.353
  CDXLines.iter: 21.455 (3)
  PetaboxLoader3.datanode: 1082.751 (4)
  esindex: 0.015
  exclusion.robots: 0.192
-->
```

Here's the same request, but with `id_` added at the end of the datetime.  That is, `19971010044705id_` instead of just `19971010044705`:

```
% curl -i https://web.archive.org/web/19971010044705id_/http://www.dlib.org/dlib/July95/07arms.html  
HTTP/2 200 
server: nginx/1.15.8
date: Wed, 07 Oct 2020 17:21:24 GMT
content-type: text/html
x-archive-orig-date: Fri, 10 Oct 1997 04:49:13 GMT
x-archive-orig-server: Apache/1.1.3
x-archive-orig-content-length: 16459
x-archive-orig-last-modified: Mon, 07 Oct 1996 14:45:49 GMT
cache-control: max-age=1800
memento-datetime: Fri, 10 Oct 1997 04:47:05 GMT
link: <http://www.dlib.org:80/dlib/July95/07arms.html>; rel="original", <https://web.archive.org/web/timemap/link/http://www.dlib.org:80/dlib/July95/07arms.html>; rel="timemap"; type="application/link-format", <https://web.archive.org/web/http://www.dlib.org:80/dlib/July95/07arms.html>; rel="timegate", <https://web.archive.org/web/19971010044705/http://www.dlib.org:80/dlib/July95/07arms.html>; rel="first memento"; datetime="Fri, 10 Oct 1997 04:47:05 GMT", <https://web.archive.org/web/19971010044705/http://www.dlib.org:80/dlib/July95/07arms.html>; rel="memento"; datetime="Fri, 10 Oct 1997 04:47:05 GMT", <https://web.archive.org/web/19971210081027/http://www.dlib.org:80/dlib/July95/07arms.html>; rel="next memento"; datetime="Wed, 10 Dec 1997 08:10:27 GMT", <https://web.archive.org/web/20200208020611/http://www.dlib.org/dlib/July95/07arms.html>; rel="last memento"; datetime="Sat, 08 Feb 2020 02:06:11 GMT"
content-security-policy: default-src 'self' 'unsafe-eval' 'unsafe-inline' data: blob: archive.org web.archive.org analytics.archive.org pragma.archivelab.org
x-archive-src: FS-195284-c/FS-195470.arc.gz
server-timing: captures_list;dur=484.827765, exclusion.robots.policy;dur=0.120372, RedisCDXSource;dur=7.376191, esindex;dur=0.021349, load_resource;dur=129.270256, PetaboxLoader3.resolve;dur=104.984189, PetaboxLoader3.datanode;dur=305.210275, CDXLines.iter;dur=16.936252, exclusion.robots;dur=0.130152, LoadShardBlock;dur=455.616121
x-app-server: wwwb-app100
x-ts: 200
x-location: All
x-cache-key: httpsweb.archive.org/web/19971010044705id_/http://www.dlib.org/dlib/July95/07arms.htmlUS
x-page-cache: HIT
x-archive-screenname: 0

<HTML>

<HEAD>

<META NAME = "author" CONTENT = "William Y. Arms">
<META NAME="title" CONTENT="Key Concepts in the Architecture of the Digital Library">
<META NAME="date" CONTENT="July 1995">
<META NAME="identifier" CONTENT="hdl:cnri.dlib/july95-arms">

<TITLE>Digital library concepts</TITLE>

<META NAME="VERSION" CONTENT="Author final">
<META NAME = "CHANGE" CONTENT = "Metadata added 5/24/96">

</HEAD>

<BODY>

<H1><CENTER>  
<IMG SRC="dlib_header.gif"border=0 >
</H1>

<H1>Key Concepts in the Architecture of the Digital Library</H1>

[deletia]
```

Note that in the above response, although there is no archival banner inserted and the HTML has not had its links rewritten, the HTTP response headers are updated to be "now" and not "then" (i.e., `Wed, 07 Oct 2020 17:21:24 GMT` and not `Fri, 10 Oct 1997 04:49:13 GMT`).  Also note the presence of the `x-archive-orig` HTTP response headers.  The entity body is not transformed, but the HTTP response headers are transformed.  

Replaying the tranformed page with the HTTP response headers will result in different hashes each time:

```
% date ; curl -i -s https://web.archive.org/web/19971010044705/http://www.dlib.org/dlib/July95/07arms.html | md5sum
Wed Oct  7 13:26:49 EDT 2020
33b98ae8f5bc38eaf74cb5aadbfcd0d8  -
% date ; curl -i -s https://web.archive.org/web/19971010044705/http://www.dlib.org/dlib/July95/07arms.html | md5sum
Wed Oct  7 13:26:53 EDT 2020
bee305f27dfbfa168b945e39092710ee  -
% date ; curl -i -s https://web.archive.org/web/19971010044705/http://www.dlib.org/dlib/July95/07arms.html | md5sum
Wed Oct  7 13:26:56 EDT 2020
9b2dd3e6e1626042a1515b5ea9804953  -
```

Leaving out the HTTP response headers will result in the same hash, as long as the replay is recent and thus is a cache hit:

```
% date ; curl -s https://web.archive.org/web/19971010044705/http://www.dlib.org/dlib/July95/07arms.html | md5sum
Wed Oct  7 13:28:16 EDT 2020
8fc843af08eae08b326b6010e82621d3  -
% date ; curl -s https://web.archive.org/web/19971010044705/http://www.dlib.org/dlib/July95/07arms.html | md5sum
Wed Oct  7 13:28:18 EDT 2020
8fc843af08eae08b326b6010e82621d3  -
% date ; curl -s https://web.archive.org/web/19971010044705/http://www.dlib.org/dlib/July95/07arms.html | md5sum
Wed Oct  7 13:28:19 EDT 2020
b68ab56b7770682fdb6d8c543c09f506  -
```

If you note above, the first two replays produced hash values of `8fc843af08eae08b326b6010e82621d3`, and then at exactly 10 minutes after the first request (shown in this first example above; `Wed, 07 Oct 2020 17:18:19 GMT` vs. `Wed Oct  7 13:28:19 EDT 2020`), there is a new hash value.  Thus the IA's cache has a 10 minute duration.  Below are two HEAD requests and showing the appropriate header:

```
% date ; curl -s -I https://web.archive.org/web/19971010044705/http://www.dlib.org/dlib/July95/07arms.html | grep "x-page-cache:"
Wed Oct  7 13:34:30 EDT 2020
x-page-cache: HIT
% date ; curl -s -I https://web.archive.org/web/19971010044705/http://www.dlib.org/dlib/July95/07arms.html | grep "x-page-cache:"
Wed Oct  7 13:38:40 EDT 2020
x-page-cache: EXPIRED
% date ; curl -s -I https://web.archive.org/web/19971010044705/http://www.dlib.org/dlib/July95/07arms.html | grep "x-page-cache:"
Wed Oct  7 13:51:52 EDT 2020
x-page-cache: MISS
```

## Comparison with the live web

Here is an example of a live web resource that appears to not have been modified since 2013 (`Last-Modified: Thu, 09 May 2013 18:57:53 GMT`):

```
% curl -I http://www.dlib.org/dlib/July95/07arms.html
HTTP/1.1 200 OK
Date: Wed, 07 Oct 2020 17:43:02 GMT
Server: Apache/2.2.15 (CentOS)
Last-Modified: Thu, 09 May 2013 18:57:53 GMT
ETag: "1819ab-404b-4dc4da0b59c97"
Accept-Ranges: bytes
Content-Length: 16459
Content-Type: text/html; charset=UTF-8
```

But `Last-Modified` can be changed just by making a idempotent change to the file (e.g., using the `touch` command to update the `Last-Modified` value for a file but leave the contents unchaged).  Here we will show that the content on the live web is the same as the version the IA archived in 1997.  To do so, we'll hash the entity of the live web and the entity of the raw archived version:

```
% date ; curl -s http://www.dlib.org/dlib/July95/07arms.html | md5sum
Wed Oct  7 13:48:13 EDT 2020
3cc0fb32a7fe8f1f4de9a40aa5069cfe  -
% date ; curl -s https://web.archive.org/web/19971010044705id_/http://www.dlib.org/dlib/July95/07arms.html | md5sum
Wed Oct  7 13:48:27 EDT 2020
3cc0fb32a7fe8f1f4de9a40aa5069cfe  -
```

Although this doesn't prove that the live web page did not have a different value in 1998, 1999, etc., it does show that the live web version now (i.e., `Wed Oct  7 13:48:27 EDT 2020`) is exactly the same as the version the IA archived then (i.e., `Fri, 10 Oct 1997 04:49:13 GMT`).  This process could be extended with all the mementos in the [TimeMap](https://web.archive.org/web/timemap/link/http://www.dlib.org:80/dlib/July95/07arms.html) to show the datetimes where IA archived the page and that they also match each other as well as the version on the live web.

The above example was with an HTML page, although they are less likely to 1) have a `Last-Modified` HTTP response header, and 2) to remain unchanged on the live web for so long.  This is more likely to occur with images, PDFs, style sheets, etc.

```
% curl -I https://web.archive.org/web/19971111151037id_/http://www.dlib.org/dlib/July95/dlib_header.gif
HTTP/2 200 
server: nginx/1.15.8
date: Wed, 07 Oct 2020 17:57:47 GMT
content-type: image/gif
x-archive-orig-date: Tue, 11 Nov 1997 15:12:31 GMT
x-archive-orig-server: Apache/1.2.4
x-archive-orig-last-modified: Mon, 07 Oct 1996 14:45:50 GMT
x-archive-orig-etag: "121c5-8bf-3259179e"
x-archive-orig-content-length: 2239
x-archive-orig-accept-ranges: bytes
cache-control: max-age=1800
memento-datetime: Tue, 11 Nov 1997 15:10:37 GMT
link: <http://www.dlib.org:80/dlib/July95/dlib_header.gif>; rel="original", <https://web.archive.org/web/timemap/link/http://www.dlib.org:80/dlib/July95/dlib_header.gif>; rel="timemap"; type="application/link-format", <https://web.archive.org/web/http://www.dlib.org:80/dlib/July95/dlib_header.gif>; rel="timegate", <https://web.archive.org/web/19970719053256/http://www.dlib.org:80/dlib/July95/dlib_header.gif>; rel="first memento"; datetime="Sat, 19 Jul 1997 05:32:56 GMT", <https://web.archive.org/web/19970719053256/http://www.dlib.org:80/dlib/July95/dlib_header.gif>; rel="prev memento"; datetime="Sat, 19 Jul 1997 05:32:56 GMT", <https://web.archive.org/web/19971111151037/http://www.dlib.org:80/dlib/July95/dlib_header.gif>; rel="memento"; datetime="Tue, 11 Nov 1997 15:10:37 GMT", <https://web.archive.org/web/19980624061425/http://www.dlib.org:80/dlib/July95/dlib_header.gif>; rel="next memento"; datetime="Wed, 24 Jun 1998 06:14:25 GMT", <https://web.archive.org/web/20200605041246/http://www.dlib.org/dlib/July95/dlib_header.gif>; rel="last memento"; datetime="Fri, 05 Jun 2020 04:12:46 GMT"
content-security-policy: default-src 'self' 'unsafe-eval' 'unsafe-inline' data: blob: archive.org web.archive.org analytics.archive.org pragma.archivelab.org
x-archive-src: FS-358868-c/FS-359145.arc.gz
server-timing: CDXLines.iter;dur=24.160144, captures_list;dur=280.040291, RedisCDXSource;dur=2.574927, exclusion.robots.policy;dur=0.661183, exclusion.robots;dur=0.681324, load_resource;dur=183.108635, PetaboxLoader3.resolve;dur=56.562540, esindex;dur=0.021275, PetaboxLoader3.datanode;dur=287.328980, LoadShardBlock;dur=245.560450
x-app-server: wwwb-app29
x-ts: 200
x-location: All
x-cache-key: httpsweb.archive.org/web/19971111151037id_/http://www.dlib.org/dlib/July95/dlib_header.gifUS
x-page-cache: MISS
x-archive-screenname: 0
```

Also note that for images, it is more common to use the `im_` modifier (which replays the original image without a banner).  When in doubt, use the `id_` for the identity transformation.  Another image example:

```
% curl -I https://pbs.twimg.com/profile_images/1099396215538626561/b8OM6dBK_400x400.png
HTTP/2 200 
access-control-allow-origin: *
access-control-expose-headers: Content-Length
cache-control: max-age=604800, must-revalidate
last-modified: Sat, 23 Feb 2019 19:48:58 GMT
strict-transport-security: max-age=631138519
x-content-type-options: nosniff
content-type: image/png
accept-ranges: bytes
date: Wed, 07 Oct 2020 18:01:24 GMT
x-cache: MISS, MISS
x-tw-cdn: FT
x-served-by: cache-fty21338-FTY, cache-bos4620-BOS, cache-tw-ZZZ1
content-length: 111733
% curl -I https://web.archive.org/web/20190313204158id_/https://pbs.twimg.com/profile_images/1099396215538626561/b8OM6dBK_400x400.png
HTTP/2 200 
server: nginx/1.15.8
date: Wed, 07 Oct 2020 18:03:25 GMT
content-type: image/png
x-archive-orig-accept-ranges: bytes
x-archive-orig-access-control-allow-origin: *
x-archive-orig-access-control-expose-headers: Content-Length
x-archive-orig-cache-control: max-age=604800, must-revalidate
x-archive-orig-date: Wed, 13 Mar 2019 20:41:58 GMT
x-archive-orig-last-modified: Sat, 23 Feb 2019 19:48:58 GMT
x-archive-orig-server: ECS (dab/4BF1)
x-archive-orig-surrogate-key: profile_images profile_images/bucket/9 profile_images/1099396215538626561
x-archive-orig-x-cache: HIT
x-archive-orig-x-connection-hash: 6bb3203b16818bcc05993ac24ba2a08a
x-archive-orig-x-content-type-options: nosniff
x-archive-orig-x-response-time: 59
x-archive-orig-content-length: 111733
cache-control: max-age=1800
memento-datetime: Wed, 13 Mar 2019 20:41:58 GMT
link: <https://pbs.twimg.com/profile_images/1099396215538626561/b8OM6dBK_400x400.png>; rel="original", <https://web.archive.org/web/timemap/link/https://pbs.twimg.com/profile_images/1099396215538626561/b8OM6dBK_400x400.png>; rel="timemap"; type="application/link-format", <https://web.archive.org/web/https://pbs.twimg.com/profile_images/1099396215538626561/b8OM6dBK_400x400.png>; rel="timegate", <https://web.archive.org/web/20190313204158/https://pbs.twimg.com/profile_images/1099396215538626561/b8OM6dBK_400x400.png>; rel="first memento"; datetime="Wed, 13 Mar 2019 20:41:58 GMT", <https://web.archive.org/web/20190313204158/https://pbs.twimg.com/profile_images/1099396215538626561/b8OM6dBK_400x400.png>; rel="memento"; datetime="Wed, 13 Mar 2019 20:41:58 GMT", <https://web.archive.org/web/20190527085450/https://pbs.twimg.com/profile_images/1099396215538626561/b8OM6dBK_400x400.png>; rel="next memento"; datetime="Mon, 27 May 2019 08:54:50 GMT", <https://web.archive.org/web/20200830195734/https://pbs.twimg.com/profile_images/1099396215538626561/b8OM6dBK_400x400.png>; rel="last memento"; datetime="Sun, 30 Aug 2020 19:57:34 GMT"
content-security-policy: default-src 'self' 'unsafe-eval' 'unsafe-inline' data: blob: archive.org web.archive.org analytics.archive.org pragma.archivelab.org
x-archive-src: archiveteam_archivebot_go_20190314070002/netpreserve.org-inf-20190313-133517-c8mrt-00000.warc.gz
server-timing: esindex;dur=0.016003, LoadShardBlock;dur=2951.394539, RedisCDXSource;dur=51.325283, exclusion.robots.policy;dur=0.195063, PetaboxLoader3.resolve;dur=379.647541, exclusion.robots;dur=0.211465, load_resource;dur=487.308357, PetaboxLoader3.datanode;dur=2671.572329, captures_list;dur=3028.495723, CDXLines.iter;dur=21.725981
x-app-server: wwwb-app39
x-ts: 200
x-location: All
x-cache-key: httpsweb.archive.org/web/20190313204158id_/https://pbs.twimg.com/profile_images/1099396215538626561/b8OM6dBK_400x400.pngUS
x-page-cache: HIT
x-archive-screenname: 0
% curl -s https://pbs.twimg.com/profile_images/1099396215538626561/b8OM6dBK_400x400.png | md5sum
1e2635a4b97791ad415bce0f697ed76e  -
% curl -s https://web.archive.org/web/20190313204158im_/https://pbs.twimg.com/profile_images/1099396215538626561/b8OM6dBK_400x400.png | md5sum
1e2635a4b97791ad415bce0f697ed76e  -
% ^im^id
curl -s https://web.archive.org/web/20190313204158id_/https://pbs.twimg.com/profile_images/1099396215538626561/b8OM6dBK_400x400.png | md5sum
1e2635a4b97791ad415bce0f697ed76e  -
```

The above examples leverage `Last-Modified`.  It's useful, but keep in mind that it can be fake or wrong (see [Clausen, 2004](http://www.netarkivet.dk/wp-content/uploads/Etags-2004.pdf) for a discussion of some of the problems with `Last-Modified`).  For example, on HTML pages (but not images) Twitter always sets `Last-Modified` to have the same value as `Date`:

```
% curl -s -I https://twitter.com/phonedude_mln | grep -i "last-modified:\|date:"
date: Wed, 07 Oct 2020 23:43:03 GMT
last-modified: Wed, 07 Oct 2020 23:43:03 GMT
% curl -s -I https://twitter.com/phonedude_mln | grep -i "last-modified:\|date:"
date: Wed, 07 Oct 2020 23:43:05 GMT
last-modified: Wed, 07 Oct 2020 23:43:05 GMT
% curl -s -I https://twitter.com/phonedude_mln | grep -i "last-modified:\|date:"
date: Wed, 07 Oct 2020 23:43:08 GMT
last-modified: Wed, 07 Oct 2020 23:43:08 GMT
% curl -s -I https://twitter.com/phonedude_mln | grep -i "last-modified:\|date:"
date: Wed, 07 Oct 2020 23:43:11 GMT
last-modified: Wed, 07 Oct 2020 23:43:10 GMT
```

The reason can be explained by all of the headers that they send to prevent caching:

```
% curl -I https://twitter.com/phonedude_mln
HTTP/2 200 
cache-control: no-cache, no-store, must-revalidate, pre-check=0, post-check=0
content-security-policy: connect-src 'self' blob: https://*.giphy.com https://*.pscp.tv https://*.video.pscp.tv https://*.twimg.com https://api.twitter.com https://api-stream.twitter.com https://ads-api.twitter.com https://caps.twitter.com https://media.riffsy.com https://pay.twitter.com https://sentry.io https://ton.twitter.com https://twitter.com https://upload.twitter.com https://www.google-analytics.com https://app.link https://api2.branch.io https://bnc.lt https://vmap.snappytv.com https://vmapstage.snappytv.com https://vmaprel.snappytv.com https://vmap.grabyo.com https://dhdsnappytv-vh.akamaihd.net https://pdhdsnappytv-vh.akamaihd.net https://mdhdsnappytv-vh.akamaihd.net https://mdhdsnappytv-vh.akamaihd.net https://mpdhdsnappytv-vh.akamaihd.net https://mmdhdsnappytv-vh.akamaihd.net https://mdhdsnappytv-vh.akamaihd.net https://mpdhdsnappytv-vh.akamaihd.net https://mmdhdsnappytv-vh.akamaihd.net https://dwo3ckksxlb0v.cloudfront.net ; default-src 'self'; form-action 'self' https://twitter.com https://*.twitter.com; font-src 'self' https://*.twimg.com; frame-src 'self' https://twitter.com https://mobile.twitter.com https://pay.twitter.com https://cards-frame.twitter.com ; img-src 'self' blob: data: https://*.cdn.twitter.com https://ton.twitter.com https://*.twimg.com https://analytics.twitter.com https://cm.g.doubleclick.net https://www.google-analytics.com https://www.periscope.tv https://www.pscp.tv https://media.riffsy.com https://*.giphy.com https://*.pscp.tv; manifest-src 'self'; media-src 'self' blob: https://twitter.com https://*.twimg.com https://*.vine.co https://*.pscp.tv https://*.video.pscp.tv https://*.giphy.com https://media.riffsy.com https://dhdsnappytv-vh.akamaihd.net https://pdhdsnappytv-vh.akamaihd.net https://mdhdsnappytv-vh.akamaihd.net https://mdhdsnappytv-vh.akamaihd.net https://mpdhdsnappytv-vh.akamaihd.net https://mmdhdsnappytv-vh.akamaihd.net https://mdhdsnappytv-vh.akamaihd.net https://mpdhdsnappytv-vh.akamaihd.net https://mmdhdsnappytv-vh.akamaihd.net https://dwo3ckksxlb0v.cloudfront.net; object-src 'none'; script-src 'self' 'unsafe-inline' https://*.twimg.com   https://www.google-analytics.com https://twitter.com https://app.link  'nonce-ZjE0NTczYjctZDZiOS00M2U1LWE4NWUtMTZhN2EwN2IzYjhj'; style-src 'self' 'unsafe-inline' https://*.twimg.com; worker-src 'self' blob:; report-uri https://twitter.com/i/csp_report?a=O5RXE%3D%3D%3D&ro=false
content-type: text/html; charset=utf-8
cross-origin-opener-policy: same-origin
date: Wed, 07 Oct 2020 23:44:09 GMT
expiry: Tue, 31 Mar 1981 05:00:00 GMT
last-modified: Wed, 07 Oct 2020 23:44:09 GMT
pragma: no-cache
server: tsa_a
set-cookie: personalization_id="v1_MPteRytvbrFn3AdpxR1l/A=="; Max-Age=63072000; Expires=Fri, 07 Oct 2022 23:44:09 GMT; Path=/; Domain=.twitter.com; Secure; SameSite=None
set-cookie: guest_id=v1%3A160211424957753034; Max-Age=63072000; Expires=Fri, 07 Oct 2022 23:44:09 GMT; Path=/; Domain=.twitter.com; Secure; SameSite=None
strict-transport-security: max-age=631138519
vary: Accept-Encoding
x-connection-hash: 5e36364786dced1f705bca3811deb153
x-content-type-options: nosniff
x-frame-options: DENY
x-powered-by: Express
x-response-time: 49
x-xss-protection: 0
```
