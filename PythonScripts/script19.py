#hough lines transform in real time video
import cv2
import numpy

vidCap = cv2.VideoCapture(0)

while True:
	ret, img = vidCap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	cannyImg = cv2.Canny(gray, 150, 255)
	lines = cv2.HoughLinesP(cannyImg, 1, numpy.pi/180, threshold = 5, minLineLength = 20, maxLineGap = 10)

	for lineSet in lines:
	    for line in lineSet:
	        cv2.line(img, (line[0], line[1]), (line[2], line[3]), (255, 255, 0))

	cv2.imshow("HoughLinesP", img)
	cv2.imshow("Canny", cannyImg)
	x = cv2.waitKey(10)
	if x > -1 and chr(x)=='q':
		cv2.destroyAllWindows()
		break

cv2.destroyAllWindows()
vidCap.release()