import glob
import imutils
import cv2

#  loading and coverting the image into numpy array
# images = [cv2.imread(file) for file in glob.glob("/Users/taralgurung/Desktop/blister_main/color_space1/*.jpg")]
# images = [cv2.imread(file) for file in glob.glob("/Users/taralgurung/Desktop/blister_main/edge/*.jpg")]
images = [cv2.imread(file) for file in glob.glob("/Users/taralgurung/Desktop/blister_main/blur/*.jpg")]


# method for image rotation
def rotate(image, angle, center = None, scale = 1.0):
	(h,w) = image.shape[:2]

	if center is None:
		center = (w // 2, h // 2)

	M = cv2.getRotationMatrix2D(center, angle, scale)
	rotated = cv2.warpAffine(image, M, (w,h))
	return rotated

count = 1

for image in images:

	rotated = rotate(image, 180)

	# save to folder with custom name
	name = '/Users/taralgurung/Desktop/blister_main/rotated/rotate_blur'+str(count)+'.jpg'
	resize = imutils.resize(rotated,width = 400)

	path = cv2.imwrite(name, rotated)
	count += 1



