import requests

url = "http://api.apilayer.com/exchangerates_data/convert?to=ILS&from=USD&amount=1"

payload = {}
headers= {
  "apikey": "lEQGZ4yZw5GQK7PWSJZ4SYXVX0boIh1i"
}

response = requests.request("GET", url, headers=headers, data = payload)
data = response.json()
results = data['result']
print(results)
