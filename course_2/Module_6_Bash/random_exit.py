#!/usr/bin/env python3

import sys
import random

number = random.randint(0, 4)
print("Number returned : {}".format(str(number)))
sys.exit(number)