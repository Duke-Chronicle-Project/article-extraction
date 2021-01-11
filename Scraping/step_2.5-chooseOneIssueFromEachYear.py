# Step 2.5: randomly choose one issues from each year and write their keys into
# 'chosenIssue.json' for picking a small subset of files

# File input: 
#   `fileList.json`: a dictionary with five digit number as key to each issue,
#       and each value is a dictionary detailing date and other info about the
#       issue. Gathered through running JS on the page.

# File output:
#   `chosenIssue.json`: a list of keys for each chosen issue.


import random, json

with open('fileList.json') as f:
    fileList = json.load(f)

fileByYear = {}

for i in fileList:
    year = fileList[i]['date'][:4]
    if year not in fileByYear:
        fileByYear[year] = []
    fileByYear[year].append(i)

output = list(map(lambda x: random.choice(fileByYear[x]), fileByYear))

with open('chosenIssue.json', 'w') as f:
    json.dump(output, f)