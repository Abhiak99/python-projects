#!/usr/bin/env python3

import subprocess
import argparse
from time import sleep

parser = argparse.ArgumentParser()



parser.add_argument("-i", "--interface", dest="interface", help="The MAC Address of which interface you want to change")
parser.add_argument("-m", "--mac", dest="new_mac", help="The MAC Address you want to change")
args = parser.parse_args()

interface = args.interface

new_mac = args.new_mac


print("[+] Your old Mac_changer is here ")

subprocess.run("ifconfig ", shell=True, check=False)

print("[+] Changing MAC Address for " + interface + " to "  + new_mac)



subprocess.run("ifconfig "+ interface + " down", shell=True, check=False)
subprocess.run("ifconfig "+ interface + " hw ether "+new_mac, shell=True, check=False)
subprocess.run("ifconfig "+ interface + " up", shell=True, check=False)

print("\n[+] Running Command ifconfig to check the new MAC Address")
sleep(2)
subprocess.run(["ifconfig"])