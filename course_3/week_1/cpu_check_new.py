#!/usr/bin/env python3

import psutil
import sys

def cpu_overload_check(latency, percentage):
    usage = psutil.cpu_percent(float(latency))
    return usage > float(percentage)

if cpu_overload_check(sys.argv[1], sys.argv[2]):
    print("Overloaded")
else:
    print("Everything OK!")