'''
Two different methods two find contours:
1. Canny algorithm + cv.findContours
1.1 Blur the image before algorithm -> less contours
2. Binarize image (cv.treshold), find contours

We then added the contours on a blank image

'''

import cv2 as cv
import numpy as np

img = cv.imread('images-videos/people.jpg')
img = cv.resize(img, (700, 600), interpolation=cv.INTER_AREA)
print(f'image shape: {img.shape}')
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Original', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grey', gray)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

# we find contours using the function cv.findCountours
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f"{len(contours)} contour(s) in the image")

# By adding a blur image we have much less countours
blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 125, 175)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f"{len(contours)} contour(s) in the blurred image")
cv.imshow('Blur + Canny', canny)

# Binarization of image. If pixel < 125 -> 0, oterwhise -> 1
ret, tresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
contours, hierarchies = cv.findContours(tresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f"{len(contours)} contour(s) in the tresholded image")
cv.imshow('Trash image', tresh)

cv.drawContours(blank, contours, -1, (0,0,255), 2)
cv.imshow('Blank with contours ', blank)

cv.waitKey(0)