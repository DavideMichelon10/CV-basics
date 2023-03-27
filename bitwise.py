'''
bitwise operators: AND, OR, NOT, ... and operate in a binary manner. 
'''

import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale=0.10):
    width = int(frame.shape[1] * scale)
    heigth = int(frame.shape[0] * scale)
    return cv.resize(frame, (width,heigth), interpolation=cv.INTER_AREA)

img = cv.imread('images-videos/van.jpg')
img = rescaleFrame(img, 0.51)
img = img[0:400, 0:400]

print(f"shape of image: {img.shape}")

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, thickness=-1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, thickness=-1)

cv.imshow('Original', img)
cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# bitwise AND --> intersection
bitwise = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise)

# bitwise OR --> intersection & not-intersection
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)

#bitwise XOR --> non-intersection region
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)

# bitwise NOT --> invert pixels in image
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Bitwise NOT', bitwise_not)

cv.waitKey(0)