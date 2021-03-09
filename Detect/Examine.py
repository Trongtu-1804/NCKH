import cv2 as cv
import numpy as np



cap = cv.VideoCapture(0)

while(1):
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    #Establece los intervalos de el color de piel
    low_skin = np.array([0,5,0])
    up_skin = np.array([65,165,165])

    #Guarda esa matriz en mask
    mask = cv.inRange(hsv, low_skin, up_skin)
    #cv.imshow('Segmentacion',mask)

    #Lleva los pixeles de 255 a 1 para multiplicarlo despues
    _,mask = cv.threshold(mask,127,255,cv.THRESH_BINARY)

    #Erosion del frame
    element_E = cv.getStructuringElement(cv.MORPH_ELLIPSE, (2*5 + 1, 2*5+1), (5, 5))
    Ero = cv.erode(mask, element_E)

    #Dilatacion de los elemntos previa erosion
    element_D = cv.getStructuringElement(cv.MORPH_ELLIPSE, (2*11 + 1, 2*11 + 1), (11, 11))
    dil = cv.dilate(Ero, element_D)

    #Multiplica ambas matrices
    res = cv.bitwise_and(frame,frame,mask=mask)

    cv.imshow('Actual',res)
    cv.imshow('Salida',frame)
    print('Mask')
    print( mask.shape )
    print( mask.dtype )
    print('Dil')
    print( dil.shape )
    print( dil.dtype )


    k = cv.waitKey(30)
    if k == ord('q') or k == 27:
        break

cv.destroyAllWindows()
cap.release()
