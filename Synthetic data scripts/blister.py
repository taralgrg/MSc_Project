#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 01:12:51 2019

@author: taralgurung
"""

import cv2
import imutils



image = cv2.imread("/Users/taralgurung/Desktop/blister_main/blister.jpg")





converted = cv2.cvtColor(image, cv2.COLOR_BGR2BGR555)
name = '/Users/taralgurung/Desktop/blister_main/color_space1/color_space_1.jpg'
path = cv2.imwrite(name, converted)

converted = cv2.cvtColor(image, cv2.COLOR_BGR2BGR565)
name = '/Users/taralgurung/Desktop/blister_main/color_space1/color_space_2.jpg'
path = cv2.imwrite(name, converted)

# converted = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
# name = '/home/taral/Desktop/blister_main/color_space1/color_space_3.jpg'
# path = cv2.imwrite(name, converted)
#
# converted = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# name = '/home/taral/Desktop/blister_main/color_space1/color_space_4.jpg'
# path = cv2.imwrite(name, converted)
#
# converted = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
# name = '/home/taral/Desktop/blister_main/color_space1/color_space_5.jpg'
# path = cv2.imwrite(name, converted)
#
# converted = cv2.cvtColor(image, cv2.COLOR_BGR2HLS_FULL)
# name = '/home/taral/Desktop/blister_main/color_space1/color_space_6.jpg'
# path = cv2.imwrite(name, converted)
#
# converted = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# name = '/home/taral/Desktop/blister_main/color_space1/color_space_7.jpg'
# path = cv2.imwrite(name, converted)
#
# converted = cv2.cvtColor(image, cv2.COLOR_BGR2HSV_FULL)
# name = '/home/taral/Desktop/blister_main/color_space1/color_space_8.jpg'
# path = cv2.imwrite(name, converted)
#
# converted = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
# name = '/home/taral/Desktop/blister_main/color_space1/color_space_9.jpg'
# path = cv2.imwrite(name, converted)
#
# converted = cv2.cvtColor(image, cv2.COLOR_BGR2LUV)
# name = '/home/taral/Desktop/blister_main/color_space1/color_space_10.jpg'
# path = cv2.imwrite(name, converted)
#
# converted = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
# name = '/home/taral/Desktop/blister_main/color_space1/color_space_11.jpg'
# path = cv2.imwrite(name, converted)
#
# converted = cv2.cvtColor(image, cv2.COLOR_BGR2Luv)
# name = '/home/taral/Desktop/blister_main/color_space1/color_space_12.jpg'
# path = cv2.imwrite(name, converted)
#
# converted = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# name = '/home/taral/Desktop/blister_main/color_space1/color_space_13.jpg'
# path = cv2.imwrite(name, converted)
#
# converted = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
# name = '/home/taral/Desktop/blister_main/color_space1/color_space_14.jpg'
# path = cv2.imwrite(name, converted)
#
# converted = cv2.cvtColor(image, cv2.COLOR_BGR2XYZ)
# name = '/home/taral/Desktop/blister_main/color_space1/color_space_15.jpg'
# path = cv2.imwrite(name, converted)
#
# converted = cv2.cvtColor(image, cv2.COLOR_BGR2YCR_CB)
# name = '/home/taral/Desktop/blister_main/color_space1/color_space_16.jpg'
# path = cv2.imwrite(name, converted)
#
# converted = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
# name = '/home/taral/Desktop/blister_main/color_space1/color_space_17.jpg'
# path = cv2.imwrite(name, converted)
#
# converted = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
# name = '/home/taral/Desktop/blister_main/color_space1/color_space_18.jpg'
# path = cv2.imwrite(name, converted)
#
# converted = cv2.cvtColor(image, cv2.COLOR_BGR2YUV_I420)
# name = '/home/taral/Desktop/blister_main/color_space1/color_space_19.jpg'
# path = cv2.imwrite(name, converted)
#
# converted = cv2.cvtColor(image, cv2.COLOR_BGR2YUV_IYUV)
# name = '/home/taral/Desktop/blister_main/color_space1/color_space_20.jpg'
# path = cv2.imwrite(name, converted)
#
# converted = cv2.cvtColor(image, cv2.COLOR_BGR2YUV_YV12)
# name = '/home/taral/Desktop/blister_main/color_space1/color_space_21.jpg'
# path = cv2.imwrite(name, converted)
#
