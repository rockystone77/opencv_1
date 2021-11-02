import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

blank[200:300, 300:400] = 0,255,0
cv.imshow('Green', blank)

#draw a rectangle
cv.rectangle(blank, (0,0), (250,250) , (0,255,0), thickness=2)
cv.imshow('Rectangle', blank)

cv.circle(blank, (250,250), 40, (0,0,255), thickness=-1)
cv.imshow('Circle', blank)



cv.waitKey(0)

