'''

'''

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def rescaleFrame(frame, scale=0.10):
    width = int(frame.shape[1] * scale)
    heigth = int(frame.shape[0] * scale)
    return cv.resize(frame, (width,heigth), interpolation=cv.INTER_AREA)


img = cv.imread('images-videos/people.jpg')
blank=np.zeros((400,400), dtype='uint8')
img = rescaleFrame(img, 0.51)
img = img[0:400, 0:400]

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('gray', gray)

# Laplacian: it computes the gradient of image
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel computes the gradient along two directions 
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('sobelx', sobelx)
cv.imshow('sobely', sobely)
cv.imshow('combined_sobel', combined_sobel)
cv.imshow('canny', cv.Canny(gray, 150, 150))
# Laplacian vs sobel vs canny
# 1. Laplacian. "paintful" shading. Not much used
# 2. combined sobel: gradient in x and y and combine. Used only in some advanced case
# 3. Canny is more advanced which uses sobel in one of the stage. Canny very clean and used
cv.waitKey(0)