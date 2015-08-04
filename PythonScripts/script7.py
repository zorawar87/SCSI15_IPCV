#crop image

import cv2
import numpy

image = cv2.imread("../TestImages/shops.jpg")
subImg = image[0:100, 0:200]
cv2.imshow("Subimage", subImg)

cv2.waitKey(0)
cv2.destroyAllWindows()