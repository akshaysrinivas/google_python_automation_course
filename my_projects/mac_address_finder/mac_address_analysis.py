#!/usr/bin/env python3
import os
import datetime

#mac_address_list = []
mac_count = {}

with open("mac_address.txt") as mac_address:
    mac_address_list = mac_address.readlines()

for mac in mac_address_list:
    if mac.strip() not in mac_count:
        mac_count[mac.strip()] = 1
    else:
        mac_count[mac.strip()] += 1
for mac, mac_nos in mac_count.items():
    print("{} : {}".format(mac, mac_nos))

time_now = datetime.datetime.now()

if os.path.exists("mac_count_from_list.txt"):
    with open("mac_count_from_list.txt", "a") as mac_write:
        mac_write.write("\n\n{}".format(str(time_now)))
        for mac, mac_nos in mac_count.items():
            #print("{} : {}".format(mac, mac_nos))
            mac_write.write("{} : {}\n".format(mac, mac_nos))
        print("File written succesfully")
else:
    with open("mac_count_from_list.txt", "w") as mac_write:
        mac_write.write("\n\n{}".format(str(time_now)))
        for mac, mac_nos in mac_count.items():
            #print("{} : {}".format(mac, mac_nos))
            mac_write.write("{} : {}\n".format(mac, mac_nos))
        print("File \"mac_count_from_list.txt\" created and written succesfully")    
#print(mac_address_list)
