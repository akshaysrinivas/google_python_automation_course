#!/usr/bin/env python3
import os
import requests
#import json

feedback_text_path = '/home/student-03-061b74e5ec6d/supplier-data/descriptions/'
feedback_url = 'http://104.155.145.229/fruits/'

""" feedback_convert_json - This function will read the file and convert it into json format for posting """
def feedback_convert_json(filename, image_file):
    with open(filename) as feedback_data:
        image_name = os.path.splitext(image_file)[0]
        data_formatted = feedback_data.read().split('\n')
        data_dict = {"name": data_formatted[0], "weight": int(data_formatted[1].strip(" lbs")), "description": data_formatted[2], "image_name": image_name+".jpeg"}
    return data_dict

""" This function sends the files to feedback_convert_json function to format the data in json and post the feedback $ """
def post_feedback():
    file_list = os.listdir(feedback_text_path)
    for feedback_file in file_list:
        if feedback_file.endswith('.txt'):
            feedback_data = feedback_convert_json(feedback_text_path+feedback_file, feedback_file)
            #print(feedback_text_path+feedback_file)
            #print(feedback_data)
            #print(feedback_file)
            response = requests.post(feedback_url, json=feedback_data)
            print(response.raise_for_status())
    return True
print(post_feedback())
