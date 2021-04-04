import json, sys
from urllib.request import Request, urlopen

token = sys.argv[1]
with open('testfile.txt') as f:
        tag = f.read()

url = 'https://api.github.com/repos/Aboghazala/zmaker/releases'
data = {"tag_name": tag, "name": f"my release - {tag}", "prerelease": True, "draft": False,
        "body": "this is the body description"}
headers = {'Accept': 'application/vnd.github.v3+json', 'Authorization': f'token {token}'}

data = json.dumps(data)
data = str(data).encode('utf-8')

request = Request(url, headers=headers, data=data)

try:
    res = urlopen(request)
except Exception as e:
        print(e)
print(res.headers)
print(res.read())
