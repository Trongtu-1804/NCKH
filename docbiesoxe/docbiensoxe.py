##LOAD THU VIEN VA MODUL CAN THIET
import numpy as np
import cv2
import pytesseract
import matplotlib.pyplot as pit
from PIL import Image
#----------------------DOC HINH ANH - TACH HINH ANH NHAN DIEN---------------
img = cv2.imread('1.jpg')
cv2.imshow(' HINH ANH GOC', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
contours,h = cv2.findContours(thresh,1,2)
largest_rectangle = [0,0]
for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    if len(approx)==4:
        area = cv2.contourArea(cnt)
        if area > largest_rectangle[0]:
            largest_rectangle = [cv2.contourArea(cnt), cnt, approx]
x,y,w,h = cv2.boundingRect(largest_rectangle[1])

image = img[y:y+h,x:x+w]
cv2.drawContours(img,[largest_rectangle[1]],0,(0,255),8)

cropped = img[y:y+h,x:x+w]
cv2.imshow('DANH DAU DOI TUONG', img)

cv2.drawContours(img,[largest_rectangle[1]],0,(255,255,255),18)
#cv2.imshow('CAT KHUNG BIEN SO', img)

#----------------DOC HINH ANH CHUYEN THANH FILE TEXT-----------
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Admin\AppData\Roaming\Python\Python38\site-packages\tesseract.exe'
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3,3), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU) [1]
cv2.imshow('crop', thresh)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations = 1)
invert = 255 - opening
data = pytesseract.image_to_string(invert, lang = 'eng', config = '--psm 6')
print("THONG TIN NHAN DIEN:")
print(data)
cv2.waiKey()
