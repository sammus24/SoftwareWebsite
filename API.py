import requests
from pyzipcode import ZipCodeDatabase



def search_healthcare_providers(zip_code, provider, radius):
    zip_codes = Zip_codes(zip_code, radius)
    final = []

    for code in zip_codes:
        parameters = {
            "postal_code": code,
            "taxonomy_description": provider
        }

        response = requests.get("https://npiregistry.cms.hhs.gov/api/?pretty=on&enumeration_type=NPI-1&version=2.1", params=parameters)

        if response.status_code == 200:
            data = response.json()
            results = data.get("results", [])
            
            

            for result in results:
                first_name = result.get("basic", {}).get("first_name", "")
                last_name = result.get("basic", {}).get("last_name", "")
                NPI_number = result.get("number", "")

                address_data = result.get("addresses", [{}])[0]
                address = ", ".join(filter(None, [address_data.get("address_1", ""), address_data.get("address_2", ""), address_data.get("city", ""), address_data.get("state", ""),code]))

                doctor_info = {
                    "first_name": first_name,
                    "last_name": last_name,
                    "address": address,
                    "NPI": NPI_number
                }
                
               
                final.append(doctor_info)
        else:
            # Handle potential errors
            print(f"Failed to fetch data for {code}. Status code: {response.status_code}")

    return final

def Zip_codes(zip, radius): 
    zcdb = ZipCodeDatabase()
    in_radius = [z.zip for z in zcdb.get_zipcodes_around_radius(zip, radius)]
    return in_radius

