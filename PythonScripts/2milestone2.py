#blend images, continually change blend

import cv2
import numpy

img1 = cv2.imread("../TestImages/redDoor.jpg")
img2 = cv2.imread("../TestImages/SnowLeo1.jpg")

h1, w1, c1 = img1.shape

img2 = img2[0:h1,0:w1]
a =1
b =0

f = cv2.addWeighted(img1,a,img2,b,-10)
cv2.imshow("Weighted", f)
cv2.waitKey(0)
cv2.destroyWindow("Weighted")

while(a>0 and b<1):
	a-=0.1
	b+=0.1
	f = cv2.addWeighted(img1,a,img2,b,-10)
	cv2.imshow("Weighted", f)
	cv2.waitKey(0)
	print "End", a, b

cv2.waitKey(0)
cv2.destroyAllWindows()