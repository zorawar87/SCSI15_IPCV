#find Face
import cv2


vidCap = cv2.VideoCapture(0)
ret, img = vidCap.read()
                                         

cv2.imshow("Original 1", img)

                                                
#replace sift with surg and vice versa
# create a SIFT object, that can run the SIFT algorithm.

SIFT = cv2.xfeatures2d.SIFT_create(400)

                                                

keypts, des = SIFT.detectAndCompute(img, None)

print "Number of keypoints found:", len(keypts)

                                                

img2 = cv2.drawKeypoints(img, keypts, None, (255, 0, 0), 4)

cv2.imshow("Keypoints 1", img2)

cv2.waitKey(0)

cv2.destroyAllWindows()