#canny edge detection
import cv2

img = cv2.imread("../TestImages/shops.jpg")
# img = cv2.imread("../TestImages/Blowhole013.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cannyImg = cv2.Canny(gray, 255, 255)
cv2.imshow("Canny", cannyImg)

cv2.waitKey(0)
cv2.destroyAllWindows()