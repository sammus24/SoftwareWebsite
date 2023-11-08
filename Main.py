import streamlit as st
import folium
import geopy
from geopy.geocoders import Nominatim  # You need to import geopy for geolocation
from geopy.extra.rate_limiter import RateLimiter
from streamlit_folium import folium_static  # Import the streamlit_folium extension
from API import search_healthcare_providers  # Import the function from your module


# Function to display the search results page
def display_search_results(zip_code, provider):
    doctors = search_healthcare_providers(zip_code, provider)
    st.title("Search Results")

    # Create a two-column layout
    left_column, right_column = st.columns(2)

    if doctors:
        m = folium.Map(location = [0,0],zoom_start = 1)
        locations = []
        for doctor in doctors:
            geolocator = Nominatim(user_agent="Main.py")  # Create a geolocator instance
            geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

            location = geolocator.geocode(doctor["address"])
            if location is not None:
                lat = location.latitude
                lon = location.longitude
                folium.Marker([lat, lon]).add_to(m)
                locations.append((lat,lon))
               
               
            with left_column:
                st.write("Doctor Name:", doctor["first_name"], doctor["last_name"])
                st.write("Address:", doctor["address"])

        m.fit_bounds(locations)
        with right_column:
            folium_static(m,width = 700)  # Use streamlit_folium to display the map

       

    else:
        left_column("No results found.")

   
# Function to display the search form page
st.title("Healthcare Provider Search")
zip_code = st.text_input("Enter ZIP code:")
provider = st.selectbox(
    "Select Doctor Type:",
    ("Blank","Dentist","Optometrist","Pediatrician","Physcian",
     "Gynecology","Internal Medicicne","Pharmacist","Radiology","Dermatology","Plastic Surgery",
     "Psychiatrist", "Counselor","Surgery"))

if st.button("Search"):
    display_search_results(zip_code, provider)
