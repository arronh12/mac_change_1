#!/usr/bin/env python

import subprocess

from pip._vendor.distlib.compat import raw_input

interface = raw_input("Interface > ")
new_mac = raw_input("New MAC > ")

print("[+] changing MAC address for " + interface + "to " + new_mac)

subprocess.call('ifconfig ' + interface + ' down', shell=True)
subprocess.call('ifconfig ' + interface + ' hw ether '+ new_mac, shell=True)
subprocess.call('ifconfig ' + interface + ' up', shell=True)
