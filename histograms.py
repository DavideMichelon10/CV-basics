'''
Create a mask and compute the histogram for each color on the masked image
N.B. the mask must be in gray scale
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

circle = cv.circle(blank.copy(), (200,200), 100, 255, -1)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
mask = cv.bitwise_and(gray, gray, mask=circle)

cv.imshow('Original', img)
cv.imshow('Mask', mask)

# compute histogram
# (list of image, number of channels, mask if we want histogram for a portion of image, number of bins)
gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

# plt.figure()
# plt.title('histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# Colour histogram
colors = ('b', 'g', 'r')

mask_color = cv.bitwise_and(img, img, mask=circle)

plt.figure()
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.xlim([0,256])

for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0, 256])
    plt.title(f'Color {i} histogram')
    plt.plot(hist, color=col)

plt.show()
    
cv.imshow('Colour mask', mask_color)

cv.waitKey(0)