#merge random color channels

import cv2
import numpy
import random

image = cv2.imread("../TestImages/waterfall.jpg")

(bc, gc, rc) = cv2.split(image)

zc = numpy.zeros( bc.shape, numpy.uint8 )

x = [bc, gc, rc]
random.shuffle(x)
print x

blueImg = cv2.merge(x)
cv2.imshow("Blue channel", blueImg)

cv2.waitKey(0)
cv2.destroyAllWindows()