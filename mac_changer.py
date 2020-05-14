#!/usr/bin/env python

import subprocess
import optparse

def get_arguments():
    prs = optparse.OptionParser()
    prs.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address...")
    prs.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = prs.parse_args()
    if not options.interface:
        prs.error("[*] Error. Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        prs.error("[*] Error. no MAC address entered, use --help for more info.")
    return options


def change_mac(interface, new_mac):
    print("[+] changing MAC address for " + interface + "to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()
change_mac(options.interface, options.new_mac)
result = subprocess.check_output(["ifconfig", options.interface])
print(result)

