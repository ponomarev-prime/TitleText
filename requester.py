import json
import requests

# Чтение данных из файла config.json
with open('config.json', 'r') as file:
    data = json.load(file)

url = 'http://localhost:8000/titlegen'

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())
