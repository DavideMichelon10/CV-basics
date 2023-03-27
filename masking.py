'''
Apply bitwise to real image: get a (circle) mask of an original image
N.B. size of mask same as image
'''

import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale=0.10):
    width = int(frame.shape[1] * scale)
    heigth = int(frame.shape[0] * scale)
    return cv.resize(frame, (width,heigth), interpolation=cv.INTER_AREA)

blank = np.zeros((400,400), dtype='uint8')

img = cv.imread('images-videos/van.jpg')
img = rescaleFrame(img, 0.51)
img = img[0:400, 0:400]

mask = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

masked = cv.bitwise_and(img, img, mask=mask)

cv.imshow('Original', img)
cv.imshow('Mask', mask)
cv.imshow('masked', masked)



cv.waitKey(0)