import urllib.request
import json

try:
    req = urllib.request.urlopen("http://127.0.0.1:8000/?ano=2024")
    print(req.status)
    print("Length:", len(req.read()))
except Exception as e:
    print(e)
