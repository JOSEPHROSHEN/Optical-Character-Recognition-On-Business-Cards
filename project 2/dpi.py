import os, sys
import PIL
from PIL import Image
def test():
    print 'hello world'
    basewidth = 900
    img = Image.open('/Users/josephroshen1234/Desktop/ocr/project/img/dpi1.jpg')
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
    img.save('/Users/josephroshen1234/Desktop/ocr/project/img/dpi1.jpg',dpi=(1000,1000)) 

if __name__ == '__main__':
    test()