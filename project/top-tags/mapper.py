#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
	if line[0] == "id":
		continue

	node_type = line[5].strip()

	if node_type != "question":
		continue

	tagnames = line[2].split(" ")
	
	for tagname in tagnames:
		print tagname.lower(), "\t", 1
