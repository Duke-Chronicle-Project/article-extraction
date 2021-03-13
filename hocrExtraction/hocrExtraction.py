'''
hOCR extraction using the hOCR standards defined here: http://kba.cloud/hocr-spec/1.2/
sampleInput.hocr generated using tesseract 4.1.1 command `tesseract alice_1.png sampleInput hocr -c hocr_font_info=1`
'''

from lxml import html
import pandas as pd


def parseAttrib(attributes):
    '''
    Return the properties of an hOCR element when given its attributes
    '''
    if attributes['class'] == 'ocrx_word':
        wordProps = attributes['title'].split('; ')

        wordBbox = [int(i) for i in wordProps[0].split()[1:]]   # get word bounding box
        wordConf = int(wordProps[1].split()[1])                 # get word confidence
        wordNum = int(attributes['id'].split('_')[-1])          # get word number
        fontSize = int(wordProps[2].split()[1])                 # get word font size
        return wordBbox, wordConf, wordNum, fontSize

    elif attributes['class'] == 'ocr_line':
        lineProps = attributes['title'].split('; ')

        lineBbox = [int(i) for i in lineProps[0].split()[1:]]   # get line bounding box
        lineHeight = float(lineProps[2].split()[1])             # get line height | TODO: get font size from this?
        lineNum = int(attributes['id'].split('_')[-1])          # get line number
        return lineBbox, lineHeight, lineNum        

    elif attributes['class'] == 'ocr_par':
        parBbox = [int(i) for i in attributes['title'].split()[1:]] # get paragraph area bounding box
        parNum = int(attributes['id'].split('_')[-1])               # get paragraph number
        return parBbox, parNum

    elif attributes['class'] == 'ocr_carea':
        colAreaBbox = [int(i) for i in attributes['title'].split()[1:]] # get column area bounding box
        colAreaNum = int(attributes['id'].split('_')[-1])               # get column area number
        return colAreaBbox, colAreaNum

    else:
        pageProps = attributes['title'].split('; ')

        pageBbox = [int(i) for i in pageProps[1].split()[1:]]   # get page bounding box
        pageImage = pageProps[0].split(' "')[1][:-1]            # get page image
        pageNum = int(attributes['id'].split('_')[-1])          # get page number
        return pageBbox, pageImage, pageNum

def parseHOCR(path, save=False):
    '''
    Parse and save the data from an hOCR file
    '''
    doc = html.parse(path)
    final = []

    for page in doc.xpath("//*[@class='ocr_page']"):
        pageBbox, pageImage, pageNum = parseAttrib(page.attrib)

        for colArea in page.xpath("./*[@class='ocr_carea']"):
            colAreaBbox, colAreaNum = parseAttrib(colArea.attrib)
            
            for paragraph in colArea.xpath("./*[@class='ocr_par']"):
                parBbox, parNum = parseAttrib(paragraph.attrib)

                for line in paragraph.xpath("./*[@class='ocr_line']"):
                    lineBbox, lineHeight, lineNum = parseAttrib(line.attrib)

                    for word in line.xpath("./*[@class='ocrx_word']"):
                        wordBbox, wordConf, wordNum, fontSize = parseAttrib(word.attrib)

                        final.append((word.text, wordConf, wordNum, fontSize, wordBbox[0], wordBbox[1], wordBbox[2], wordBbox[3],
                                      lineNum, lineHeight, lineBbox[0], lineBbox[1], lineBbox[2], lineBbox[3],
                                      parNum, parBbox[0], parBbox[1], parBbox[2], parBbox[3],
                                      colAreaNum, colAreaBbox[0], colAreaBbox[1], colAreaBbox[2], colAreaBbox[3],
                                      pageNum, pageBbox[0], pageBbox[1], pageBbox[2], pageBbox[3], pageImage))

    df = pd.DataFrame(final, columns=['word', 'conf', 'wordNum', 'fontSize', 'wordX0', 'wordY0', 'wordX1', 'wordY1',
                                      'lineNum', 'lineHeight', 'lineX0', 'lineY0', 'lineX1', 'lineY1',
                                      'parNum', 'parX0', 'parY0', 'parX1', 'parY1',
                                      'colAreaNum', 'colAreaX0', 'colAreaY0', 'colAreaX1', 'colAreaY1',
                                      'pageNum', 'pageX0', 'pageY0', 'pageX1', 'pageY1', 'image'])
    if save:
        df.to_csv(path.replace('.hocr', '.csv'), index=False)
        print(f"Saved as {path.replace('.hocr', '.csv')}")


if __name__ == '__main__':
    parseHOCR('./test/test.hocr', save=True)