import os, sys
import pytesseract
import PIL
from PIL import Image
import subprocess
from mongodv import mongoclient

def parser(fileNames):
     #imgConvertedString = ''
    print 'Parser Method Is Parsing'
    directoryName = '/Users/josephroshen1234/Desktop/desktop/ocr/project/img/'
   

    for element in fileNames:
        imgFile = getResizedImageFromFilePath(directoryName, element)
        imgConvertedString = pytesseract.image_to_string(imgFile, lang='eng')
        #mongoclient(imgConvertedString)
        #subprocess.call(["say","Hello!"+imgConvertedString])
        #ExtractedData=[]
        print imgConvertedString
        status = mongoclient(imgConvertedString,element)
        if (status):
            os.remove(os.path.join(directoryName, element))
            os.remove(os.path.join(directoryName + 'new/', element))
            subprocess.call(["say","Hello!"+imgConvertedString])


def getResizedImageFromFilePath(directory, filename):
    basewidth = 900
    img = Image.open(directory + filename)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))

    newDirPath = directory + 'new/'
    if os.path.exists(newDirPath) == False:
        os.mkdir(newDirPath)

    newFilepath = newDirPath + filename
    img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
    img.save(newFilepath,dpi=(1000,1000))
    return img
#def say(text):
    #subprocess.call("say " + text, shell=True)

try:
    import Image
except ImportError:
    from PIL import Image
    print 'Image Is Getting Parsed'
