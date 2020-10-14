#!/usr/bin/env python3

#Import libraries
import csv
import re

"""Returns True if the email address contains the given domain, in the domain position, false if not."""
def contains_domain(address, domain):
    domain_pattern = r"[\w\.-]+@"+domain+"$"
    if re.match(domain_pattern, address):
        return True
    return False

"""Replaces the old domain with the new domain in the received address."""
def replace_domain(address, old_domain, new_domain):
    old_domain_pattern = r""+old_domain+"$"
    address = re.sub(old_domain_pattern, new_domain, address)
    return address

"""Processes the list of emails, replacing any instances of the old domain with the new domain."""
def main():
    old_domain, new_domain = 'abc.edu', 'xyz.edu'
    #csv_file_location = "/home/akshaysrinivas/python-training/Module_3_regex/user_emails.csv"
    #report_file = "/home/akshaysrinivas/python-training/Module_3_regex" + "/updated_user_emails.csv" #/home/<username>/data
    csv_file_location = "/home/student-00-2dea87c5365a/data/user_emails.csv"
    report_file = "/home/student-00-2dea87c5365a/data" + "/updated_user_emails.csv" #/home/<username>/data
    user_email_list = []
    old_domain_email_list = []
    new_domain_email_list = []

    with open(csv_file_location, 'r') as f:
        user_data_list = list(csv.reader(f))
        user_email_list = [data[1].strip() for data in user_data_list[1:]]
        for email_address in user_email_list:
            if contains_domain(email_address, old_domain):
                old_domain_email_list.append(email_address)
                replaced_email = replace_domain(email_address, old_domain, new_domain)
                new_domain_email_list.append(replaced_email)

        email_key = ' ' + 'Email Address'
        email_index = user_data_list[0].index(email_key)

        for user in user_data_list[1:]:
            for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
                if user[email_index] == ' ' + old_domain:
                    user[email_index] = ' ' + new_domain
        f.close()

    with open(report_file, 'w+') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(user_data_list)
        output_file.close()

main()

#ssh -i qwikLABS-L2379-19467677.pem student-00-6fbd5a643cd9@34.122.102.107