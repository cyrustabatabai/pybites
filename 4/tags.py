import os
from collections import Counter
import urllib.request
import xml.etree.ElementTree as ET

# prep
tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.join(tmp, 'feed')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
    tempfile
)

with open(tempfile) as f:
    content = f.read().lower()

tree = ET.parse(tempfile)
root = tree.getroot()
for child in root:
    for c in child:
        print(c)

def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    tree = ET.parse(tempfile)
    root = tree.getroot()

    counts = Counter(item.text.lower() for item in root.iter('category')).most_common(n)
    return sorted(counts,key=lambda x: (x[1],x[0]),reverse=True)




