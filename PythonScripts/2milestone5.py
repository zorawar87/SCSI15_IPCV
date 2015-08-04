#VidMorph

import cv2
import numpy

vidCap = cv2.VideoCapture(0)
shouldQuit = 0

while (not shouldQuit):
	ret, img = vidCap.read()

	img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# cv2.imshow("greyscale",img1)

	img2 = cv2.GaussianBlur(img, (25, 25), 15)
	# cv2.imshow("Blur",img2)

	res, img3 = cv2.threshold(img2, 125, 225, cv2.THRESH_TOZERO)
	cv2.imshow("Binary threshold",img3)

	x = cv2.waitKey(10)
	if x > -1 and chr(x) =='q':
		shouldQuit = 1;

vidCap.release()
cv2.destroyAllWindows()

