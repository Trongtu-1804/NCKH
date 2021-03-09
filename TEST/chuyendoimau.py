import cv2
import numpy as np

img = np.uint8([[[76, 177, 34]]]);
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV);
print (hsv_img)
img2 = cv2.imread("vebay.png",1);
hsv_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV);
min_mau = np.array([69, 206, 177])
max_mau = np.array([72, 206, 177])
mask = cv2.inRange(hsv_img2, min_mau, max_mau);
final = cv2.bitwise_and(img2,img2, mask=mask);
cv2.imshow("abc",final);
cv2.waitKey(0);
