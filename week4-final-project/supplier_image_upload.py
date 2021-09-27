#!/usr/bin/env python3
import requests
import os
# This example shows how a file can be uploaded using
# The Python Requests module

count = 0

url = "http://localhost/upload/"
images_location = os.getcwd()+'/supplier-data/images/' 
for image_file in os.listdir(images_location):
    #print(image_file)
    if image_file.endswith('jpeg'):
       #  print(images_location+image_file)
        count += 1
        with open(images_location+image_file, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
            print("\nFile {} uploaded".format(count))
