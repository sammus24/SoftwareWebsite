import requests
from pyzipcode import ZipCodeDatabase
import streamlit as st
from concurrent.futures import ThreadPoolExecutor
from functools import partial
import asyncio
import httpx
from geopy.distance import geodesic
from geopy.geocoders import Bing

import time



# Using a dictionary as a cache for API responses
api_cache = {}

def fetch_data_batch(api_url, parameters_list):
    results = []

    with ThreadPoolExecutor(max_workers=5) as executor:
        # Partially apply the API URL to the requests function
        fetch = partial(requests.get, api_url)

        # Fetch data for each parameter in parallel
        responses = executor.map(fetch, parameters_list)

        # Process responses
        for response in responses:
            if response.status_code == 200:
                data = response.json()
                results.append(data.get("results", []))
            else:
                # Handle potential errors
                st.warning(f"Failed to fetch data. Status code: {response.status_code}")

    return results
def specific_provider(provider, code):
    info = []
    parameters_list = [
        {
            "postal_code": code,
            "organization_name": provider,
            "pretty": "on",
            "enumeration_type": "NPI-2",
            "version": "2.1"
        }
        # Additional parameters if needed can be added in this list
    ]

    api_url = "https://npiregistry.cms.hhs.gov/api/"

    try:
        # Fetch data in batches using parallel processing
        results = fetch_data_batch(api_url, parameters_list)

        # Process results from multiple API calls
        for result_set in results:
            for result in result_set:
                # Process and append the data as needed
                organization_name = result.get("basic", {}).get("organization_name")
                taxonomies = result.get("taxonomies", [])
                if taxonomies:
                    taxonomy_desc = taxonomies[0].get("desc")
                    # Process taxonomy description

                addresses = result.get("addresses", [{}])[0]
                if addresses:
                    telephone_number = addresses.get("telephone_number")  # Assuming first address
                    address = ", ".join(filter(None, [addresses.get("address_1", ""), addresses.get("address_2", ""), addresses.get("city", ""), addresses.get("state", ""), code]))
                    # Process address and telephone number

               

                # Create information dictionary and append to 'info' list
                information = {
                    "org_name": organization_name,
                    "taxonomy_description": taxonomy_desc,
                    "telephone_number": telephone_number,
                    "address": address
                }
                info.append(information)

    except requests.RequestException as e:
        # Handle request exceptions gracefully
        st.error(f"Request Exception: {e}")

    return info

async def fetch_data(url, params):
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        return response.json()

async def fetch_data_async(zip_codes, provider):
    api_url = "https://npiregistry.cms.hhs.gov/api/"
    params_list = [
        {
            "postal_code": code,
            "taxonomy_description": provider,
            "pretty": "on",
            "enumeration_type": "NPI-2",
            "version": "2.1"
        }
        for code in zip_codes
    ]

    tasks = [fetch_data(api_url, params) for params in params_list]
    results = await asyncio.gather(*tasks)

    return results


def search_healthcare_providers(zip_code, provider, radius):
    # Fetch data for the provided zip code
    zip_codes = [zip_code]

    # If a valid zip code is provided, fetch data for surrounding zip codes
    if zip_code.strip():
        zip_codes += Zip_codes(zip_code, radius)

    final = []
    
     # Geolocate the provided ZIP code
    geolocator = Bing(api_key="AiD2FXje7LL88RhGVmH1mhdAr1-LQC2aApNC1oPG3Psnj_4NStiayQh_Vuct1moh")

    location_zip = geolocator.geocode(zip_code)
    
    if location_zip is None:
        return False
    
    zip_coords = (location_zip.latitude, location_zip.longitude)

    # Batch the parameters for multiple API calls
    parameters_list = [
        {
            "postal_code": code,
            "taxonomy_description": provider,
            "pretty": "on",
            "enumeration_type": "NPI-2",
            "version": "2.1"
        }
        for code in zip_codes
    ]

    api_url = "https://npiregistry.cms.hhs.gov/api/"

    try:
        # Fetch data in batches using parallel processing
        results = fetch_data_batch(api_url, parameters_list)

        # Process results from multiple API calls
        for result_set in results:
            for result in result_set:
                # Extract NPI number from the API response
                npi_number = result.get("number", "")
                # Process and append the data as needed
                organization_name = result.get("basic", {}).get("organization_name")
               

                addresses = result.get("addresses", [{}])[0]
                if addresses:
                    telephone_number = addresses.get("telephone_number")  # Assuming first address
                    postal_code = addresses.get("postal_code", "")[:5]  # Extract first 5 digits of the postal code
                    address = ", ".join(filter(None, [addresses.get("address_1", ""), addresses.get("address_2", ""), addresses.get("city", ""), addresses.get("state", ""), postal_code]))
                    # Process address and telephone number
                    location = geolocator.geocode(address)
                    if location is not None:
                        address_coords = (location.latitude, location.longitude)
                        distance = geodesic(zip_coords, address_coords).miles
                        if distance <= radius:
                          # Create information dictionary and append to 'final' list
                            information = {
                                "organization": organization_name,
                                "phone": telephone_number,
                                "address": address,
                                "NPI":npi_number
                            }
                            final.append(information)

    except requests.RequestException as e:
        # Handle request exceptions gracefully
        st.error(f"Request Exception: {e}")

    return final


def Zip_codes(zip, radius): 
    if zip is None or not zip.strip():
        st.warning('Please Enter a Valid Zip Code')
        return []


    zcdb = ZipCodeDatabase()
    in_radius = [z.zip for z in zcdb.get_zipcodes_around_radius(zip, radius)]
    return in_radius


"""
start_time = time.time()

doc = search_healthcare_providers('08054','dentist',5)
if not doc:  # Check if the doc list is empty
    print("No Results")
else:
    for i in doc: 
        print(i)
        

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution Time: {execution_time} seconds")
"""