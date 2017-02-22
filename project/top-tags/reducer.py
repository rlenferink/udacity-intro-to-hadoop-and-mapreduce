#!/usr/bin/python

import sys

n = 10
top_n = dict()

least_used_tag = None
least_used_count = 0

prev_tag = None
tag_count = 0

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue	

	cur_tag = data_mapped[0].strip()
	cur_tag_count = int(data_mapped[1])

	if prev_tag and prev_tag != cur_tag:
		tag_count = 0

	prev_tag = cur_tag
	tag_count += cur_tag_count

	if top_n.has_key(cur_tag):
		top_n[cur_tag] += cur_tag_count
	else:
		if len(top_n.keys()) >= n:
			if tag_count > least_used_count:
				del top_n[least_used_tag]
				top_n[cur_tag] = tag_count
		else:
			top_n[cur_tag] = cur_tag_count

	if bool(top_n) == True:
		least_used_tag = min(top_n, key=top_n.get)
		least_used_count = top_n[least_used_tag]

top_n = sorted(top_n.items(), key=lambda x: x[1], reverse=True)
for key, value in top_n:
	print key, "\t", value
