#geometric transformations

import cv2
import numpy

Img = cv2.imread("../TestImages/SnowLeo2.jpg")

h, w ,c = Img.shape

angle=0
clicked = 0

c1x = 0
c1y = 0
c2x = h
c2y = 0
c3x = 0
c3y = w
tv = 0
th = 0
while(not clicked):
	x=cv2.waitKey(10)
	if (x>-1) and (chr(x) =='s'):
		clicked=1
		break
	elif (x>-1) and (chr(x) =='w'):
		tv+=10
	elif (x>-1) and (chr(x) =='a'):
		th-=10
	elif (x>-1) and (chr(x) =='s'):
		tv-=10
	elif (x>-1) and (chr(x) =='d'):
		th+=10

	angle +=5
	rMat = cv2.getRotationMatrix2D( (w / 2, h / 2), angle, 1)
	img = cv2.warpAffine(Img, rMat, (w, h))

	origPts = numpy.float32([[c1x, c1y], [c2x, c2y], [c3x, c3y]])
	newPts = numpy.float32([[c1x+th, c1y+tv], [c2x+th, c2y+tv], [c3x+th, c3y+th]])
	mat = cv2.getAffineTransform(origPts, newPts)
	warpImg = cv2.warpAffine(img, mat, (h, w))

	cv2.imshow("Rotated", img)
	cv2.imshow("Rotated", warpImg)


cv2.waitKey(0)
cv2.destroyAllWindows()




