#corner detection

import cv2
import numpy

img1 = cv2.imread("../TestImages/Puzzle1.jpg")
grayImg = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
goodFeats = cv2.goodFeaturesToTrack(grayImg, 10000, 0.1, 20)

print len(goodFeats)

for circleSet in goodFeats:
	for i in circleSet:
		cv2.circle(grayImg,(i[0],i[1]), 10,(0,255,0),2)
		cv2.circle(grayImg,(i[0],i[1]),1,(0,0,0),3)


cv2.imshow("Corner", grayImg);

cv2.waitKey(0)
cv2.destroyAllWindows()