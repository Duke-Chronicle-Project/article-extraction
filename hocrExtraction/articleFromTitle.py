import pandas as pd
import os

def findTitles(path):
    partID = []
    id = 0
    df = pd.read_csv(path)
    onTitle = False
    isTitleList = df['isTitle'].tolist()
    for x in isTitleList:
        if not(onTitle) and x == True:
            id = id+1
            onTitle = True
        elif onTitle and x == False:
            onTitle = False
        partID.append(id)
    df['PartID'] = partID
    df.to_csv('./test/testPartID.csv', index = False)
if __name__ == '__main__':
    findTitles('./test/testTitle.csv')