import cv2
import numpy

image = cv2.imread("../TestImages/waterfall.jpg")
cv2.imshow("Original Image", image)
cv2.waitKey(0)

(bc, gc, rc) = cv2.split(image)

zc = numpy.zeros( bc.shape, numpy.uint8 )

blueImg = cv2.merge((bc, zc, zc))
cv2.imshow("Blue channel", blueImg)

greenImg = cv2.merge((zc, gc, zc))
cv2.imshow("Green channel", greenImg)

redImg = cv2.merge((zc, zc, rc))
cv2.imshow("Red channel", redImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

final = cv2.merge (blueImg, greenImg)
final = cv2.merge (redImg, final)
print final
# cv2.imshow("Final",final)
cv2.waitKey(0)