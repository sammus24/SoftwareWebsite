import streamlit as st
import random
import re

def generate_random_npi():
    # Generate a random 10-digit NPI number
    npi = ''.join([str(random.randint(0, 9)) for _ in range(10)])
    return npi

def application_function():
    with st.form("application"):
        st.title("Doctor's Information Form")
        
        # Generate a random NPI for the doctor
        doctor_npi = generate_random_npi()

        # Display the generated NPI
        st.write(f"Doctor's NPI ID: {doctor_npi}")

        # Text input for full name
        full_name = st.text_input("Enter full name")

        # Text input for email
        email = st.text_input("Enter the email")

        # Text input for phone number
        phone_number = st.text_input("Enter phone number")

        # Text input for address
        address = st.text_input("Enter the address")
        
        # Text area for message
        message = st.text_area("Enter the reason for an Appointment")
        
        # Checkbox for agreeing to terms
        agree = st.checkbox("I agree to the terms and conditions.")

        # Button to submit the form
        if st.form_submit_button("Submit", on_click= application_function):
            if verify_email(email):
           
                if full_name and email and phone_number and address and message and agree:
                    # Process the form data (you can add your own processing logic here)
                    st.success(f"Form submitted successfully!")

                    # Write form data to a file
                    with open('Form.txt', 'w') as file:
                        file.write(f"Doctor's NPI: {doctor_npi}\nFull Name: {full_name}\nEmail: {email}\nPhone Number: {phone_number}\nAddress: {address}\nMessage: {message}\nAgreed to terms: {agree}")
                    
                    st.session_state.page = 'navigation' 
                    st.rerun()  # Rerun the app to show the search page 
                else:
                    st.warning("Please fill out all fields and agree to the terms.")
            else:
                st.warning("Please Enter Valid Email")
                



def verify_email(email):
    # Regular expression pattern for basic email validation
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    if re.match(pattern, email):
        return True  # Email matches the pattern
    else:
        return False  # Email does not match the pattern