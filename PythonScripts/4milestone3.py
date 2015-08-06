#accentuate edges and detect lines
import cv2
import numpy

img = cv2.imread("../TestImages/Puzzle1.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cannyImg = cv2.Canny(gray, 255, 255)
f = cv2.addWeighted(gray,2,cannyImg,-1,0)
fCanny = cv2.Canny(gray,255,255)


lines = cv2.HoughLinesP(fCanny, 2, numpy.pi/2, threshold = 5, minLineLength = 50, maxLineGap = 7)
for lineSet in lines:
    for line in lineSet:
        cv2.line(img, (line[0], line[1]), (line[2], line[3]), (255, 0, 255))

# cv2.cvtColor(f, cv2.GRAY2BGR)
cv2.imshow("O", img)
# cv2.imshow("AL", fCanny)
cv2.waitKey(0)
cv2.destroyAllWindows()