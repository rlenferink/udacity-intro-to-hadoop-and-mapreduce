#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:

	if line[0] == "id" or line[0] == "user_ptr_id": # first line of file
		continue
	
	if len(line) == 5:
		user_ptr_id, reputation, gold, silver, bronze = line
		print user_ptr_id, "\tA\t", reputation, "\t", gold, "\t", silver, "\t", bronze
	elif len(line) == 19:
		id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = line
		print author_id, "\tB\t", id, "\t", title, "\t", tagnames, "\t", node_type, "\t", parent_id, "\t", abs_parent_id, "\t", added_at, "\t", score