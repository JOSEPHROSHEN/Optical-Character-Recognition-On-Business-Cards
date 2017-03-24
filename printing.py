import os,sys
import glob
import re
from parsing import parser

def play():
    print 'play_function is called'
    fileList = []

    for x in os.listdir('/Users/josephroshen1234/Desktop/desktop/ocr/project/img/'):
        if re.match('.*\.jpg|.*\.png', x):
            fileList.append(x)
    parser(fileList)
    #        print x
    #       fileNames.append(x)
    #        print fileNames
    #        parser(fileNames)


