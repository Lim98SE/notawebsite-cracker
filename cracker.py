import requests
import os

# notawebsite cracker
# put codes in codes.txt, seperated by newline
# for requests run `pip install requests` (or whatever you need to do to run pip)
# just open with whatever python interpreter you want and run it, all valid codes will get their output in the output folder

if not os.path.exists("output"):
    os.mkdir("output")

if not os.path.exists("log.txt"):
    open("log.txt", "w").close()

data = b"""-----------------------------2147034967845007372574805033
Content-Disposition: form-data; name="code"

CodeGoesHere
-----------------------------2147034967845007372574805033--
"""

headers = {
"Host": "codes.thisisnotawebsitedotcom.com",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0",
"Accept": "*/*",
"Accept-Language": "en-US,en;q=0.5",
"Referer": "https://thisisnotawebsitedotcom.com/",
"Content-Type": "multipart/form-data; boundary=---------------------------2147034967845007372574805033",
"Content-Length": "177",
"Content-Disposition": "form-data",
"Origin": "https://thisisnotawebsitedotcom.com",
"Connection": "keep-alive",
"Sec-Fetch-Dest": "empty",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Site": "same-site",
"Priority": "u=0"
}

def send_request(code):
    req_data = data.replace(b"CodeGoesHere", code.encode("utf-8"))
    req = requests.post("https://codes.thisisnotawebsitedotcom.com", data=req_data, headers=headers)
    
    if (req.status_code == 200):
        print(f"{code} is valid!")

        with open(f"output/{code}.html", "wb") as file:
            file.write(req.content)
    
    else:
        print(f"{code} is invalid.")
    
    with open("log.txt", "a") as file:
        file.write(f"{code}: {'Valid' if req.status_code == 200 else 'Invalid'}\n")

def correct(code):
    code = code.lower()
    newcode = ""

    for i in code:
        if i in "abcdefghijlmnopqrstuvwxyz1234567890":
            newcode += i
    
    return newcode

with open("codes.txt") as file:
    codes = file.readlines()

for i in codes:
    send_request(correct(i.strip()))