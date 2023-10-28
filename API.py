import requests
import json

parameters ={
    "postal_code": "08054",
   
}

response = requests.get("https://npiregistry.cms.hhs.gov/api/?pretty=on&version=2.1",params=parameters)
print(response.status_code)
formatted_response = json.dumps(response.json(),separators=(",",":"), indent=4)
print(formatted_response)