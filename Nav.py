import streamlit as st
from streamlit_folium import folium_static

from map import location,are_within_radius
from application import application_function
from API import search_healthcare_providers,specific_provider
from print import generate_pdf

def provider_page(provider ,code):
    st.title("Provider Page")
    infos = specific_provider(provider, code)
    if infos:
        st.write('Name: ',infos["name"])
    
def display_search_results(zip_code, provider, sort_option, radius):

   
    doctors = search_healthcare_providers(zip_code, provider, radius)
    doc = are_within_radius(zip_code,doctors,radius)

    # Sort the doctors based on the selected sorting option
    if sort_option == "Name  A-Z":
        doc.sort(key=lambda doctor: (doctor["organization"]))
    elif sort_option == "Name Z-A":
        doc.sort(key=lambda doctor: (doctor["organization"]),reverse= True)
    elif sort_option == "Address":
        doc.sort(key=lambda doctor: doctor["address"])

    st.title("Search Results")

    # Create a two-column layout
    left_column, right_column = st.columns(2)
    
    

    if doc:
        count = st.session_state.get("count", 5)
        key = st.session_state.get("key", 1)
        with left_column:
            for i in doc[:count]:
                st.write("Organization Name:", i['organization'])
                st.write("Address: ", i['address'])
                st.write("Phone Number: ",i['phone'])
                number = i['NPI']
                st.button(f"Apply Here",key = number,on_click= app_page)
                  
                    
            if (len(doc)> count):
                load = st.button("Load more", key = key)
                if load:
                    st.session_state.count += 5
                    st.session_state.key += 1
                    st.session_state.page = 'load'
                    for i in doc[count:count+5]:
                        st.write("Organization Name:", i['organization'])
                        st.write("Address: ", i['address'])
                        st.write("Phone Number: ",i['phone'])
                        number = i['NPI']
                        st.button(f"Apply Here",key = number,on_click= app_page)
                            
    
                
            
                           
            with right_column:
                #map = location(doc)
                #if map:
                    #st.write("Map exists.")
                    #folium_static(map)
                #else:
                    #st.write("No vaild location found.")
                
                pdf = generate_pdf(doctors)
            
                st.download_button(
                    label='Download Results',
                    data=pdf,
                    file_name='Doctor_results.pdf'
                )
                

    else:
        st.write("No results found.")

def app_page():
    st.session_state.page = "apply"
    st.session_state.rerun_flag = True
    
    application_function()

    
def Navigation():
    
    tab1, tab2 =st.tabs(['Provider search', 'Health Credit provider'])
    
    with tab1:
        st.title("Health Care Provider search")
        zip_code = st.text_input("Enter ZIP code:")

        radius = st.text_input("Enter Radius (Default Radius = 5 miles): ")
        if not radius:
            radius = 5  # Set default radius to 5 if not provided
        else:
            radius = int(radius)
        provider = st.selectbox(
            "Select Provider Type:",
            ("Blank", "Dentist", "Optometrist", "Pediatrician", "Physician",
            "Gynecology", "Internal Medicine", "Pharmacist", "Radiology", "Dermatology", "Plastic Surgery",
            "Psychiatrist", "Counselor", "Surgery"))
        sort_option = st.selectbox("Sort Results By:", ["Name A-Z",'Name Z-A', "Address"])
        # clear the search box

        if st.button("Search",key = 'multiple'):
            # Check if the entered ZIP code is valid
            if is_valid_zip(zip_code):
                display_search_results(zip_code, provider, sort_option, radius)
            else:
                st.warning('Please Enter a Valid 5-digit ZIP Code')
    with tab2:
        st.title("Find out if your Doctor is a Health Credit provider")
        code = st.text_input("ZIP code:")
        provider = st.text_input("Enter Provider Name: ")
        
        if st.button ("Search", key = 'spcific'):
            if is_valid_zip(code):
                provider_page(code, provider)
            else:
                st.warning('Please Enter a Valid 5-digit ZIP Code')
            
       
def is_valid_zip(zip_code):
    # Check if the ZIP code meets the required conditions for validity (you may need a more robust check)
    return len(zip_code) == 5 and zip_code.isdigit()