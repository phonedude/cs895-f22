# Archived Tweets of Andrew Tate

### Step 1 - Obtain Archived Tweet URI-Ms
```bash

for TWITTER_HANDLE in "ofwudan" "cobratate" "masterfulpo"; do \
curl -sL 'https://web.archive.org/cdx/search/cdx?url=twitter.com/'${TWITTER_HANDLE}'/status/*&filter=statuscode:200&filter=mimetype:text/html&filter=original:^.*\/status\/\d\{18\}.*$' \
| tee cdx/${TWITTER_HANDLE}-1.txt; \
done

```

### Step 2 - Keep only the Oldest Memento
```bash

cat cdx/ofwudan-1.txt | \
awk '{print $2, $3, substr($3,36,18)}' | \
sort -k3 -k1 | \
uniq -f 2 | \
tee cdx/ofwudan-2.txt

cat cdx/cobratate-1.txt | \
awk '{print $2, $3, substr($3,38,18)}' | \
sort -k3 -k1 | \
uniq -f 2 | \
tee cdx/cobratate-2.txt

cat cdx/masterfulpo-1.txt | \
awk '{print $2, $3, substr($3,40,18)}' | \
sort -k3 -k1 | \
uniq -f 2 | \
tee cdx/masterfulpo-2.txt

```

### Step 3 - Get the Memento-Datetime and URI-R Fields
```bash
for TWITTER_HANDLE in "ofwudan" "cobratate" "masterfulpo"; do \
cat cdx/${TWITTER_HANDLE}-2.txt | \
awk '{print $1,$2}' | \
sort | \
tee cdx/${TWITTER_HANDLE}-3.txt; \
done
```

### Step 4 - Generate the URI-M for each Memento
```bash
for TWITTER_HANDLE in "ofwudan" "cobratate" "masterfulpo"; do \
cat cdx/${TWITTER_HANDLE}-3.txt | \
awk '{print "https://web.archive.org/web/"$1"/"$2}' | \
tee urims/${TWITTER_HANDLE}.txt; \
done
```

### Step 5 - Dereferencing the HTML of each URI-M
```bash
python -u extract-html.py ofwudan
python -u extract-html.py cobratate
python -u extract-html.py masterfulpo
```
