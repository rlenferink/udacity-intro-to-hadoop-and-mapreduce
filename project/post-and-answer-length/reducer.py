#!/usr/bin/python

import sys

prev_question_id = None

number_of_answers = 0
total_answers_length = 0
question_length = 0

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 3:
		continue

	cur_question_id, node_type, body_length = data_mapped
	node_type = node_type.strip()

	if prev_question_id and prev_question_id != cur_question_id:
		if number_of_answers > 0:
			avg_answer_length = float(total_answers_length) / number_of_answers
		else:
			avg_answer_length = 0

		print prev_question_id, "\t", question_length, "\t", avg_answer_length
		number_of_answers = 0
		total_answers_length = 0
		question_length = 0

	if node_type == "question":
		question_length += int(body_length)
	elif node_type == "answer":
		total_answers_length += float(body_length)
		number_of_answers += 1

	prev_question_id = cur_question_id

if prev_question_id != None:
	if number_of_answers > 0:		
		avg_answer_length = float(total_answers_length) / number_of_answers
	else:
		avg_answer_length = 0
	
	print prev_question_id, "\t", question_length, "\t", avg_answer_length
