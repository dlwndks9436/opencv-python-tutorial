import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow('Blank', blank)
# print("blank = ", blank)

# 1. Paint the image a certain color
# blank[400:500, 100:200] = 0,0,255
# cv.imshow('Green', blank)

# 2. Draw a Rectangle
# cv.rectangle(blank, (0,0),(blank.shape[1]//3, blank.shape[0]//2), thickness=-1, color=(0,255,0))
# cv.imshow("Rectangle", blank)

# 3. Draw a circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=cv.FILLED)
# cv.imshow('Circle', blank)

# 4. Draw a line
# cv.line(blank, (100,250),(300, 400), thickness=3, color=(255,255,255))
# cv.imshow("Line", blank)

# 5. Write text
cv.putText(blank, 'Hello, my name is David!!', (0,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow("Text", blank)

cv.waitKey(0)