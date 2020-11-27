#!/usr/bin/env python3

import random

def greeting():
  name = input("Hello!, What's your name?")
  number = random.randint(1,101)
  print("hello " + name + ", your random number is " + str(number)) #Fixing the type conflict while trying to concatenate a string and an integer.

greeting()