import requests
import json


# Make an API call, and store the response
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explore the structure of the data
response_dicts = r.json()
response_file = 'data/readable_hn_data.json'
with open(response_file, 'w') as f:
    json.dump(response_dicts, f, indent=4)

