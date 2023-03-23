
'''
Functions for read an image, read a video (frame-by-frame) and rescale
'''

import cv2 as cv
print(cv.__version__)

def read_image(path:str):
    # can access with relatively path because it is in my directory
    img = cv.imread(path)
    cv.imshow('me',img)
    #wait until one key is pressed (in this time infinite)
    cv.waitKey(0)
    
def read_video(path:str, scale:int):
    # if instead path we pass 0/1/... -> webcam/cameras connected to computer
    capture = cv.VideoCapture(path)
    while True:
        isFrame, frame = capture.read()
        frame_resized = rescaleFrame(frame, scale)
        cv.imshow('video', frame)
        cv.imshow('video resized',frame_resized)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break
    capture.release()
    cv.destroyAllWindows()

def rescaleFrame(frame, scale=0.10):
    width = int(frame.shape[1] * scale)
    heigth = int(frame.shape[0] * scale)
    return cv.resize(frame, (width,heigth), interpolation=cv.INTER_AREA)


#read_image('./images-videos/me.JPG')
read_video('./images-videos/osella.mp4', 0.8)