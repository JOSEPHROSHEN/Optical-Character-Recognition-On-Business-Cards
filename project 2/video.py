import os,sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
cap = cv2.VideoCapture('/Users/josephroshen1234/Desktop/The..Last.Witch.Hunter.2015.HDRip.XviD.AC3-EVO/sample.avi')
while(True):
    ret, frame = cap.read()
 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('/Applications/VLC',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        cap.release()
        cv2.destroyAllWindows()