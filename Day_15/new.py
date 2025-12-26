import requests

name="sunil"
url=f"https://api.agify.io/?name={name}"

r=requests.get(url)

if r.status_code==200:
    data=r.json()
    print(f"Name:{data['name']}")
    print(f"Predicted Age: {data['age']}")
else:
    print("Failed to fetch data")
    
