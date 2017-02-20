#!/usr/bin/python

import sys

mostPopularPage = None
mostPopularPageHits = -1

prevFileName = None

totalPageHits = 0

for line in sys.stdin:
	data_mapped = line.strip().split(" ")
	if len(data_mapped) != 1:
		continue

	fileName = data_mapped[0]

	if fileName != prevFileName:
		if totalPageHits > mostPopularPageHits:
			mostPopularPageHits = totalPageHits
			mostPopularPage = prevFileName 
		totalPageHits = 0

	prevFileName = fileName
	totalPageHits += 1

print mostPopularPage, " ", mostPopularPageHits

