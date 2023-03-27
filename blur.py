'''
link doc: https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html
1. average blur
2. gaussian blur
3. median blur
4. bilateral blur
'''

import cv2 as cv
import numpy as np

kernel = (3,3)
img = cv.imread('images-videos/van.jpg')

img = cv.resize(img, (700, 600), interpolation=cv.INTER_AREA)

cv.imshow('Original', img)

average = cv.blur(img, kernel)
cv.imshow('Average blur', average)

# gaussian is less blurred, because it uses a weighted average
gaussian = cv.GaussianBlur(img, kernel, 0)
cv.imshow('Gaussian blur', gaussian)

# median blurred. Same as average but it chooses the media
median = cv.medianBlur(img, 3)
cv.imshow('Median blur', median)

# bilateral blurring: used in a lots of advanced CV -> blurred images but keeps the corners
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)


cv.waitKey(0)