import requests
import json

response = requests.get("https://npiregistry.cms.hhs.gov/api/?version=2.1")
print(response.status_code)