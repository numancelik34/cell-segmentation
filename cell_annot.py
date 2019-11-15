
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 10:12:54 2019

@author: ncelik34
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


#watershed algorithm
img = cv.imread('con230_crp.jpg',0)
img_copy = img.copy()
#img = cv.bilateralFilter(img, 9, 170, 170)
#gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#ret, thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)


blur = cv.GaussianBlur(img,(5,5),0)
ret3,th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
plt.imshow(th3)
th3=cv.subtract(255, th3) 
plt.imshow(th3)

kernel = np.ones((9,9),np.uint8)


image, contours, hier = cv.findContours(th3, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cnts = sorted(contours, key = cv.contourArea, reverse = True)[:2] # get largest five contour area
contour_sizes = [(cv.contourArea(contour), contour) for contour in contours]
area_min=1000
area_max=4000
x, y = th3.shape
arr = np.zeros((x, y, 3), np.uint8)
final_contours = []


for i in range(len(cnts)):
    cntss=cnts[i]
    #cv.drawContours(image_channels, cntss, -1, [0, 255, 255],-1)
    cv.fillConvexPoly(arr, cntss, [255, 255, 255])

plt.imshow(arr)
cv.imwrite('annot1.jpg', arr) 

