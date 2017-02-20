#!/usr/bin/python

import sys
import re

strToReplace = "http://www.the-associates.co.uk"
strToReplace_len = len(strToReplace)

for line in sys.stdin:
	data = line.strip().split(" ")
	if len(data) != 10:
		continue
   
	fileName = data[6] 

	if len(fileName) > strToReplace_len:
		startingOfFileName = fileName[:strToReplace_len]
		if startingOfFileName == strToReplace:
			fileName = fileName[strToReplace_len:]
 
	print fileName
