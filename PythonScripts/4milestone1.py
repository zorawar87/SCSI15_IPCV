
import cv2
import numpy

# Coins2.jpg detection

img = cv2.imread('../TestImages/Coins2.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blurred = cv2.medianBlur(gray, 7)
blurred = cv2.addWeighted(gray,3,blurred,-2,0)

circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,100, param1=30,param2=50,minRadius=50,maxRadius=75)

if len(circles) >=1:
	for circleSet in circles:
		for i in circleSet:
			cv2.circle(blurred,(i[0],i[1]),i[2],(0,255,0),2)
			cv2.circle(blurred,(i[0],i[1]),1,(0,0,255),3)
else:
	print "No circles"

cv2.imshow('detected circles',blurred)
'''

# Coins1.jpg detection
img = cv2.imread('../TestImages/Coins1.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blurred = cv2.medianBlur(gray, 7)
blurred = cv2.addWeighted(gray,3,blurred,-2,0)

circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,70, param1=50,param2=30,minRadius=34,maxRadius=55)

if len(circles) >=1:
	for circleSet in circles:
		for i in circleSet:
			cv2.circle(blurred,(i[0],i[1]),i[2],(0,255,0),2)
			cv2.circle(blurred,(i[0],i[1]),1,(0,0,255),3)
else:
	print "No circles"

cv2.imshow('detected circles',blurred)
'''

cv2.waitKey(0)
cv2.destroyAllWindows()

