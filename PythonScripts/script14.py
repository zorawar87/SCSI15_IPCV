import cv2

img = cv2.imread("../TestImages/sampleRed.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
(h, s, v) = cv2.split(hsv)

door = cv2.imread("../TestImages/shops.jpg")
dhsv = cv2.cvtColor(door, cv2.COLOR_BGR2HSV)

hist = cv2.calcHist([h], [0], None, [256], [0, 256])
bp = cv2.calcBackProject([dhsv], [0], hist, [0, 256], 1)
cv2.imshow("BackProject", bp)
# cv2.imshow("shops.jpg", cv2.imread("../TestImages/shops.jpg"))
cv2.waitKey(0)
cv2.destroyAllWindows()