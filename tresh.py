'''
1. Fixed treshold: it has problem with image with different lights
2. Adaptive treshold: gaussian or mean. The treshold is the average/gaussian of the neighbours
'''

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def rescaleFrame(frame, scale=0.10):
    width = int(frame.shape[1] * scale)
    heigth = int(frame.shape[0] * scale)
    return cv.resize(frame, (width,heigth), interpolation=cv.INTER_AREA)

img = cv.imread('images-videos/van.jpg')
blank=np.zeros((400,400), dtype='uint8')
img = rescaleFrame(img, 0.51)
img = img[0:400, 0:400]

cv.imshow('Original', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# Simple tresholding

# second term is the treshold number
#third term is, when a pixel is positevly tresholded, which value assign to it
# threshold is the same value we passed, tresh is the new image
treshold, tresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
cv.imshow('threshold image ', tresh)

# Invert treshold
treshold, tresh_inv = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)
# cv.imshow('Inverted threshold image ', tresh_inv)

# Adaptive treshold
# We let the computer to find the optimal treshold by analyzing the neighbours. 
# So we have different treshold for different areas in the image
# The treshold is the mean of the neighbours
adaptive_tresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 0)
cv.imshow('Adaptive threshold image ', adaptive_tresh)

adaptive_tresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 0)
cv.imshow('Gaussian threshold image ', adaptive_tresh)



cv.waitKey(0)