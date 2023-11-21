import streamlit as st
import random

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

        # Text input for last 4 digits of SSN
        ssn_last_4 = st.text_input("Enter the last 4 digits of SSN", type="password")
        
        # Text area for message
        message = st.text_area("Enter the reason for an Appointment")
        
        # Checkbox for agreeing to terms
        agree = st.checkbox("I agree to the terms and conditions.")

        # Button to submit the form
        if st.form_submit_button("Submit", on_click = application_function):
            # Check if all fields are filled
            if full_name and email and phone_number and address and ssn_last_4 and message and agree:
                # Process the form data (you can add your own processing logic here)
                st.success(f"Form submitted successfully!")

                # Write form data to a file
                with open('Form.txt', 'w') as file:
                    file.write(f"Doctor's NPI: {doctor_npi}\nFull Name: {full_name}\nEmail: {email}\nPhone Number: {phone_number}\nAddress: {address}\nLast 4 digits of SSN: {ssn_last_4}\nMessage: {message}\nAgreed to terms: {agree}")
            else:
                st.warning("Please fill out all fields and agree to the terms.")

