#!/bin/python3
import requests

url = "https://www.virustotal.com/api/v3/ip_addresses/195.23.212.226"

headers = {
    "accept": "application/json",
    "x-apikey": "5a134b511bc672a79c5cb21b921827724f4de331096f0e32743e61520bd7e792"
}

response = requests.get(url, headers=headers)

print(response.text)
