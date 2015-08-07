#accentuate edges
import cv2

img = cv2.imread("../TestImages/Puzzle1.jpg")
# img = cv2.imread("../TestImages/Blowhole013.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cannyImg = cv2.Canny(gray, 255, 255)
f = cv2.addWeighted(gray,2,cannyImg,-1,0)

cv2.imshow("Orig", gray)
cv2.imshow("AccentuatedLines", f)
cv2.waitKey(0)
cv2.destroyAllWindows()