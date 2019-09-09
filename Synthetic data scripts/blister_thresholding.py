import numpy as np
import cv2 
import glob


images = [cv2.imread(file) for file in glob.glob("/Users/taralgurung/Desktop/blister_main/blur_colorspace_edge/*.jpg")]
# images = [cv2.imread(file) for file in glob.glob("/Users/taralgurung/Desktop/blister_main/color_space1/*.jpg")]
# images = [cv2.imread(file) for file in glob.glob("/Users/taralgurung/Desktop/blister_main/edge/*.jpg")]
# images = [cv2.imread(file) for file in glob.glob("/Users/taralgurung/Desktop/blister_main/blur/*.jpg")]


count = 1

for image in images:

	# applying blurr to pass to threshold
	blurred = cv2.GaussianBlur(image, (5,5), 0)

	# simple thresholding using binary
	(T, thresh1) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)

	# simple thresholding using inv binary
	(T, threshInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)

	# adaptive thresholding using mean
	# thresh2 = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)

	# adaptive thresolding using gaussian     ------doesnt work
	# thresh3 = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
	# 							   cv2.THRESH_BINARY_INV, 11, 4)

	# save to folder with custom name
	name1 = '/Users/taralgurung/Desktop/blister_main/thresh/thresh1'+str(count)+'.jpg'
	# name2 = '/Users/taralgurung/Desktop/blister_main/thresh/thresh2'+str(count)+'.jpg'
	# name3 = '/Users/taralgurung/Desktop/blister_main/threshold/thresh3'+str(count)+'.jpg'
	name4 = '/Users/taralgurung/Desktop/blister_main/thresh/thresh4'+str(count)+'.jpg'

	path1 = cv2.imwrite(name1, thresh1)
	# path2 = cv2.imwrite(name2, thresh2)
	# path3 = cv2.imwrite(name3, thresh3)
	path4 = cv2.imwrite(name4, threshInv)

	count += 1




