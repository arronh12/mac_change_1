#!/usr/bin/env python

import subprocess
import optparse

def get_arguments():
    prs = optparse.OptionParser()
    prs.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address...")
    prs.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    return prs.parse_args()



def change_mac(interface, new_mac):
    print("[+] changing MAC address for " + interface + "to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

(options, arguments) = get_arguments()
change_mac(options.interface, options.new_mac)


