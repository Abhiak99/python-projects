#!/usr/bin/env python3

import subprocess
import optparse

parser = optparse.OptionParser()

interface = input("interface :   ")
new_mac = input("new MAC :   ")


print("[+] Your old Mac_changer is here ")
print()
print()
print()
subprocess.run("ifconfig ", shell=True, check=False)

print("[+] Changing MAC Address for " + interface + " to "  + new_mac)



subprocess.run("ifconfig "+ interface + " down", shell=True, check=False)
subprocess.run("ifconfig "+ interface + " hw ether "+new_mac, shell=True, check=False)
subprocess.run("ifconfig "+ interface + " up", shell=True, check=False)
