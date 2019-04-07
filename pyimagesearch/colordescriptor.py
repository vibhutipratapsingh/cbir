# import the necessary packages
import numpy as np
import cv2 as cv
# cv version 3.4.1
# imutils to check OpenCV version
# import imutils

class ColorDescriptor:
	def __init__(self, bins):
		# store the number of bins for the 3D histogram
		pass

	def describe(self, image):
		# print(cv.__version__)
		# print(image)
		# convert the image to the HSV color space and initialize
		# the features used to quantify the image
		# img = cv.imread(image)
		gray= cv.cvtColor(image,cv.COLOR_BGR2GRAY)
		sift = cv.xfeatures2d.SIFT_create()
		kp, des = sift.detectAndCompute(gray,None)
		# print (kp)
		# image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
		

		# return the feature vector
		return kp

	# def histogram(self, image, mask):
	# 	# extract a 3D color histogram from the masked region of the
	# 	# image, using the supplied number of bins per channel
	# 	hist = cv2.calcHist([image], [0, 1, 2], mask, self.bins,
	# 		[0, 180, 0, 256, 0, 256])

	# 	# normalize the histogram if we are using OpenCV 2.4
	# 	# if imutils.is_cv2():
	# 	# 	hist = cv2.normalize(hist).flatten()

	# 	# otherwise handle for OpenCV 3+
	# 	# else:
	# 	hist = cv2.normalize(hist, hist).flatten()

	# 	# return the histogram
	# 	return hist