import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

#coverting to greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Blur
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

#Edge cascade
canny = cv.Canny(img, 125,175)
cv.imshow('Canny', canny)

#Dilating the image
dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('Dilated', dilated)

cv.waitKey(0)