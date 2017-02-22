#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
	if line[0] == "id" or len(line) != 19: 
		continue

	node_id = line[0]
	node_body = line[4]
	node_type = line[5]
	node_parent_id = line[6]

	question_id = None
	if node_type == "question":
		question_id = node_id
	elif node_type == "answer":
		question_id = node_parent_id

	if question_id == None:
		continue

	print question_id, "\t", node_type, "\t", len(node_body)
