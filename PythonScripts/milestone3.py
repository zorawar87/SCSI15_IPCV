import cv2
import numpy

sl2 = cv2.imread("../TestImages/SnowLeo2.jpg")

cv2.circle(sl2, (130, 135), 65, (255,255,255), -1)
cv2.rectangle(sl2, (260, 320), (540, 85), (0, 0,0), -1)
cv2.line(sl2, (555, 125), (600, 392), (0, 0, 255))
cv2.ellipse(sl2, (120,385), (50, 10), 15, 0, 360, (250, 180, 110), -1)
cv2.ellipse(sl2, (410,422), (20, 5), -15, 0, 360, (250, 180, 110), -1)
cv2.ellipse(sl2, (535,430), (20, 10), 15, 0, 360, (250, 180, 110), -1)

cv2.imshow("SnowLeo2.jpg", sl2)
cv2.imwrite("SnowLeo2.jpg", sl2)

cv2.waitKey(0)
cv2.destroyAllWindows()
