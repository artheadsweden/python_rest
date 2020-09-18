import requests

#Use it as the 'x-api-key' header when making any request to the API

key = "3b9ebba7-0493-4617-b0dd-77fa8edadff5"
url = "https://api.thecatapi.com/v1/breeds"

header = {
    'x-api-key': key
}

#responce = requests.get(url + "?api_key=" + key)
responce = requests.request("GET", url, headers=header)

for obj in responce.json():
    print(obj['weight'])