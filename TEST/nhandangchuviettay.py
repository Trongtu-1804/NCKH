import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('digits.png',0)

cells = [np.hsplit(row, 100) for row in np.vsplit(img, 50)]

x = np.array(cells)

xx = x[0,0].reshape(-1, 400)
cv2.imwrite('anh1.jpg',xx)

