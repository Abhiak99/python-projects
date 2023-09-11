import pytesseract
from PIL import Image
import requests
import base64
from io import BytesIO
import re


url = ""
s = requests.Session()
r = s.get(url)
captcha = ""

def read_captcha(base64_data):
    try:
        image_data = base64.b64decode(base64_data)
        image_stream = BytesIO(image_data)
        image = Image.open(image_stream)
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        print(f"Error: {e}")
        return None
totalrequest = 300

while(totalrequest!=1):
    r = s.post(url, data={"captcha":captcha})
    ## Basedata and need to be changed to required results.
    basedata= re.findall(r'<img src="data:image/png;base64,(.*)" alt="Generated Image">', r.text)[0]
    captcha = read_captcha(basedata)
    #totalrequest = int(re.findall(r'number of captchas (.*) more to go!', r.text)[0])
    totalrequest -=1
    print("captcha = {}  : Total Number {}".format(captcha,totalrequest))


print(s.cookies)
