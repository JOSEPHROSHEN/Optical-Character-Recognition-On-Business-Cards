import os,sys
import glob
import re

def the():
    # file=glob.glob('/Users/josephroshen1234/Desktop/ocr/project/img/*.jpg')
    # file=extend(glob.glob('/Users/josephroshen1234/Desktop/ocr/project/img/*.png'))
    # print file
    fileNames = []
    for x in os.listdir('/Users/josephroshen1234/Desktop/ocr/project/img/'):
        if re.match('.*\.jpg|.*\.png', x):
            print x
            fileNames.append(x)
            print fileNames

if __name__ == '__main__':
    the()
    

