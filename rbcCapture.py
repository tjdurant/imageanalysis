#!/usr/bin/env python

###############################################################################
######### Import
###############################################################################

import os
import sys
import time

from time import strftime, gmtime
from os import listdir
from os.path import isfile, join 


###############################################################################
######### Paths
###############################################################################

# set current working directory path
pgmPath = os.getcwd()

# rbc image path
rbcPath = pgmPath + '/Cellavision_Trial_images/rbcs/'

# rbc image path
wbcPath = pgmPath + '/Cellavision_Trial_images/wbcs/'

# set log path
logPath = pgmPath + '/log'
if not os.path.isdir(logPath):
	os.makedirs(logPath)


###############################################################################
######### Create file objects
###############################################################################

#create time stamp YYMMDD_HH:MM:SS  (Greenwhich mean time)
logStamp = strftime('%Y%m%d_%H:%M:%S',gmtime())

#create log file name RSOIS_YYYYMMDD.log
logFile = str('rbcCapture.log.txt')


###############################################################################
######### Test file connections
###############################################################################

newUser = "#####################################################################"

#Create connection to log file
try:
	rbcCapture_log = open(os.path.join(logPath, logFile), 'a')
	rbcCapture_log.write('\n'+newUser+'\n'+logStamp + "-- Successfully opened log file")
except:
	rbcCapture_log.write('\n'+logStamp + 'Invalid pathname, or invalid user permissions\n')
	raise IOError('Invalid pathname, or invalid user permissions')


###############################################################################
######### Create objects
###############################################################################

wbcImgFiles = [f for f in listdir(wbcPath) if isfile(join(wbcPath,f))]



###############################################################################
######### Main
###############################################################################


def main(*args):
	
	try:
		try:
			for f in wbcImgFiles:
				image = wbcPath + f
		except:
			raise
	except:
		raise
		return 2
	return 0


###############################################################################
######### Run
###############################################################################

if __name__ == "__main__":
	sys.exit(main())
