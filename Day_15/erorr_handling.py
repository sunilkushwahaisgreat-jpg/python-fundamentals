import requests

url="https://api.github.com/invalidendpoint"

try:
    r=requests.get(url)
    r.raise_for_status()
    print(r.json())
except requests.exceptions.HTTPError as err:
    print("HTTP error: ", err)
except requests.exceptions.RequestException as err:
    print("Request Failed: ",err)
