#greyscale image

import cv2
import numpy

image = cv2.imread("../TestImages/SnowLeo4.jpg")
print image.shape
print image.size
print image.dtype
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray image", gray)
cv2.imshow("Gray image", image)
blackImg = numpy.zeros((150, 250), numpy.uint8)
cv2.imshow("Blank image", blackImg)

cv2.waitKey(0)
cv2.destroyAllWindows()