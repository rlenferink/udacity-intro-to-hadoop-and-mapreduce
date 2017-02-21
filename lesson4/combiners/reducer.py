#!/usr/bin/python

import sys

oldWeekday = None
daySalesSum = 0

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue

	curWeekday, cost = data_mapped

	if oldWeekday and oldWeekday != curWeekday:
		print oldWeekday, "\t", daySalesSum
		daySalesSum = 0

	oldWeekday = curWeekday
	daySalesSum += float(cost)

if oldWeekday != None:
	print oldWeekday, "\t", daySalesSum 
