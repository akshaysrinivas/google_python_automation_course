#!/usr/bin/env python3
import os
import requests
#import json

feedback_text_path = '/data/feedback/'
feedback_url = 'http://34.133.61.219/feedback/'

""" feedback_convert_json - This function will read the file and convert it into json format for posting """
def feedback_convert_json(filename):
    with open(filename) as feedback_data:
        data_formatted = feedback_data.read().split('\n')
        data_dict = {"title": data_formatted[0], "name": data_formatted[1], "date": data_formatted[2], "feedback": data_formatted[3]}
    return data_dict

""" This function sends the files to feedback_convert_json function to format the data in json and post the feedback $ """
def post_feedback():
    file_list = os.listdir(feedback_text_path)
    for feedback_file in file_list:
        if feedback_file.endswith('.txt'):
            feedback_data = feedback_convert_json(feedback_text_path+feedback_file)
            #print(feedback_text_path+feedback_file)
            #print(feedback_data)
            #print(feedback_file)
            response = requests.post(feedback_url, json=feedback_data)
            print(response.raise_for_status())
    return True
print(post_feedback())
