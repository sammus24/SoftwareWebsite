import streamlit as st
from API import search_healthcare_providers  # Import the function from your module

# Function to display the search results page
def display_search_results(zip_code, provider):
    doctors = search_healthcare_providers(zip_code, provider)
    st.title("Search Results")

    if doctors:
        st.write("Search Results:")
        st.table(doctors)
    else:
        st.write("No results found.")
    st.write("Back to [Search](#search)")

# Function to display the search form page

st.title("Healthcare Provider Search")
zip_code = st.text_input("Enter ZIP code:")
provider = st.text_input("Enter Provider Type:")

if st.button("Search"):
    display_search_results(zip_code, provider)



