'''
1. Convert image to different color scale (in this case to grayscale)
2. Blur the image
3. Get edges of image with cv.Canny
4. dilated canny image -> get edges larger
5. Eroded
6. Resize
7. Cropped
'''

def rescaleFrame(frame, scale=0.10):
    width = int(frame.shape[1] * scale)
    heigth = int(frame.shape[0] * scale)
    return cv.resize(frame, (width,heigth), interpolation=cv.INTER_AREA)

import cv2 as cv

URL = 'images-videos/van.jpg'
SCALE = 0.50 

img = cv.imread(URL)
img = rescaleFrame(img, SCALE)
cv.imshow('Original image', img)

# Convert to grayscale
# the funtion cvtColor is used to convert an image from one color scale to anoter
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur image
# second parameter is the kernel size
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

# Edge cascade
# Note that if we pass to cv.Canny the blurred image, the edges are less and only the one more relevant
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

# Dilatating image
dilated = cv.dilate(canny, kernel=(10,10), iterations=3)
cv.imshow('Dilated', dilated)

# Erode image
# if we dilate+erode on same image we go back to the original 
eroded = cv.erode(canny, kernel=(10,10), iterations=1)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 50:200]
cv.imshow('Cropped', cropped)

cv.waitKey(0)