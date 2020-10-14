#!/usr/bin/env python3
import shutil # shutil is a module to taking care of disk related informations.
import psutil # psutil is a module to taking care of CPU related informations.

# This function reads the total disk usage and return the percentage of used disk space
def check_disk_usage_percentile():
    disk_usage = shutil.disk_usage("/")
    return (disk_usage.used/disk_usage.total) * 100

# This function reads the CPU usage percentile in a certain time period ( here 2 seconds ) and return the cpu_usage
def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(2)
    return cpu_usage

# Prints the disk usage and CPU usage in good format.
print("Disk usage : {:.4f} \n CPU usage : {}".format(check_disk_usage_percentile(),check_cpu_usage()))

# Check if the disk & CPU usage above a certain threshold, So that based on it, it returns corresponding outputs.
if check_disk_usage_percentile() > 50 and check_cpu_usage() > 50:
    print("ERROR!")
else:
    print("Everything seems fine! Chill relax and have a cup of coffee.") 