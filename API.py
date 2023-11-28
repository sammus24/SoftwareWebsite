import requests
from pyzipcode import ZipCodeDatabase
import streamlit as st



def specific_provider(provider, code):
    parameters = {
        "postal_code": code,
        "organization_name": provider,
        "pretty": "on",
        "enumeration_type": "NPI-2",
        "version": "2.1"
    }
    
    api_url = "https://npiregistry.cms.hhs.gov/api/"

    try:
        response = requests.get(api_url, params=parameters)
        if response.status_code == 200:
            data = response.json()
            # Extracting relevant information
            results = data.get("results", [])
            if results:
                for result in results:
                    basic_info = result.get("basic", {})
                    organization_name = basic_info.get("organization_name")
                    # Check if the organization_name matches the provided provider
                    if organization_name and organization_name.lower() == provider.lower():
                        return True
                return "Provider not found"
            else:
                return "No results found"
        else:
            return f"Request failed with status code: {response.status_code}"
    except requests.RequestException as e:
        return f"Request error: {str(e)}"

    
    
    
def search_healthcare_providers(zip_code, provider, radius):
    
    zip_codes = Zip_codes(zip_code, radius)
    final = []

    for code in zip_codes:
        parameters = {
            "postal_code": code,
            "taxonomy_description": provider,
            
            
        }

        response = requests.get("https://npiregistry.cms.hhs.gov/api/?pretty=on&enumeration_type=NPI-2&version=2.1", params=parameters)

        if response.status_code == 200:
            data = response.json()
            results = data.get("results", [])
            
            

            for result in results:
                organization = result.get("basic",{}).get("organization_name")
                NPI_number = result.get("number", "")

                address_data = result.get("addresses", [{}])[0]
                address = ", ".join(filter(None, [address_data.get("address_1", ""), address_data.get("address_2", ""), address_data.get("city", ""), address_data.get("state", ""),code]))

                doctor_info = {
                    "address": address,
                    "organization":organization,
                    "NPI": NPI_number
                }
                
               
                final.append(doctor_info)
        else:
            # Handle potential errors
            print(f"Failed to fetch data for {code}. Status code: {response.status_code}")

    return final

def Zip_codes(zip, radius): 
    if zip is None or not zip.strip():
        st.warning('Please Enter a Valid Zip Code')
        return []


    zcdb = ZipCodeDatabase()
    in_radius = [z.zip for z in zcdb.get_zipcodes_around_radius(zip, radius)]
    return in_radius



doctor = specific_provider('South Jersey Dental Care','08057')

print(doctor)