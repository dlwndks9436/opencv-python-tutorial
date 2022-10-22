import cv2 as cv
import numpy as np

img = cv.imread("photos/cat.jpeg")
cv.imshow("Cat", img)

blank = np.zeros(img.shape[:2], dtype="uint8")
cv.imshow("Blank Image", blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 200, 255, -1)
# cv.imshow('Mask', mask)

rectangle = cv.rectangle(blank.copy(), (500,500), (970, 970), 255, cv.FILLED)
print("rectangle_shape: ", np.shape(rectangle))

wierd_shape = cv.bitwise_and(circle, rectangle)
cv.imshow("Wierd Shape", wierd_shape)

masked = cv.bitwise_and(img, img, mask=wierd_shape)
cv.imshow('Weird Shaped Masked Image', masked)

cv.waitKey(0)