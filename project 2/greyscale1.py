#gray=CV.cvtcolor('/Users/josephroshen1234/Desktop/ocr/images/Business-card-template-design.jpg',CV.COLOR_BGR2GRAY)
#gray=CV.bitwise_not(gray)
#thresh=CV.threshold(gray,0,255,CV.THRESH_BINARY | CV.THRESH_OTSU)[1]
import os, sys
import pytesseract
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def img_ocr():
     print 'hi..'
    
try:
    import Image
except ImportError:
    from PIL import Image
    print 'image parsing'
    
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

img = mpimg.imread('/Users/josephroshen1234/Desktop/ocr/project/img/capture_image.png')     
gray = rgb2gray(img)    
plt.imshow(gray, cmap = plt.get_cmap('gray'))
# basewidth = 800
# img = Image.open('/Users/josephroshen1234/Desktop/ocr/images/grey2.png')
# wpercent = (basewidth/float(img.size[0]))
# hsize = int((float(img.size[1])*float(wpercent)))
# img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
# img.save('/Users/josephroshen1234/Desktop/ocr/Business451.jpg',dpi=(1000,1000)) 
plt.show()
plt.imsave('/Users/josephroshen1234/Desktop/ocr/images/grey23.jpg')
#img=(thresh) 
# print(pytesseract.image_to_string(Image.open('/Users/josephroshen1234/Desktop/ocr/images/card13.jpg'),lang='eng'))
# print(pytesseract.image_to_string(Image.open('/Users/josephroshen1234/Desktop/ocr/images/Business-card-template-design.jpg')))
#print thresh 
#pytesseract.run_tesseract('image.png','output', lang=None, boxes=False, config="hocr")
# basewidth = 800
# img = Image.open('/Users/josephroshen1234/Desktop/ocr/images/grey.png')
# wpercent = (basewidth/float(img.size[0]))
# hsize = int((float(img.size[1])*float(wpercent)))
# img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
# img.save('/Users/josephroshen1234/Desktop/ocr/Business45.jpg',dpi=(1000,1000)) 

if __name__ == '__main__':
    img_ocr()
    rgb2gray()