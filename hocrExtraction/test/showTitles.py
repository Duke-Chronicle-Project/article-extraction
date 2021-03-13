'''
Visualizes the identified titles of a single image
'''

import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image


def getTitles(path):
    df = pd.read_csv(path)
    return df[df.isTitle == True]

def showTitles(path):
    '''
    :param path: path to CSV to visualize
    '''
    df = getTitles(path)
    df.reset_index(drop=True, inplace=True)
    img = df.iloc[0]['image']

    im = Image.open(img)
    # Create figure and axes
    fig, ax = plt.subplots()

    # Display the image
    ax.imshow(im)

    for index, row in df.iterrows():
        # Create a Rectangle patch
        width = df.iloc[index]['wordX1'] - df.iloc[index]['wordX0']
        height = df.iloc[index]['wordY1'] - df.iloc[index]['wordY0']
        rect = patches.Rectangle((df.iloc[index]['wordX0'], df.iloc[index]['wordY0']), width, height, linewidth=1, edgecolor='b', facecolor='none')

        # Add the patch to the Axes
        ax.add_patch(rect)

    plt.show()


if __name__ == '__main__':
    path = './testPartIDSpace.csv'
    showTitles(path)