#start/stop video feed

import cv2

vidCap = cv2.VideoCapture(0)

for i in range(300):
    ret, img = vidCap.read()
    cv2.imshow("Webcam", img)
    x = cv2.waitKey(10)
    if x > -1 and chr(x)=='q':
    	break

cv2.destroyAllWindows()
vidCap.release()