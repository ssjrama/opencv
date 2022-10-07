import cv2 as cv

img = cv.imread('Photos/cat_large.jpg')
cv.imshow('Cat', img)

def rescaleFrame(fram, scale=0.75):
    # image, video, live video
    width = int(fram.shape[1] * scale)
    height = int(fram.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(fram,dimensions,interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img,.5)
cv.imshow('Image', resized_image)

def changeRes(width,height):
    # live video
    capture.set(3,width)
    capture.set(4,height)

# Reading Videos
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=.2)
    cv.imshow('VIdeo',frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()