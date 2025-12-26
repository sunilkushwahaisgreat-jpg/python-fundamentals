import requests

url="https://httpbin.org/post"

data={
    "Name":"Sunil",
    "Course":"Python"
}

r=requests.post(url,data=data)

print("Status Code: ",r.status_code)
print(r.json())

payload={
    "name":"Sunil",
    "level":"Beginner"
}

r=requests.post(url,json=payload)

print(r.status_code)
print(r.json()['json'])

url = "https://httpbin.org/headers"

headers={
    "User-Agent": "Sunilpythonclient/1.0",
    "Accept": "application/json"
}

r=requests.get(url, headers=headers)

print(r.json())

url = "https://httpbin.org/basic-auth/user/pass"

r=requests.get(url, auth=("user","pass"))

print(r.status_code)
print(r.json())
