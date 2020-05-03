import subprocess

interface = "eth0"
new_mac = "22:54:78:22:22:88"

print("[+] changing MAC address for " + interface + "to " + new_mac)

subprocess.call('ifconfig ' + interface + ' down', shell=True)
subprocess.call('ifconfig ' + interface + ' hw ether '+ new_mac, shell=True)
subprocess.call('ifconfig ' + interface + ' up', shell=True)
