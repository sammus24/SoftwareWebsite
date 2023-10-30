import requests
import json

parameters = {
    "postal_code": "08054",
    "taxonomy_description":"dentist"
}

response = requests.get("https://npiregistry.cms.hhs.gov/api/?pretty=on&enumeration_type=NPI-1&version=2.1", params=parameters)

if response.status_code == 200:
    data = response.json()
    results = data.get("results", [])  # Get the "results" array from the JSON data
    
    for result in results:
        first_name = result.get("basic", {}).get("first_name", "")  # Get doctor's first name
        last_name = result.get("basic", {}).get("last_name", "")  # Get doctor's last name
        
        # Get the full address
        address_data = result.get("addresses", [{}])[0]
        address = ", ".join(filter(None, [address_data.get("address_1", ""), address_data.get("address_2", ""), address_data.get("city", ""), address_data.get("state", ""), address_data.get("postal_code", "")]))
        
        # Print doctor's name and address
        print("Doctor's Name:", first_name,last_name)
        print("Address:", address)
else:
    print("Request failed with status code:", response.status_code)
