#!/usr/bin/python

import sys
import re

parts = [
    r'(?P<host>\S+)',                   # host %h
    r'\S+',                             # indent %l (unused)
    r'(?P<user>\S+)',                   # user %u
    r'\[(?P<time>.+)\]',                # time %t
    r'"(?P<request>.+)"',               # request "%r"
    r'(?P<status>[0-9]+)',              # status %>s
    r'(?P<size>\S+)',                   # size %b (careful, can be '-')
]
pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')

for line in sys.stdin:
    m = pattern.match(line)
    
    if m is None:
        continue

    res = m.groupdict()
    if len(res) != 6:
        continue
    
    request_data = res["request"].strip().split(" ")
    
    if len(request_data) != 3:
        continue

    method, fileName, httpVersion = request_data
    
    print fileName
