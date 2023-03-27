'''
1. translation
2. rotation
3. resize
4. flip
'''
import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale=0.10):
    width = int(frame.shape[1] * scale)
    heigth = int(frame.shape[0] * scale)
    return cv.resize(frame, (width,heigth), interpolation=cv.INTER_AREA)

# translation: shift image along axes
# Affine transformation: transformation that preserves lines and parallelism but not necessarly euclidian distance
# Remember that black pixels are added by default when rotate/translate
def translate(img, x, y):
    transMAT = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMAT, dimensions)

# Rotation
def rotation(img, angle, rotationPoint=None):
    (height, width) = img.shape[:2]
    
    if rotationPoint == None:
        rotationPoint = (width//2, height//2)
    
    dimensions = (width, height)
    rotMat = cv.getRotationMatrix2D(rotationPoint, angle, 1.0)
    return cv.warpAffine(img, rotMat, dimensions)

URL = 'images-videos/van.jpg'
SCALE = 0.50 

img = cv.imread(URL)
img = rescaleFrame(img, SCALE)
cv.imshow('Original image', img)

trans = translate(img, 100, 100)
cv.imshow('Translate', trans)

rotate = rotation(img, 45)
cv.imshow('Rotate', rotate)

rotateTrans = rotation(trans, 45)
cv.imshow('Rotate + transl', rotateTrans)


# flip
# 0: flip horizontally
# 1: flip vertically
# -1: both vertically and horizontally
flip = cv.flip(img, -1)
cv. imshow('flipped', flip)


cv.waitKey(0)


    