#posterise image

import cv2
import numpy

im = cv2.imread("../TestImages/shops.jpg")
cv2.imshow("a",im)

n = 2

indices = numpy.arange(0,256)   # List of all colors 
divider = numpy.linspace(0,255,n+1)[1] # we get a divider
quantiz = numpy.int0(numpy.linspace(0,255,n)) # we get quantization colors
color_levels = numpy.clip(numpy.int0(indices/divider),0,n-1) # color levels 0,1,2..
palette = quantiz[color_levels] # Creating the palette

im2 = palette[im]  # Applying palette on image
im2 = cv2.convertScaleAbs(im2) # Converting image back to uint8

cv2.imshow('im2',im2)
cv2.waitKey(0)
cv2.destroyAllWindows()