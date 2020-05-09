#!/usr/bin/env python

import subprocess
import optparse

from pip._vendor.distlib.compat import raw_input

prs = optparse.OptionParser()
prs.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address...")
prs.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

prs.parse_args()

interface = raw_input("Interface > ")
new_mac = raw_input("New MAC > ")

print("[+] changing MAC address for " + interface + "to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

