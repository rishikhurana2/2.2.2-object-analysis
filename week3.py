import cv2
import numpy as np
class week3lab:
	minX = 10000
	minY = 10000
	maxX = 0
	maxY = 0
	img = cv2.imread("rect.jpg")
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	THRESHOLD_MIN = np.array([0,0,200], np.uint8)
	THRESHOLD_MAX = np.array([255, 0, 255], np.uint8)
	threshedframe = cv2.inRange(hsv, THRESHOLD_MIN, THRESHOLD_MAX)
	count = -1;
	image, contours, hierarchy = cv2.findContours(threshedframe, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(img, contours, -1, (255,0,0), 5)
	cv2.imshow("Contours", img)
	for cont in contours:
		approx = cv2.approxPolyDP(cont, 0.1*cv2.arcLength(cont, True), True)
		for i in approx:
			if i[0][0] > maxX:
				maxX = i[0][0]
			if i[0][0] < minX:
				minX = i[0][0]
			if i[0][1] > maxY:
				maxY = i[0][1]
			if i[0][1] < minY:
				minY = i[0][1]
		width = maxX-minX
		height = maxY-minY
		focalLength = 700
		realWidth = 50
		realHeight = 25
		imgCenterX = width/2
		imgCenterY = height/2
	distance = (focalLength * realWidth)/width
	azimuth = np.arctan(imgCenterX/focalLength)
	altitude = np.arctan(imgCenterY/focalLength)
	print(distance)
	print(azimuth)
	print(altitude)
	print("The first one is distance")
	print("The second one is azimuth")
	print("The third one is altitude")
	print("(For some reason I couldn't cacatinate a string with the distance, azimuth, and altitude)")
	cv2.waitKey(0)