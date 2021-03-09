import cv2
import numpy as np

img1 = cv2.imread("car.JPG",1)
img2 = cv2.imread("anh1.JPG",1)

img1 = img1[100: 400, 100: 500]
img2 = img2[100: 400, 100: 500]
img3 = cv2.add(img1, img2)

cv2.imshow('image',img3)
cv2.waitKey(0)
