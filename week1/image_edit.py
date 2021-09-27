#!/usr/bin/env python3
import os
from PIL import Image

current_directory = os.getcwd()
image_dir = current_directory+'/images/'
icon_save_dir = '/home/akshay/images_icon/'
count = 0


""" image_convert(), Function convert row image to desired format """
def image_convert(image_in):
    image_for_process = Image.open(image_in)
    processed_image = image_for_process.convert('RGB').rotate(270).resize((128,128))
    image_for_process.close()
    return processed_image

""" Checking if the end directory exist or not. If not exist new directory is created """
if not os.path.exists(icon_save_dir):
    os.makedirs(icon_save_dir)

""" Process started to convert the file from given location to /opt/icon/ location """

for image_file in os.listdir(image_dir):
    if image_file.endswith('48dp'):
        count += 1
        image_convert(image_dir+image_file).save(icon_save_dir+image_file, "JPEG")
        print("Image {} converted".format(count))