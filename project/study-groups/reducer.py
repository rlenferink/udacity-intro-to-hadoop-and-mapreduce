#!/usr/bin/python

import sys

prev_question_id = None
question_authors = set()

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue

	cur_question_id = int(data_mapped[0])
	cur_question_author_id = int(data_mapped[1])

	if prev_question_id and prev_question_id != cur_question_id:
		print prev_question_id, "\t", sorted(question_authors)
		question_authors = set()

	prev_question_id = cur_question_id
	question_authors.add(cur_question_author_id)

if prev_question_id != None:
	print prev_question_id, "\t", sorted(question_authors)
