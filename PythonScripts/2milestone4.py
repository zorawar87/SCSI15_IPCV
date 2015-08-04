#sharpen image 

import cv2
import numpy

img = cv2.imread("../TestImages/SnowLeo2.jpg")
# blur = cv2.GaussianBlur(img, (3, 3), 0)
blur = cv2.blur(img, (3, 3), 15)

f = cv2.addWeighted(img,2,blur,-1,0)

cv2.imshow("O", img)
cv2.imshow("Sharpened", f)
cv2.waitKey(0)
cv2.destroyAllWindows()