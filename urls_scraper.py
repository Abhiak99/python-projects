import requests
import sys
import re

if len(sys.argv)!=2:
	print("Usage: python3 {} [url]".format(sys.argv[0]))
	sys.exit()


url = sys.argv[1]
if url[-1]=='/':
	url = url.strip('/')
# print(url)

r = requests.get(url, allow_redirects=True)

# print(r.status_code)
# print(r.text)

pattern = re.compile(r'\bhttps?://[^/\s]+\b')
matches = pattern.findall(r.text)

rel = re.compile(r'\b(?:/[^/\s]+)+\b')
matches = matches + [url+k for k in rel.findall(r.text)]

scraped = [n for n in matches]

scraped_final = list(set(scraped))
# print(scraped_final)

for i in scraped_final:
	print(i)                                                                                                                     
