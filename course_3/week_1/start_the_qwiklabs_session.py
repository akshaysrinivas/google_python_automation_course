#!/usr/bin/env python3

import sys
import subprocess

name_read = sys.argv[1]
username_read = sys.argv[2]
ip_read = sys.argv[3]

def pem_file_process(name, username, ip_address):
    location = "/mnt/c/Users/SriNi/Downloads/{}".format(name)
    usernameAip = "{}@{}".format(username, ip_address)

    print("{} {} {}".format("mv", location, "~/"))

    #subprocess.run(["mv", location, "~/"])
    #subprocess.run(["chmod", "600", name])
    #subprocess.run(["ssh", "-i", name, usernameAip])

pem_file_process(name_read, username_read, ip_read)

#mv /mnt/c/Users/SriNi/Downloads/qwikLABS-L2398-19969507.pem ~/

#chmod 600 qwikLABS-L2398-19969507.pem

#ssh -i qwikLABS-L2398-19969507.pem student-00-183cab1f2dc2@35.239.125.224