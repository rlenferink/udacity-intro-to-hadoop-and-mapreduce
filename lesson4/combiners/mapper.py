#!/usr/bin/python

import sys
from datetime import datetime

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 6:
		continue

	date, time, store, item, cost, payment = data
	weekday = datetime.strptime(date, "%Y-%m-%d").weekday() #weekday where monday = 0 and sunday = 6

	print weekday, "\t", cost
