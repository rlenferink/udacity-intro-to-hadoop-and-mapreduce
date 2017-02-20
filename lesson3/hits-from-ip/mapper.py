#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) != 10:
        continue
   
    ip = data[0] 
    
    print ip
