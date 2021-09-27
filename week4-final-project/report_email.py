#!/usr/bin/env python3

import os 
import datetime
import reports
import emails

current_date = datetime.datetime.now().strftime('%Y-%m-%d')

def pdf_generation(directory_location):
    content_pdf = ""
    for feedback_file in os.listdir(directory_location):
        if feedback_file.endswith('.txt'):
            with open(directory_location+feedback_file) as feedback_data:
                data_formatted = feedback_data.read().split('\n')
                content_pdf += "name: "+data_formatted[0]+"<br/>"+"weight: "+data_formatted[1]+"<br/><br/>"
    return content_pdf

if __name__ == "__main__":
  description_path = "/home/student-03-061b74e5ec6d/supplier-data/descriptions/"
  title = "Process Updated on " + current_date 
  #generate the package for pdf body
  PDF_Generation = pdf_generation(description_path)
  reports.generate_report("/tmp/processed.pdf", title, PDF_Generation)

  #generate email information
  sender = "automation@example.com"
  receiver = "student-03-061b74e5ec6d@example.com"
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  attachment = "/tmp/processed.pdf"
  
  #generate email for the online fruit store report and pdf attachment
  email_message = emails.generate_email(sender, receiver, subject, body, attachment)
  emails.send_email(email_message)