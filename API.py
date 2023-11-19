import requests
import json


def search_healthcare_providers(zip_code, provider):
    parameters = {
        "postal_code": zip_code,
        "taxonomy_description": provider
    }

    response = requests.get("https://npiregistry.cms.hhs.gov/api/?pretty=on&enumeration_type=NPI-1&version=2.1", params=parameters)

    if response.status_code == 200:
        data = response.json()
        results = data.get("results", [])  # Get the "results" array from the JSON data

        doctors = []
        for result in results:
            first_name = result.get("basic", {}).get("first_name", "")  # Get doctor's first name
            last_name = result.get("basic", {}).get("last_name", "")  # Get doctor's last name

            # Look for NPI number in different possible locations within the response
            NPI_number = None
            if "number" in result:
                NPI_number = result["number"]
            elif "enumeration_type" in result and result["enumeration_type"] == "NPI-2":
                NPI_number = result.get("number", "")

            
            
            # Get the full address
            address_data = result.get("addresses", [{}])[0]
            code = zip_code
    
            address = ", ".join(filter(None, [address_data.get("address_1", ""), address_data.get("address_2", ""), address_data.get("city", ""), address_data.get("state", ""), code]))
            
            doctor_info = {
                "first_name": first_name,
                "last_name": last_name,
                "address": address,
                "NPI":NPI_number
            }
                    
            doctors.append(doctor_info)
        return doctors
    else:
        return None
    
    
