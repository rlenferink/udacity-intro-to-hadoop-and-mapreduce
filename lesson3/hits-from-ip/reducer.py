#!/usr/bin/python

import sys

oldIp = None
totalIpVisits = 0

for line in sys.stdin:
	data_mapped = line.strip().split(" ")
	if len(data_mapped) != 1:
		continue

	newIp = data_mapped[0]

	if oldIp and oldIp != newIp:
		print oldIp, "\t", totalIpVisits
		totalIpVisits = 0

	oldIp = newIp
	totalIpVisits += 1

if oldIp != None:
	print oldIp, "\t", totalIpVisits
