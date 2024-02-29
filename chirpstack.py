import requests

url = "http://52.220.91.130:8080/api/applications"

api_key = "f04941d9-b15c-48b1-a2ab-99e6856e8895"

headers = {
    "Grpc-Metadata-Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}


response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code} - {response.text}")