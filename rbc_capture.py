#!/usr/bin/env python

##############################################################################
#Copyright (c) 2015 Thomas Durant
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#the above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
################################################################################

__author__    = 'Thomas Durant'
__date__      = '10/14/2015'
__pyver__     = '2.7'

###############################################################################
######### Import
###############################################################################

import os
import sys
import time
import PIL

import numpy as np

from time import strftime, gmtime
from os import listdir
from os.path import isfile, join 
from PIL import Image

# http://stackoverflow.com/questions/15514593/importerror-no-module-named-when-trying-to-run-python-script
# openCV sometimes doesn't import so you have to append it's directory to your local path, even if /
# it is installed to your python environment. 

import sys
sys.path.append('C:/Anaconda/Lib/site-packages')
import cv2


###############################################################################
######### Classes/Functions
###############################################################################
	
def rbc_capture():
	image = rbcPath + test

	im = cv2.imread(image)

	test = im.copy()
	test = cv2.cvtColor(test,cv2.COLOR_BGR2GRAY)
	test = cv2.medianBlur(test, 5)
	ret,thresh = cv2.threshold(test,205,255,0)
	image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

	idx = 0 
	rectParameters = []
	for h, cnt in enumerate(contours):
	    
	    area = cv2.contourArea(cnt)
	    if area < 300:
	        continue
	    if area > 2000:
	        continue
	    if len(cnt) < 5:
	        continue
	    
	    # pandas; original, mask, and coordinates
	    x,y,w,h = cv2.boundingRect(cnt) 
	    
	    idx += 1
	    # crop and save each object
	    crop_img = im[y: y + h, x: x + w]
	    cv2.imwrite('%s.png'%idx, crop_img)
	    
	    # build full list of rect params
	    param = cv2.boundingRect(cnt) 
	    rectParameters.append(param)
	    
	    # draw rectangles on image
	    cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)



	# cv2.imshow("cropped", crop_img)
	# cv2.waitKey(0)
	    
	cv2.imshow('img',im)
	cv2.waitKey(0) 