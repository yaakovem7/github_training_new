import requests

res = requests.get('http://google.com')
if res.ok:
    print(res.content)
