import requests

res = requests.get("https://www.tetricz.com/text/fun.txt")
print("Status code: ", res.status_code)
print("Content length: ", res.headers['Content-Length'])
print(res.text)
