import cv2

img1 = cv2.imread("../TestImages/SnowLeo3.jpg")
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

img2 = cv2.imread("../TestImages/SnowLeo2.jpg")
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

hist = cv2.calcHist([gray1], [0], None, [256], [0, 256])
bp = cv2.calcBackProject([gray2], [0], hist, [0, 256], 1)
cv2.imshow("BackProject", bp)

cv2.waitKey(0)
cv2.destroyAllWindows()