#!/usr/bin/env python3
import csv
file = open("csv_example.csv")
read_file = csv.reader(file)
for row in read_file:
    print("Name: {} Phone No: {} Role : {}".format(row[0], row[1], row[2]))
file.close()