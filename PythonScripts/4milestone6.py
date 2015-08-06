#posterise image

import cv2 as ii
import numpy

img = ii.imread("../TestImages/shops.jpg")
ii.imshow("a",img)
n=2
indices = numpy.arange(0,256)
divider = numpy.linspace(0,255,n+1)[1]
quantiz = numpy.int0(numpy.linspace(0,255,n))
color_levels = numpy.clip(numpy.int0(indices/divider),0,n-1)
palette = quantiz[color_levels]

img = palette[img]
img = ii.convertScaleAbs(img)

ii.imshow('posterise',img)
ii.waitKey(0)
ii.destroyAllWindows()