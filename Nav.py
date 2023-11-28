import streamlit as st
import folium
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from streamlit_folium import folium_static
from application import application_function
from API import search_healthcare_providers
from print import generate_pdf

def display_search_results(zip_code, provider, sort_option, radius):

   
    doctors = search_healthcare_providers(zip_code, provider, radius)

    # Sort the doctors based on the selected sorting option
    if sort_option == "Name":
        doctors.sort(key=lambda doctor: (doctor["organization"]))
    elif sort_option == "Name":
        doctors.sort(key=lambda doctor: (doctor["organization"]),reverse= True)
    elif sort_option == "Address":
        doctors.sort(key=lambda doctor: doctor["address"])

    st.title("Search Results")

    # Create a two-column layout
    left_column, right_column = st.columns(2)

    if doctors:
        geolocator = Nominatim(user_agent="Nav.py")
        m = folium.Map(location=[0, 0], zoom_start=1)
        locations = []
        for idx, doctor in enumerate(doctors):
            with left_column:
                try:
                    location = geolocator.geocode(doctor["address"])
                    if location is not None:
                        st.write("Organization Name: ",doctor['organization'])                     
                        #st.write("Doctor Name:", doctor["last_name"], doctor["first_name"])
                        number = doctor['NPI']
                        st.write("Address:", doctor["address"])
                        
                        st.button(f"Apply Here",key = number,on_click= application_function)                          
                        lat = location.latitude
                        lon = location.longitude
                        marker = folium.Marker([lat, lon], tooltip=doctor["address"])
                        marker.add_to(m)
                        locations.append((lat, lon))
                except Exception as e:
                    st.warning("Error getting location")
        with right_column:
            if locations:
                m.fit_bounds(locations)
                folium_static(m, width=700)

            pdf = generate_pdf(doctors)

            if st.download_button(
                label='Download Results',
                data=pdf,
                file_name='Doctor_results.pdf'
             ):
                st.session_state.page = 'results'

    if not doctors:
        st.write("No results found.")

def results_page(zip_code, provider, sort_option, radius):
    st.session_state.page = "results"
    st.session_state.rerun_flag = True

    display_search_results(zip_code, provider, sort_option, radius)

def Navigation():
    st.title("Healthcare Provider Search")

    zip_code = st.text_input("Enter ZIP code:")

    radius = st.text_input("Enter Radius (Default Radius = 5): ")
    if not radius:
        radius = 5  # Set default radius to 5 if not provided
    else:
        radius = int(radius)
    provider = st.selectbox(
        "Select Doctor Type:",
        ("Blank", "Dentist", "Optometrist", "Pediatrician", "Physician",
        "Gynecology", "Internal Medicine", "Pharmacist", "Radiology", "Dermatology", "Plastic Surgery",
        "Psychiatrist", "Counselor", "Surgery"))
    sort_option = st.selectbox("Sort Results By:", ["Name", "Address"])
    # clear the search box

    if st.button("Search"):
         # Check if the entered ZIP code is valid
        if is_valid_zip(zip_code):
            results_page(zip_code, provider, sort_option, radius)
        else:
            st.warning('Please Enter a Valid 5-digit ZIP Code')
       
def is_valid_zip(zip_code):
    # Check if the ZIP code meets the required conditions for validity (you may need a more robust check)
    return len(zip_code) == 5 and zip_code.isdigit()