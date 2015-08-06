import cv2
import os
import histogramDemo.py

img = cv2.imread("../TestImages/shops.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([gray], [0], None, [8], [0, 256])
#os.system("python histogramDemo.py img")
# hist_curve(img)
print this

cv2.waitKey(0)
	