#!/usr/bin/env python3

import sys
import os

file_name = sys.argv[1]
if not os.path.exists(file_name):
    with open(file_name, "w+") as new_file:
        new_file.write("This file is writtern successfully.")
else:
    print("File already exist. Cannot proceed")
    sys.exit(22)

#echo $? shows the error code after execution of the script/program