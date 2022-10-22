import cv2 as cv

# img = cv.imread('Photos/cat_large.jpeg')
# cv.imshow('Cat', img)

def rescaleFrame(frame, scale = 0.75):
    # Images, Videos, and Live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
  
def changeRes(width, height):
    # Live videos only
    capture.set(3, width)
    capture.set(4, height)
    
# Read video
capture = cv.VideoCapture('videos/sample.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('video', frame)
    cv.imshow('video resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break
  
capture.release
cv.destroyAllWindows()
