import streamlit as st
from streamlit_folium import folium_static

from map import location
from application import application_function
from API import search_healthcare_providers,specific_provider
from print import generate_pdf


def provider_page(provider ,code):
    
    
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("Results")
        info = specific_provider(provider, code)
        if info:
            for i in info:
                st.write(i['org_name'])
                st.write(i['telephone_number'])
                st.write(i['taxonomy_description']) 
                st.button(f"Apply Here",on_click= app_page)
                
            with right_column:
                map = location(info)
                if map:
                    st.write("Map exists.")
                    folium_static(map)
                else:
                    st.write("No vaild location found.")
                    
        else:
            st.write("There no provider by that name")
            
        
        
   
def display_search_results(zip_code, provider, sort_option, radius):
   
      
    doc = search_healthcare_providers(zip_code, provider, radius)
    

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
    
    with left_column:
         # Show the first five doctors
        if doc:
            num=1
            for i in doc:
                num +=1
                display_doctor_info(i,num)
              
            with right_column:
                #map = location(doc)
                #if map:
                    #st.write("Map exists.")
                    #folium_static(map)
                #else:
                    #st.write("No vaild location found.")
                
                pdf = generate_pdf(doc)
                
                st.download_button(
                        label='Download Results',
                        data=pdf,
                        file_name='Doctor_results.pdf'
                        )

                

        else:
            st.write("No results found.")

def display_doctor_info(doctor_info,num):
    st.write("Organization Name:", doctor_info['organization'])
    st.write("Address: ", doctor_info['address'])
    st.write("Phone Number: ", doctor_info['phone'])
    number = doctor_info['NPI']
    st.button(f"Apply Here",key = num,on_click= app_page)
    

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
            "Gynecology", "Internal Medicine", "Pharmacist","Physical Therapist", "Radiology", "Dermatology", "Plastic Surgery",
            "Psychiatrist", "Counselor", "Surgery"))
        sort_option = st.selectbox("Sort Results By:", ["Name A-Z",'Name Z-A', "Address"])
        # clear the search box

        if st.button("Search",key = 'multiple'):
            # Check if the entered ZIP code is valid
            if provider == 'Blank':
                st.write("Please select a provider")
            else:
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
                provider_page(provider, code)
            else:
                st.warning('Please Enter a Valid 5-digit ZIP Code')
            
       
def is_valid_zip(zip_code):
    # Check if the ZIP code meets the required conditions for validity (you may need a more robust check)
    return len(zip_code) == 5 and zip_code.isdigit()