# Step 4: download issues that hasn't been downloaded in the base Chronicle
# folder
# Note: depending on what you did for step 3, this script might download stuff
# already in the `SelectedIssues` folder!!!

# File input: 
#   `fileListWithPagesAndActuralCount.json`: a dictionary with five digit number as
#       key to each issue, and each value is a dictionary detailing date, other info,
#       total number of pages, and existing pages of the issue.
#   `chosenIssue.json`: a list of keys for each chosen issue.

# File output:
#   Downloaded image in `images/`

import json
import shutil
import os
import time
import tqdm
import requests

with open('fileListWithPagesAndActuralCount.json') as f:
    fileList = json.load(f)

with open('chosenIssue.json') as f:
    chosenIssue = json.load(f)

# I used this because I don't want to write a generator or some sort while
# getting the progress bar. 
imageURLs = []

for i in chosenIssue:
    if fileList[i]['onedriveCount'] != fileList[i]['pages']:
        for j in range(fileList[i]['pages']):
            imageURLs.append('https://library.duke.edu/digitalcollections/media/jpg/dukechronicle/lrg/dchnp%s%03d0.jpg' % (i, j+1))
            
def downloadImage(url):
    fileName = url[-13:]
    filePath = 'images/%s' % fileName

    if not os.path.exists(filePath):
        # Note: there's no need to change user agent 
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(filePath, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
        else:
            raise

for i in tqdm.tqdm(imageURLs):
    downloadImage(i)
    time.sleep(0.5)