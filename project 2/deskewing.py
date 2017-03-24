import cv2
import numpy as np
from matplotlib import pyplot as plt



img = cv2.imread('/Users/josephroshen1234/Desktop/ocr/images/bcpage-Slim-Business-Cards_450x450.jpg', cv2.IMREAD_GRAYSCALE)

def compute_skew(image):
    image = cv2.bitwise_not(image)
    height, width = image.shape
    edges = cv2.Canny(image, 150, 200, 3, 5)
    lines= cv2.HoughLinesP(edges, 1, cv2.cv.CV_PI/180, 100, minLineLength=width / 2.0, maxLineGap=20)
    angle = 0.0
    nlines = lines.size
    plt.imshow('/Users/josephroshen1234/Desktop/ocr/project/deskewed.png',image)
    for x1, y1, x2, y2 in lines[0]:
        angle += np.arctan2(y2 - y1, x2 - x1)
        #plt.show('/Users/josephroshen1234/Desktop/ocr')
        matplotlib.image.imsave('/Users/josephroshen1234/Desktop/ocr/project/deskewed.png',  deskewed_image)
        #plt.imshow(/Users/josephroshen1234/Desktop/ocr/project/deskewed.png,'gray')
def deskew(image, angle):
    image = cv2.bitwise_not(image)
    non_zero_pixels = cv2.findNonZero(image)
    center, wh, theta = cv2.minAreaRect(non_zero_pixels)
    root_mat = cv2.getRotationMatrix2D(center, angle, 1)
    rows, cols = image.shape
    rotated = cv2.warpAffine(image, root_mat, (cols, rows), flags=cv2.INTER_CUBIC)
    cv2.getRectSubPix(rotated, (cols, rows), center)
    
deskewed_image = deskew(img.copy(), compute_skew(img))

def main():
    pass

