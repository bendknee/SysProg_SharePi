import requests
r = requests.get("http://127.0.0.1:5000/verification?code=12345")
print(r.json()["status"])