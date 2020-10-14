#!/usr/bin/env python3

import re
import sys
import operator

filename = sys.argv[1]
per_user = {}
error = {}
pattern1 = r"([RO])[\s]([\w\s\']*)[\s]"
pattern2 = r"\(([\w\.]*)\)$"

with open(filename, "r") as log:
  for line in log:
    log_error = re.search(pattern1, line)
    user_det = re.search(pattern2, line)
    if log_error.group(1) == 'R':
      error[log_error.group(2)] = error.get(log_error.group(2), 0) + 1
    per_user[user_det.group(1)] = [0, 0]
  log.close()

with open(filename, "r") as log:    
  for user_line in log:
    log_error = re.search(pattern1, user_line)
    user_det = re.search(pattern2, user_line)
    if log_error.group(1) == 'O':
      per_user[user_det.group(1)][0] +=1
    if log_error[1] == 'R':
      per_user[user_det.group(1)][1] +=1
  log.close()

sorted_errors = sorted(error.items(), key = operator.itemgetter(1), reverse=True)
sorted_users = sorted(per_user.items())

sorted_errors.insert(0, ("Error", "Count"))
sorted_users.insert(0, ("Username", ("INFO", "ERROR")))

with open("error_message.csv", "w") as error_write:
  for data in sorted_errors: 
    error_write.write("{}, {}\n".format(data[0], data[1]))
  error_write.close()

with open("user_statistics.csv", "w") as user_write:
  for data in sorted_users: 
    user_write.write("{}, {}, {}\n".format(data[0], data[1][0], data[1][1]))
  error_write.close()