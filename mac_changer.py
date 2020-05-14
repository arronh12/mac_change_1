#!/usr/bin/env python

import subprocess
import optparse
import re


# function to define and add parse options.
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


# function to change MAC address for specific interface
def change_mac(interface, new_mac):
    print("[+] changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


# function to use regex module that extracts MAC address from ifconfig command
def current_mac(interface):
    result = subprocess.check_output(["ifconfig", interface])
    captured_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", result)

    if captured_mac:
        return captured_mac.group(0)
    else:
        print("[*] Error - could not read MAC address.")


#function to validate that MAC has been changed to user input
def validate_mac(new_mac):
    if new_mac == options.new_mac:
        print("[*] MAC address successfully changed too " + str(new_mac))
    else:
        print("[*] Error - MAC address did not change, use --help for more information")


# function calls
options = get_arguments()
mac = current_mac(options.interface)
print("[*] Current MAC: " + str(mac))
change_mac(options.interface, options.new_mac)
validate_mac(current_mac(options.interface))



