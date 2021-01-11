# Step 5: move files in base folder to `SelectedIssues` folder
# Note: you must not add /s in step 3 for this to account for all files in the
# base folder

# File input: 
#   `fileListWithPagesAndActuralCount.json`: a dictionary with five digit number as
#       key to each issue, and each value is a dictionary detailing date, other info,
#       total number of pages, and existing pages of the issue.
#   `chosenIssue.json`: a list of keys for each chosen issue.


import json
import os

# Change this on your computer
baseFolder = r'C:\Users\xin_r\OneDrive - Duke University\Chronicle'

with open('fileListWithPagesAndActuralCount.json') as f:
    fileList = json.load(f)

with open('chosenIssue.json') as f:
    chosenIssue = json.load(f)

for i in chosenIssue:
    if fileList[i]['onedriveCount'] == fileList[i]['pages']:
        for j in range(fileList[i]['pages']):
            fileName = '%s%03d0.jpg' % (i, j+1)
            os.rename('%s/%s' % (baseFolder, fileName), '%s/SelectedIssues/%s' % (baseFolder, fileName))
            