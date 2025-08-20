import requests

url = "https://ipinfo.io/190.60.194.114/json"

try:
    response = requests.get(url)
    data = response.json()
    print(data)
except Exception as e:
    print(f"Error occurred: {e}")
