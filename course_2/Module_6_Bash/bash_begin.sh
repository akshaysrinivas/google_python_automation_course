#!/bin/bash

line="--------------------------------------------------------------------------" #There should be no spaces betweem equal sign

echo "Starting at :" $(date) #Sepcifies date result should be printed in echo command
echo; echo $line

echo "UPTIME"
uptime
echo; echo $line

echo "USERS"
who
echo; echo $line

echo "FREE"
free
echo; echo $line

echo "Finished at :" $(date)