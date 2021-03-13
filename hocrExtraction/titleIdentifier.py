import pandas as pd

def findTitles(path):
    df = pd.read_csv(path)
    heightColumns = df['lineHeight'].tolist()
    wordColumns = df['word'].tolist()
    titleBooleans = []
    for x in range(len(heightColumns)):
        if heightColumns[x] > 100 and not wordColumns[x].isspace():
            titleBooleans.append(True)
        else:
            titleBooleans.append(False)
    df['isTitle'] = titleBooleans
    df.to_csv('./test/testPartID1.csv', index = False)
if __name__ == '__main__':
    findTitles('./test/test.csv')

