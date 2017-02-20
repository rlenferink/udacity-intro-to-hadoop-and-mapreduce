#!/usr/bin/python

import sys

oldPath = None
pageHits = 0

for line in sys.stdin:
	data_mapped = line.strip().split(" ")
	if len(data_mapped) != 1:
		continue

	newPath = data_mapped[0]

	if oldPath and oldPath != newPath:
		print oldPath, "\t", pageHits
		pageHits = 0

	oldPath = newPath
	pageHits += 1

if oldPath != None:
	print oldPath, "\t", pageHits

