import cv2

img = cv2.imread("../TestImages/SnowLeo1.jpg")

cv2.imshow("Snow Leopard", img)

cv2.waitKey(0)
cv2.destroyAllWindos()