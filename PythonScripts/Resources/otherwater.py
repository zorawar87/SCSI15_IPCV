import sys
import cv2
import numpy
from scipy.ndimage import label

def showAndWait(title, image):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    
    
def segment_on_dt(a, img):
    border = cv2.dilate(img, None, iterations=5)
    border = border - cv2.erode(border, None)

    dt = cv2.distanceTransform(img, 2, 3)
    dt = ((dt - dt.min()) / (dt.max() - dt.min()) * 255).astype(numpy.uint8)
    _, dt = cv2.threshold(dt, 180, 255, cv2.THRESH_BINARY)
    showAndWait("Distance", dt)
    lbl, ncc = label(dt)
    lbl = lbl * (255/ncc)
    # Completing the markers now. 
    lbl[border == 255] = 255
    cv2.imshow("labels", lbl)
    lbl = lbl.astype(numpy.int32)
    
    cv2.watershed(a, lbl)

    lbl[lbl == -1] = 0
    lbl = lbl.astype(numpy.uint8)
    return 255 - lbl


img = cv2.imread("TestImages/Coins1.jpg")

# Pre-processing.
(b, g, r) = cv2.split(img)
diff = cv2.subtract(g, r)
img_gray = diff
_, img_bin = cv2.threshold(img_gray, 0, 255,
        cv2.THRESH_OTSU)
showAndWait("diff", diff)
img_bin = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN,
        numpy.ones((3, 3), dtype=int))
showAndWait("img_bin", img_bin)

result = segment_on_dt(img, img_bin)


result[result != 255] = 0
result = cv2.dilate(result, None)
img[result == 255] = (0, 0, 255)
showAndWait("Final", img)

cv2.destroyAllWindows()

