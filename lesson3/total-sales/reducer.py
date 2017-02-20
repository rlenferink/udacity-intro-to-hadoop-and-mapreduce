#!/usr/bin/python

import sys

salesValueTotal = 0
nrOfSalesTotal = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 1:
        continue

    salesValue = data_mapped[0]

    salesValueTotal += float(salesValue)
    nrOfSalesTotal += 1

print nrOfSalesTotal, "\t", salesValueTotal

