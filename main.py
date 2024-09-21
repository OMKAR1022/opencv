import cv2 as cv

#Read pic
#img = cv.imread('photos/an.jpg')

#cv.imshow("anime",img)

#cv.waitKey(0)


# Read Video
capture = cv.VideoCapture('videos/obstacle.mp4')

while True:
    isTrue, frame = capture.read()

    cv.imshow('Ob_Detection',frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()