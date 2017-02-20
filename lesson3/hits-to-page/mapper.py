#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) != 10:
        continue
   
    fileName = data[6] 
    
    print fileName
