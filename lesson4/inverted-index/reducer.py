#!/usr/bin/python

import sys
import re
import collections

index = collections.defaultdict(list) 

for line in sys.stdin:
	data_mapped = line.strip().split(" ")
	if len(data_mapped) != 2:
		continue

	nodeId = int(data_mapped[0])
	word = data_mapped[1].lower().strip() #assignment is to create a lower case index

	index[word].append(nodeId) # create a list with the word as key, and the array of nodeIds as value

for word in index:
	# print index
	# {word}	{number of occurrences}	{array of nodeIds}
	print word, "\t", len(index[word]), "\t", sorted(index[word])
