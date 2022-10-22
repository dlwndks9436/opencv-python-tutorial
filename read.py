import cv2 as cv

# Read image

# img = cv.imread('photos/cat_large2.jpeg')

# cv.imshow('Cat', img)

# cv.waitKey(0)

# Read video

capture = cv.VideoCapture('videos/sample.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break
  
capture.release
cv.destroyAllWindows()
