#!/usr/bin/python

# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys

users = dict()
posts = dict()

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	data_type = data_mapped[1]
	
	if data_type == "A":
		#user
		user_id, type, reputation, gold, silver, bronze = data_mapped
		users[user_id] = [reputation, gold, silver, bronze]
	elif data_type == "B":
		#post
		author_id, type, id, title, tagnames, node_type, parent_id, abs_parent_id, added_at, score = data_mapped
		posts[id] = [id, title, tagnames, author_id, node_type, parent_id, abs_parent_id, added_at, score]

for post_id in posts:
	id, title, tagnames, author_id, node_type, parent_id, abs_parent_id, added_at, score = posts[post_id]
	reputation, gold, silver, bronze = users[author_id]
	print id, "\t", title, "\t", tagnames, "\t", author_id, "\t", node_type, "\t", parent_id, "\t", abs_parent_id, "\t", added_at, "\t", score, "\t", reputation, "\t", gold, "\t", silver, "\t", bronze
