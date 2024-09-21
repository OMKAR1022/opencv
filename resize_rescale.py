import cv2 as cv

img = cv.imread('photos/an.jpg')

cv.imshow("anime",img)


def rescale(frame,scale = 0.75):
    width = int (frame.shape[1] * scale)
    height = int (frame.shape[0] * scale)

    dimension = (width,height)

    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)


#Image

resiz_img = rescale(img)
cv.imshow("image",resiz_img)

#Video
capture = cv.VideoCapture('videos/obstacle.mp4')

while True:
    isTrue , frame = capture.read()
    frame_resiz = rescale(frame)

    cv.imshow('video',frame)
    cv.imshow('resizze',frame_resiz)

    if cv.waitKey(20) & 0xff == ('d'):
        break

capture.release()
cv.destroyAllWindows()

