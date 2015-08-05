''' interactive program to test out the feature detection:
	let the user modify the parameters and/or select different images
'''

import cv2
import numpy
import argparse

lowerlim = 0
upperlim = 255

instr = '''
	w to increase lower limit
	s to decrease lower limit
	e to increase upper limit
	d to decrease upper limit
'''
print instr

while True:
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	cannyImg = cv2.Canny(gray, lowerlim, upperlim)
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
	elif x > -1 and chr(x)=='w':
		lowerlim +=5
		print "lowerlim is now" + str(lowerlim)
	elif x > -1 and chr(x)=='s':
		print "lowerlim is now" + str(lowerlim)
		lowerlim -=5
	elif x > -1 and chr(x)=='e':
		upperlim +=5
		print "ulim is now" + str(upperlim)
	elif x > -1 and chr(x)=='d':
		upperlim -=5
		print "ulim is now" + str(upperlim)

cv2.destroyAllWindows()
vidCap.release()