'''
Split the image in 3 color channels
1. cv.split divides the image in 3 channels
2. cv.merge -> merges single channel in one image
'''

import cv2 as cv
import numpy as np

img = cv.imread('images-videos/van.jpg')

img = cv.resize(img, (700, 600), interpolation=cv.INTER_AREA)

b,g,r = cv.split(img)
cv.imshow('b', b) # light color means -> big concentration
cv.imshow('g', g)
cv.imshow('r', r)
# output: shape of original: (600, 700, 3), shape b: (600, 700). Only one channel (oc!)
print(f"shape of original: {img.shape}, shape b: {b.shape}")

merged = cv.merge([b,g,r])
cv.imshow('merged', merged)

# obtain each color channel with their color-scale

blank = np.zeros(img.shape[:2], dtype='uint8')
red = cv.merge([blank, blank, r])
green = cv.merge([blank, g, blank])
blue = cv.merge([b, blank, blank])

cv.imshow('only red color', red)
b1,g1,r1 = cv.split(blue)
b2,g2,r2 = cv.split(green)
b3,g3,r3 = cv.split(red)

merged = cv.merge([b1, g2, r3])
cv.imshow('re-merge colors',merged)


cv.waitKey(0)