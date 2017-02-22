#!/usr/bin/python

import sys
import csv
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
	author_id = line[3]
	added_at = line[8]

	if author_id == "author_id" or added_at == "added_at":
		continue

	added_at_hour = datetime.strptime(added_at[:-3], "%Y-%m-%d %H:%M:%S.%f").strftime("%H")

	print author_id, "\t", added_at_hour
