#!/usr/bin/python

import sys

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

oldWeekday = None
daySalesValue = 0
daySales = 0

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue

	curWeekday, cost = data_mapped

	if oldWeekday and oldWeekday != curWeekday:
		avg = float(daySalesValue) / float(daySales)
		print weekdays[int(oldWeekday)], "\t", avg
		daySalesValue = 0
		daySales = 0

	oldWeekday = curWeekday
	daySalesValue += float(cost)
	daySales += 1

if oldWeekday != None:
	avg = float(daySalesValue) / float(daySales)
	print weekdays[int(oldWeekday)], "\t", avg
