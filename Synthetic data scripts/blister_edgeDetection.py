import numpy as np
import cv2 
import glob
import imutils

images = [cv2.imread(file) for file in glob.glob("/Users/taralgurung/Desktop/blister_main/blur/*.jpg")]


#  loading and coverting the image into numpy array
# image = cv2.imread("/home/taral/Desktop/OpenCV-tutorial-1/blister_resize/blister1.jpg")

# convert image to grayscale
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

count = 1
for image in images:

	# implement gaussian blurr
	blurred = cv2.GaussianBlur(image, (5,5), 0)
	canny = cv2.Canny(blurred, 30, 100)
	resize = imutils.resize(canny,width = 400)
	name = '/Users/taralgurung/Desktop/blister_main/edge/edge'+str(count)+'.jpg'
	path = cv2.imwrite(name, resize)
	count += 1