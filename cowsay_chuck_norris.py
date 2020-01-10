import sys
import cowsay
import requests

ENDPOINT = 'https://api.chucknorris.io/jokes/random?category=sport'
EXECUTION_DATE = sys.argv[1]

print(f"EXECUTION_DATE: {EXECUTION_DATE}")
response = requests.get(ENDPOINT)
cowsay.dragon(response.json()['value'])
