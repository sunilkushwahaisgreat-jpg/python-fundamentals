import requests

url="https://api.github.com"

r=requests.get(url)
print(r.status_code)
print(r.headers["Content-Type"])

data=r.json()

print(data)
print(data["current_user_url"])
