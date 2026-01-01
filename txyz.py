import requests 


url = "https://api.txyz.ai/v1/sessions"
api_key = "1c9e3970-5b06-42f3-980e-c020440375bf"

headers = {"Authorization": f"Bearer {api_key}"}

response = requests.post(url, headers=headers)

print(response.json())

