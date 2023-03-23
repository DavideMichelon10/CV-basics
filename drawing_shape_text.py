'''
How to draw (rectangle, circle, line) and add text on image
'''

import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale=0.10, width=None, heigth=None):
    if width==None and heigth==None:
        width = int(frame.shape[1] * scale)
        heigth = int(frame.shape[0] * scale)
    return cv.resize(frame, (width,heigth), interpolation=cv.INTER_AREA)

img = cv.imread('./images-videos/snow.jpg')

# to write on image we create a blank image
blank = np.zeros((500,500,3), dtype='uint8')

#create green rectangle
# blank[200:300,120:220:,:] = 0,255,0

# draw rectangle
cv.rectangle(blank, (250,0), (250,500), (0,255,0), thickness=2)
#cv.rectangle(blank, (250,0), (250,500), (0,255,0), thickness=cv.FILLED)
cv.imshow('green rectangle', blank)

# draw circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 50, (0,0,255), thickness=cv.FILLED)
cv.imshow('Circle', blank)

# draw line
cv.line(blank, (0,0), (blank.shape[1], blank.shape[0]), (255,0,255), thickness=2)
cv.imshow('Line', blank)

# draw text
blank = np.zeros((500,500,3), dtype='uint8')

cv.putText(blank, 'Hello mum', (0,200), cv.FONT_HERSHEY_TRIPLEX, 1, (255,0,255), thickness= 2)
cv.imshow('text', blank)

cv.waitKey(0)