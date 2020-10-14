#!/bin/bash

n=1
while [ $n -le 5 ]; do
    echo "Iterate number is $n"
    ((n+=1))
done