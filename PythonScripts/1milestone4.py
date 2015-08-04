import cv2

vidCap = cv2.VideoCapture(0)

shouldQuit = 0;
while not shouldQuit:
    ret, img = vidCap.read()
    cv2.imshow("Webcam", img)
    x = cv2.waitKey(10)
    if x > -1 and chr(x) =='q':
    	shouldQuit = 1;

vidCap.release()
cv2.destroyAllWindows()
