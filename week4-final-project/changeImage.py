#!/usr/bin/env python3
import os
from PIL import Image

current_directory = os.getcwd()
image_dir = current_directory+'/supplier-data/images/'
#icon_save_dir = current_directory+'/images_icon/'
count = 0


""" image_convert(), Function convert row image to desired format """
def image_convert(image_in):
    image_for_process = Image.open(image_in)
    processed_image = image_for_process.convert('RGB').resize((600,400))
    image_for_process.close()
    return processed_image

""" Checking if the end directory exist or not. If not exist new directory is created """
#if not os.path.exists(icon_save_dir):
#    os.makedirs(icon_save_dir)

""" Process started to convert the file from given location to /opt/icon/ location """

for image_file in os.listdir(image_dir):
    if image_file.endswith('tiff'):
        count += 1
        print(image_dir+image_file)
        new_image = os.path.splitext(image_file)[0]
        image_convert(image_dir+image_file).save(image_dir+new_image+".jpeg", "JPEG")
        print("Image {} converted".format(count))