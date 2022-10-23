import cv2 as cv

img = cv.imread("photos/couple.jpeg")
cv.imshow("People", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray people", gray)

haar_cascade = cv.CascadeClassifier("./haar_face.xml")

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
print(f"Number of faces found: {len(faces_rect)}")

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 1)

cv.imshow("People", img)

cv.waitKey(0)