#!/usr/bin/python

import sys
import re
import csv
import numbers

# split on ' .,!?:;"()<>[]#$=-/'

reader = csv.reader(sys.stdin, delimiter='\t')

delimiters = [' ', '.', ',', '!', '?', ':', ';', '"', '(', ')', '<', '>', '[', ']', '#', '$', '=', '-', '/']
regex = '|'.join(map(re.escape, delimiters))

for line in reader:
	nodeId = line[0]
	if not nodeId.isdigit():
		continue

	body = re.split(regex, line[4])
	for word in body:
		print nodeId, "\t", word
