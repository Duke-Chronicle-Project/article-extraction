# Step 2: get the number of required images per issue

# File input: 
#   `fileList.json`: a dictionary with five digit number as key to each issue,
#       and each value is a dictionary detailing date and other info about the
#       issue. Gathered through running JS on the page.

# File output: 
#   `fileListWithPages.json`: a dictionary with five digit number as
#       key to each issue, and each value is a dictionary detailing date, other info
#       and total number of pages of the issue.


import requests
import tqdm
from bs4 import BeautifulSoup
import re, json, time, os

def getTotPage(fileNum):
    """Get the total number of pages of the given issue from its library page

    Args:
        fileNum (str): five-digit id for the target issue

    Returns:
        int: total number of pages of the requested issue
    """
    html = requests.get('https://library.duke.edu/digitalcollections/dukechronicle_dchnp%s/' % fileNum).text

    soup = BeautifulSoup(html, 'html.parser')
    pageText = soup.select_one('aside>div.pagecount').text

    return int(re.match('(\d+) pages', pageText).group(1))


if os.path.exists('fileListWithPages.json'):
    fileListName = 'fileListWithPages.json'
else: 
    fileListName = 'fileList.json'

with open(fileListName) as f:
    fileList = json.load(f)

for i in tqdm.tqdm(fileList):
    if not 'pages' in fileList[i]:
        fileList[i]['pages'] = getTotPage(i)
        time.sleep(0.5)

with open('fileListWithPages.json', 'w') as f:
    json.dump(fileList, f)