import numpy as np
import cv2 
import glob

images = [cv2.imread(file) for file in glob.glob("/Users/taralgurung/Desktop/blister_main/blur_colorspace_edge/*.jpg")]


#  loading and coverting the image into numpy array
# image = cv2.imread("/home/taral/Desktop/OpenCV-tutorial-1/blister_resize/blister6.jpg")

# convert image to grayscale
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

count = 1
for image in images:

	rows,cols,ch = image.shape

	pts1 = np.float32([[50,50],[200,50],[50,200]])
	pts2 = np.float32([[10,100],[200,50],[100,250]])

	M = cv2.getAffineTransform(pts1,pts2)

	dst = cv2.warpAffine(image,M,(cols,rows))


	name = '/Users/taralgurung/Desktop/blister_main/skew/skew'+str(count)+'.jpg'

	path = cv2.imwrite(name, dst)
	count += 1


