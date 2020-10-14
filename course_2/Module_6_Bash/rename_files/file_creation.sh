#!/bin/bash

file_count=1

while [ $file_count -le 10 ]; do
    touch examplefile$file_count.txt
    ((file_count+=1))
done
