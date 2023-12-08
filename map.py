import streamlit as st
import folium
from geopy.distance import geodesic
from geopy.geocoders import Bing

def are_within_radius(zipcode, doctors, radius_mi):
    # Geolocate the provided ZIP code
    geolocator = Bing(api_key="AiD2FXje7LL88RhGVmH1mhdAr1-LQC2aApNC1oPG3Psnj_4NStiayQh_Vuct1moh")

    location_zip = geolocator.geocode(zipcode)
    
    if location_zip is None:
        return False
    
    zip_coords = (location_zip.latitude, location_zip.longitude)
    list = []
    # Geolocate addresses and check distances
    for address in doctors:
        
        try:
            add = address.get('address')
            location = geolocator.geocode(add)
            if location is not None:
                address_coords = (location.latitude, location.longitude)
                distance = geodesic(zip_coords, address_coords).miles
                if distance <= radius_mi:
                    list.append(address)  # Found an address outside the radius
            
        except Exception as e:
            print(f"Error getting location for {address}: {e}")
              # Error occurred during geocoding
    
    return list  # All addresses are within the radius from the ZIP code

def location(doctor):
    # Geolocation of the doctor's address using Bing Maps API
    geolocator = Bing(api_key="AiD2FXje7LL88RhGVmH1mhdAr1-LQC2aApNC1oPG3Psnj_4NStiayQh_Vuct1moh")

    my_map = folium.Map()  # Initialize the map outside the loop

    for i in doctor:
        try:
            # Modify the address format to include city, state, postal code
            address = f"{i['address']}, USA"
            location = geolocator.geocode(address)
            
            if location is not None:
                lat = location.latitude
                lon = location.longitude
                # Add a marker for each doctor's location
                folium.Marker([lat, lon], popup="Doctor").add_to(my_map)
        except Exception as e:
            st.write(f"Error getting location for {i['address']}: {e}")
    if my_map:
        # Fit the map to the bounds of the markers
        my_map.fit_bounds(my_map.get_bounds())
    
    return my_map
   
   