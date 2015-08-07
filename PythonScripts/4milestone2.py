#color replacement
import cv2
import numpy

img = cv2.imread("../TestImages/shops.jpg")
cv2.imshow("a",img)
print img
img[numpy.where((img == [255,255,255]).all(axis = 2))] = [0,0,0]

cv2.imshow('b',img)
cv2.waitKey(0)
cv2.destroyAllWindows()