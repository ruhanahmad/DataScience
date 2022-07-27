
import numpy as np
import cv2 
img = cv2.imread("resource/don.jpg")
img = cv2.resize(img,(800,600))
cv2.imshow("phli image",img)
cv2.waitkey(0)