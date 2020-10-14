#!/usr/bin/env python3

import sys
import subprocess

file = sys.argv[1]

with open(file, "r") as file_content:
  line = file_content.readlines()
  for location_path in line:
    location_path.strip()
    #print(location_path)
    new_line = location_path.replace("jane", "jdoe")
    #print(new_line)
    subprocess.run(['mv', location_path.strip(), new_line.strip()])