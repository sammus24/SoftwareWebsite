import streamlit as st
import requests

st.title("Healthcare Provider Search")

zip_code = st.text_input("Enter ZIP code:")
provider = st.text_input("Enter Provider Type:")

if st.button("Search"):
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
            basic_info = result.get("basic", {})
            address_data = result.get("addresses", [{}])[0]
            address = ", ".join(
                filter(None, [
                    address_data.get("address_1", ""),
                    address_data.get("address_2", ""),
                    address_data.get("city", ""),
                    address_data.get("state", ""),
                    address_data.get("postal_code", "")
                ])
            )

            doctor_info = {
                "first_name": basic_info.get("first_name", ""),
                "last_name": basic_info.get("last_name", ""),
                "address": address
            }

            doctors.append(doctor_info)

        if doctors:
            st.write("Search Results:")
            st.table(doctors)
        else:
            st.write("No results found.")
    else:
        st.write(f"Request failed with status code: {response.status_code}")
