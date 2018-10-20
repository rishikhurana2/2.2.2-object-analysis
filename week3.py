import cv2
import numpy as np
class week3lab:
	minX = 10000
	minY = 10000
	maxX = 0
	maxY = 0
	img = cv2.imread("rect.jpg")
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	THRESHOLD_MIN = np.array([0,0,236], np.uint8)
	THRESHOLD_MAX = np.array([255, 100, 255], np.uint8)
	threshedframe = cv2.inRange(hsv, THRESHOLD_MIN, THRESHOLD_MAX)
	count = -1
	image, contours, hierarchy = cv2.findContours(threshedframe, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	for cont in contours:
		count = count + 1
		approx = cv2.approxPolyDP(cont, 0.1*cv2.arcLength(cont, True), True)
		if (cv2.contourArea(approx) > 100):
			cv2.drawContours(img, contours, count, (255,0,0), 5)
			for i in approx:
				if (i[0][0] > maxX):
					maxX = i[0][0]
				if (i[0][0] < minX):
					minX = i[0][0]
				if (i[0][1] > maxY):
					maxY = i[0][1]
				if (i[0][1] < minY):
					minY = i[0][1]
			width = maxX-minX
			height = maxY-minY
			focalLength = 700
			realWidth = 50
			realHeight = 25
			imgCenterX = (maxX + minX)/2
			imgCenterY = (maxY + minY)/2
			centerX = width/2
			centerY = height/2
			xOffset = hsv.shape[0]-imgCenterX
			yOffset = hsv.shape[1]-imgCenterY
			distance = (focalLength * realWidth)/width
			azimuth = np.arctan(xOffset/focalLength)*180/np.pi
			altitude = np.arctan(yOffset/focalLength)*180/np.pi
			print(distance)
			print(azimuth)
			print(altitude)
			print("The first one is distance")
			print("The second one is azimuth")
			print("The third one is altitude")
			print("(For some reason I couldn't cacatinate a string with the distance, azimuth, and altitude)")
	cv2.imshow("Contour Image", img)
	cv2.waitKey(0)