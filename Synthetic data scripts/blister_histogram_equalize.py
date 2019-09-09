import numpy as np
import cv2 
import glob


images = [cv2.imread(file) for file in glob.glob("/Users/taralgurung/Desktop/blister_main/blur_colorspace_edge/*.jpg")]

#  loading and coverting the image into numpy array
# image = cv2.imread("/home/taral/Desktop/OpenCV-tutorial-1/blister_resize/blister1.jpg")

# convert image to grayscale
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

count = 1
for image in images:

	# apply grayscale for histogram
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# apply Histogram Equalization
	equalizer = cv2.equalizeHist(gray)

	name = '/Users/taralgurung/Desktop/blister_main/histogram/histogram'+str(count)+'.jpg'
	path = cv2.imwrite(name, equalizer)
	count += 1



# cv2.imshow("BGR image", image)
# cv2.waitKey(0)

# BGR to Grayscale
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# eq = cv2.equalizeHist(gray)
# cv2.imshow("Normal and equalized",eq)
# cv2.waitKey(0)