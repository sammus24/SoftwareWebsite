import streamlit as st
import folium
from geopy.geocoders import Bing

def location(doctor):
    # Geolocation of the doctor's address using Bing Maps API
    geolocator = Bing(api_key="AiD2FXje7LL88RhGVmH1mhdAr1-LQC2aApNC1oPG3Psnj_4NStiayQh_Vuct1moh")

    my_map = folium.Map()  # Initialize the map outside the loop

    for doc in doctor:
        try:
            # Accessing the address field properly from the doctor's dictionary
            address = f"{doc['address']}, USA"
            provider =f"{doc['organization']}"
            phone = f"{doc['phone']}"
            location = geolocator.geocode(address)
            
            if location is not None:
                lat = location.latitude
                lon = location.longitude
                # Add a marker for each doctor's location with a tooltip indicating the address
                tooltip_text = f"Provider: {provider}<br>Address: {address}<br>Phone: {phone}"
                folium.Marker([lat, lon], popup="Doctor", tooltip= tooltip_text).add_to(my_map)
        except Exception as e:
            st.write(f"Error getting location for {doc['address']}: {e}")
    
    if my_map:
        # Fit the map to the bounds of the markers
        my_map.fit_bounds(my_map.get_bounds())
    
    return my_map
