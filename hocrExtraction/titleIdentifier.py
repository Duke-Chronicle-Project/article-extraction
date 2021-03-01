import pandas as pd

def findTitles(path):
    df = pd.read_csv(path)
    heightColumns = df['lineHeight'].tolist()
    titleBooleans = []
    for x in heightColumns:
        if x > 100:
            titleBooleans.append(True)
        else:
            titleBooleans.append(False)
    df['isTitle'] = titleBooleans
    df.to_csv('./test/testTitle.csv', index = False)
if __name__ == '__main__':
    findTitles('./test/test.csv')

