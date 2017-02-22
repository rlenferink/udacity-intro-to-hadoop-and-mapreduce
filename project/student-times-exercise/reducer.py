#!/usr/bin/python

import sys

author_active_hours = [0] * 24
prev_author_id = None

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue

	cur_author_id, active_hour = data_mapped

	if prev_author_id and prev_author_id != cur_author_id:
		most_active_hour_posts = max(author_active_hours)
		for hour, posts in enumerate(author_active_hours):
			if posts == most_active_hour_posts:
				print prev_author_id, "\t", hour
		author_active_hours = [0] * 24

	prev_author_id = cur_author_id
	author_active_hours[int(active_hour)] += 1

if prev_author_id != None:
	most_active_hour_posts = max(author_active_hours)
	for hour, posts in enumerate(author_active_hours):
		if posts == most_active_hour_posts:
			print prev_author_id, "\t", hour
