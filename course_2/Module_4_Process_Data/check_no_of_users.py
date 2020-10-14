#!/usr/bin/env python3

import sys
import re
import csv

filename = sys.argv[1]
pattern = r"\(([\w]*)\)$"
username = {}

with open(filename) as f:
    for line in f:
        if "CRON" not in line:
            continue
        pattern_match = re.search(pattern, line)
        #print(pattern_match[1])
        name = pattern_match[1]
        username[name] = username.get(name, 0) + 1
print(username)

keys = username.keys()
with open(filename, "a") as f:
    file_write = csv.DictWriter(f, fieldnames=keys)
    file_write.writeheader()
    file_write.writerows([username])
