import requests

url = "https://reqres.in/api/users"

payload = {"name": "Nisse","job": "leader"}
print(payload)
headers = {
  'Content-Type': 'application/json'
}

response = requests.post(url, json=payload)
#response = requests.request("POST", url, headers=headers, data = payload)

print(response.json())