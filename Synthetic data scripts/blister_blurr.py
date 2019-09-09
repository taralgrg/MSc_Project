import glob
import cv2 

#  loading and coverting the image into numpy array
images = [cv2.imread(file) for file in glob.glob("/Users/taralgurung/Desktop/blister_main/color_space1/*.jpg")]
count = 1

for image in images:

	# bilateral blurring (showed better results than other blurring types)
	blurred = cv2.bilateralFilter(image, 3, 21, 21)
	blurred1 = cv2.blur(image, (3,3))
	blurred2 = cv2.GaussianBlur(image, (3,3), 0)
	blurred3 = cv2.medianBlur(image, 3)

	# save to folder with custom name
	name = '/Users/taralgurung/Desktop/blister_main/blur/bilateral'+str(count)+'.jpg'
	name1 = '/Users/taralgurung/Desktop/blister_main/blur/average'+str(count)+'.jpg'
	name2 = '/Users/taralgurung/Desktop/blister_main/blur/gaussian'+str(count)+'.jpg'
	name3 = '/Users/taralgurung/Desktop/blister_main/blur/median'+str(count)+'.jpg'

	path = cv2.imwrite(name, blurred)
	path = cv2.imwrite(name1, blurred1)
	path = cv2.imwrite(name2, blurred2)
	path = cv2.imwrite(name3, blurred3)

	count += 1


