import cv2

imageNames = "Blowhole013.jpg Pioneer0067.jpg frankenstein.jpg Blowhole021.jpg Pioneer0093.jpg garden.jpg Coins1.jpg Puzzle1.jpg ghostrider.jpg Coins2.jpg Puzzle2.jpg gorge.jpg DollarCoin.jpg SnowLeo1.jpg redDoor.jpg SnowLeo2.jpg sampleRed.jpg Pioneer0005.jpg SnowLeo3.jpg shops.jpg Pioneer0012.jpg SnowLeo4.jpg swans.jpg Pioneer0029.jpg frame0017.jpg waterfall.jpg Pioneer0063.jpg frame0019.jpg"
imageNames = imageNames.split(' ')

for i in images:
	print(i)
	cimg = cv2.imread("../TestImages/"+i)
	cv2.imshow("Image", cimg)
	cv2.waitKey(0)

cv2.destroyAllWindows()