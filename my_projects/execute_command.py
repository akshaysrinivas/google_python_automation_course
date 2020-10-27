#!/usr/bin/env python3

import subprocess

def execute_command(command):
    command_split = command.split()
    result = subprocess.run(command_split, capture_output=True)
    return result

command_user = input("Command to execute : ")
result = execute_command(command_user)
print("Error code : {}\ngActual o/p from bash : {}".format(result.returncode, result.stdout.decode().split() if result.returncode == 0 else result.stderr.decode()))