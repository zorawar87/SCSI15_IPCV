#compare histograms
import cv2
import numpy as np

img1 = cv2.imread("../TestImages/Blowhole013.jpg")
G1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
Ghist1 = cv2.calcHist([G1], [0], None, [256], [0, 256])

HSV1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
(h1, s1, v1) = cv2.split(HSV1)
Hhist1 = cv2.calcHist([h1], [0], None, [256], [0, 256])


img2 = cv2.imread("../TestImages/Blowhole021.jpg")
G2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
Ghist2 = cv2.calcHist([G2], [0], None, [256], [0, 256])

HSV2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
(h2, s2, v2) = cv2.split(HSV2)
Hhist2 = cv2.calcHist([h2], [0], None, [256], [0, 256])


img3 = cv2.imread("../TestImages/Coins1.jpg")
G3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
Ghist3 = cv2.calcHist([G3], [0], None, [256], [0, 256])

HSV3 = cv2.cvtColor(img3, cv2.COLOR_BGR2HSV)
(h3, s3, v3) = cv2.split(HSV3)
Hhist3 = cv2.calcHist([h3], [0], None, [256], [0, 256])


img4 = cv2.imread("../TestImages/Coins2.jpg")
G4 = cv2.cvtColor(img4, cv2.COLOR_BGR2GRAY)
Ghist4 = cv2.calcHist([G4], [0], None, [256], [0, 256])

HSV4 = cv2.cvtColor(img4, cv2.COLOR_BGR2HSV)
(h4, s4, v4) = cv2.split(HSV4)
Hhist4 = cv2.calcHist([h4], [0], None, [256], [0, 256])

method = 0

print "compare greyscales"
Gcmp12 = cv2.compareHist(Ghist1, Ghist2, method)
Gcmp13 = cv2.compareHist(Ghist1, Ghist3, method)
Gcmp34 = cv2.compareHist(Ghist3, Ghist4, method)
print Gcmp12, Gcmp13, Gcmp34 

print "compare hues"
Hcmp12 = cv2.compareHist(Hhist1, Hhist2, method)
Hcmp13 = cv2.compareHist(Hhist1, Hhist3, method)
Hcmp34 = cv2.compareHist(Hhist3, Hhist4, method)
print Hcmp12, Hcmp13, Hcmp34 



''' Splitting
	Channels
	and Comapring '''

(b1, g1, r1) = cv2.split(img1)
MDhist1 = cv2.calcHist([b1,g1,r1], [0], None, [256], [0, 256])

(b2, g2, r2) = cv2.split(img2)
MDhist2 = cv2.calcHist([b2,g2,r2], [0], None, [256], [0, 256])

(b3, g3, r3) = cv2.split(img3)
MDhist3 = cv2.calcHist([b3,g3,r3], [0], None, [256], [0, 256])

(b4, g4, r4) = cv2.split(img4)
MDhist4 = cv2.calcHist([b4,g4,r4], [0], None, [256], [0, 256])

print "Comparing Multidimentional RGB"
MDhist12 = cv2.compareHist(MDhist1, MDhist2, method)
MDhist13 = cv2.compareHist(MDhist1, MDhist3, method)
MDhist34 = cv2.compareHist(MDhist3, MDhist4, method)
print MDhist12, MDhist13, MDhist34










