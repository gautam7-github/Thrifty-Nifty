import requests as http
import json

# testing the ngrok service
url = ""


response = http.get(url)
jsonData = json.loads(response.content)

testTickers = [
    'INFY',
    'MARUTI',
    'LT',
    'UPL'
]

if __name__ == "__main__":
    for ticker in testTickers:
        print(jsonData[ticker])
