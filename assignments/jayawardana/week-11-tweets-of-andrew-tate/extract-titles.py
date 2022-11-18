import sys
import time
import urllib.request

import bs4

if __name__ == "__main__":

    # get filename
    filename = sys.argv[1]

    # open file with URI-Ms
    with open(filename, "r") as f:

        # iterate all URI-Ms
        for urim in f.readlines():
            urim = urim.strip()

            # deference URI-M
            with urllib.request.urlopen(urim) as response:
                html = response.read()
                last_modified = response.headers["x-archive-orig-last-modified"]
                t = time.strptime(last_modified, "%a, %d %b %Y %H:%M:%S GMT")
                t = time.strftime("%Y%m%d%H%M%S")
                tree = bs4.BeautifulSoup(html, features="html.parser")

                # drop <script> tags
                for s in tree.select("script"):
                    s.extract()

                # drop <style> tags
                for s in tree.select("style"):
                    s.extract()

                # parse HTML
                tweet_content_meta = tree.find("meta", {"property": "og:description"})
                if isinstance(tweet_content_meta, bs4.Tag):
                    tweet_content = tweet_content_meta.get("content") or ""
                    if isinstance(tweet_content, list):
                        tweet_content = " ".join(tweet_content).strip()
                    tweet_content = tweet_content.replace("\n", "")
                else:
                    tweet_content = ""
                print(t, tweet_content)
