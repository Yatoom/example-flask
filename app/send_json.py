import json
import requests

url = 'http://127.0.0.1:5000/'
headers = {'content-type': 'application/json'}
file = 'test.json'

with open(file) as json_data:
    data = json.load(json_data)
    print(data)
    requests.post(url, data=data, headers=headers)