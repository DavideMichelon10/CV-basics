'''
How to switch between color spaces
Different maps: BGR, RGB, gray, lab, HSV, ...
OpenCV uses BGR wheras matplotlib uses RGB
'''
import cv2 as cv
import numpy as np

img = cv.imread('images-videos/people.jpg')

img = cv.resize(img, (700, 600), interpolation=cv.INTER_AREA)

cv.imshow('Original', img)

# BGR to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

gray2bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
cv.imshow('gray2bgr', gray2bgr)

cv.waitKey(0)