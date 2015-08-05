#canny edge detection on real time video
import cv2

vidCap = cv2.VideoCapture(0)

while True:
	ret, img = vidCap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	cannyImg = cv2.Canny(gray, 150, 255)
	cv2.imshow("Webcam", cannyImg)
	x = cv2.waitKey(10)
	if x > -1 and chr(x)=='q':
		cv2.destroyAllWindows()
		break

cv2.destroyAllWindows()
vidCap.release()