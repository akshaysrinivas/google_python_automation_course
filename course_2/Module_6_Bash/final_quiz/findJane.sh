#!/bin/bash

files_jane=$(grep ' jane ' ~/data/list.txt | cut -d' ' -f 3)
#echo $files_jane
for file in  $files_jane; do
  if test -e ~/$file; then
    echo /home/student-01-a9ff97fe3291$file
  fi
  #echo $file
done