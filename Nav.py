import streamlit as st
import folium
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from streamlit_folium import folium_static
from API import search_healthcare_providers
from application import application_function

# Function to display the search results page
def search():
    
    # Function to display the search form page
    st.title("Healthcare Provider Search")
    zip_code = st.text_input("Enter ZIP code:")
    provider = st.selectbox(
        "Select Doctor Type:",
        ("Blank", "Dentist", "Optometrist", "Pediatrician", "Physician",
        "Gynecology", "Internal Medicine", "Pharmacist", "Radiology", "Dermatology", "Plastic Surgery",
        "Psychiatrist", "Counselor", "Surgery"))

    # Add a sorting option
    sort_option = st.selectbox("Sort Results By:", ["Name", "Address"])

    if st.button("Search"):
        display_search_results(zip_code, provider, sort_option)

def display_search_results(zip_code, provider, sort_option):
    doctors = search_healthcare_providers(zip_code, provider)

    # Sort the doctors based on the selected sorting option
    if sort_option == "Name":
        doctors.sort(key=lambda doctor: (doctor["last_name"], doctor["first_name"]))
    elif sort_option == "Address":
        doctors.sort(key=lambda doctor: doctor["address"])

    st.title("Search Results")

    # Create a two-column layout
    left_column, right_column = st.columns(2)

    if doctors:
        m = folium.Map(location=[0, 0], zoom_start=1)
        locations = []
        for idx, doctor in enumerate(doctors):
            geolocator = Nominatim(user_agent="Main.py")
            geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

            location = geolocator.geocode(doctor["address"])
            if location is not None:
                lat = location.latitude
                lon = location.longitude
                marker = folium.Marker([lat, lon], tooltip=doctor["address"])
                marker.add_to(m)
                locations.append((lat, lon))

            with left_column:
                st.write("Doctor Name:",doctor["last_name"], doctor["first_name"])
                if st.button(f"Apply, {idx}"):
                    application_function()
                st.write("Address:", doctor["address"])

        m.fit_bounds(locations)
        with right_column:
            folium_static(m, width=700)

    else:
        left_column("No results found.")


if __name__ == "__main__":
    search()