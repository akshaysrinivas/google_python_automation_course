#!/usr/bin/env python3

import re
import os
import subprocess

def excecute_permission(filename):
    process_return = subprocess.run(["chmod", "+x", filename])    
    if process_return.returncode == 0:
        return "\nExecute permission for file \"{}\" applied successfully.".format(filename)
    else:
        return "\nExecute permission for file {} failed.".format(filename)

directory_list = os.listdir()
pattern = r".*\.py$"
for file in directory_list:
    if not os.path.isdir(file):
        if re.match(pattern, file) is not None:
            print(excecute_permission(file))