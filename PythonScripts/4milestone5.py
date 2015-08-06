#Add Noise
import cv2 as ii
import cv2
import numpy
import time

start_time = time.time()

IMG = ii.imread("../TestImages/shops.jpg")
ii.imshow("image", IMG)

h, w, c = IMG.shape


def TransformPos():
	origP = numpy.float32([[40, 40], [160, 40], [40, 160]])
	newP = numpy.float32([[60, 60], [180, 60], [60, 195]])

	mat = ii.getAffineTransform(origP, newP)
	warpImg = ii.warpAffine(IMG, mat, (w, h))
	ii.imshow("image", warpImg)


def ThreshIm():
	res, img = cv2.threshold(IMG, 225, 225, cv2.THRESH_BINARY)
	ii.imshow("image", img)

'''
def RthresIm():


def shapenIm():
'''

def BackProject():
	hsv = cv2.cvtColor(IMG, cv2.COLOR_BGR2HSV)
	(h, s, v) = cv2.split(hsv)
	hist = cv2.calcHist([h], [0], None, [256], [0, 256])
	bp = cv2.calcBackProject([hsv], [0], hist, [0, 256], 1)
	cv2.imshow("image", bp)

def HLP():
	grayImg = cv2.cvtColor(IMG, cv2.COLOR_BGR2GRAY)
	cannyImg = cv2.Canny(grayImg, 100, 200)
	lines = cv2.HoughLinesP(cannyImg, 1, numpy.pi/180, threshold = 5, minLineLength = 20, maxLineGap = 10)
	for lineSet in lines:
		for line in lineSet:
		    cv2.line(IMG, (line[0], line[1]), (line[2], line[3]), (255, 255, 0))


def UndoEffect():
	ii.imshow("image", IMG)

while True:
	key = ii.waitKey(1)

	loopTime = time.time()
	et = int(start_time - loopTime)
	# sharpen(loopTime)
	if (et%3 == 0):
		TransformPos()
	elif (et%3 == 1):
		UndoEffect()

	loopTime = time.time()
	et = int(start_time - loopTime)
	if (et%5 == 2):
		BackProject()
	elif (et%5 == 4):
		UndoEffect()

	loopTime = time.time()
	et = int(start_time - loopTime)
	if (et%4 == 3):
		HLP()
	elif (et%5 == 0):
		UndoEffect()

	loopTime = time.time()
	et = int(start_time - loopTime)
	if (et%6 ==3):
		ThreshIm()
	elif (et%6 ==1):
		UndoEffect()

	if key > -1 and chr(key)=='q':
		ii.destroyAllWindows()
		break

cv2.waitKey(0)
cv2.destroyAllWindows()