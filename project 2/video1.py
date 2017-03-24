
import os,sys
# from SimpleCV import Camera

# def shot():
#     cam = Camera()
#     time.sleep(0.1)  # If you don't wait, the image will be dark
#     img = cam.getImage()
#     img.save("/Users/josephroshen1234/Desktop/ocr/image/pic1.png")

# if __name__ == '__main__':
#     shot()

# import time
# import cv2
# def shot():
#      camera_port = 0
#      camera = cv2.VideoCapture(camera_port)
#      time.sleep(0.25)  # If you don't wait, the image will be dark
#      return_value, image = camera.read()
#      cv2.imwrite("/Users/josephroshen1234/Desktop/ocr/image/pic1.png", image)
#      del(camera)  # so that others can use the camera as soon as possible

# if __name__ == '__main__':
#      shot()



import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    rgb_grey=cv2.imshow('/Users/josephroshen1234/Desktop/ocr/camera/frame.png',gray)
    #cv2.imwrite('rgb_grey.png')
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
