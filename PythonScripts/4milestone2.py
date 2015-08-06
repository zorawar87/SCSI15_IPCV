#color replacement
import cv2 as ii
import cv2
import numpy

img = ii.imread("../TestImages/shops.jpg")
ii.imshow("a",img)
print img
img = ii.cvtColor(img,ii.COLOR_BGR2HSV)
print "spli"
(h,s,v) = ii.split(img)
print h
h[:][numpy.where(numpy.logical_and(14<=h, h<=16))] = [180]

img = ii.merge((h,s,v))
img = ii.cvtColor(img,ii.COLOR_HSV2BGR)

ii.imshow('v',img)
ii.waitKey(0)
ii.destroyAllWindows()