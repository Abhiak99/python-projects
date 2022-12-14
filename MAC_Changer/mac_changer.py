#!/usr/bin/env python3

import subprocess
import argparse
from time import sleep
import re


def current_mac(interface):
	ifconfig_output = subprocess.check_output(["ifconfig", interface])

	mac = re.search(r"(\w{2}[:-]){5}\w{2}", str(ifconfig_output))
	return mac.group(0)
	


parser = argparse.ArgumentParser()

parser.add_argument("-i", "--interface", dest="interface", help="The MAC Address of which interface you want to change")
parser.add_argument("-m", "--mac", dest="new_mac", help="The Updated MAC Address you want")
args = parser.parse_args()

if not args.interface:
	parser.error("[-] Specify an interface")
elif not args.new_mac:
	parser.error("[-] Specify a new MAC")

interface = args.interface
new_mac = args.new_mac

if not interface:
	parser.error("[-] Specify an interface")
elif not new_mac:
	parser.error("[-] Specify a new MAC")


print("[+] Your old Mac_changer is here :   {}\n".format(current_mac(interface)))


print("[+] Changing MAC Address for " + interface + " to "  + new_mac)



subprocess.run("ifconfig "+ interface + " down", shell=True, check=False)
subprocess.run("ifconfig "+ interface + " hw ether "+new_mac, shell=True, check=False)
subprocess.run("ifconfig "+ interface + " up", shell=True, check=False)


print("\n[+] Running Command ifconfig to check the new MAC Address\n")
sleep(2)

mac = current_mac(interface)

if mac:
	print("The New MAC Address is {}".format(mac))
else:
	print("[-] MAC address is not here")