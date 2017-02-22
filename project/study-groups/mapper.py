#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
	if line[0] == "id":
		continue

	node_id = line[0]
	node_author_id = line[3]
	node_type = line[5].strip()
	node_parent_id = line[6]

	if node_type == "question":
		question_id = node_id
	else:
		question_id = node_parent_id

	print question_id, "\t", node_author_id
