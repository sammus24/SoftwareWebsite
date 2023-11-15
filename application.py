import streamlit as st

def application_function():

    st.title("Simple Form Example")


        # Text input for name
    name = st.text_input("Enter your name")

        # Text input for email
    email = st.text_input("Enter your email")

        # Text area for message
    message = st.text_area("Enter your message")

        # Checkbox for agreeing to terms
    agree = st.checkbox("I agree to the terms and conditions")

        # Button to submit the form
    if st.button("Submit"):
            # Check if all fields are filled
        if name and email and message and agree:
            # Process the form data (you can add your own processing logic here)
            st.success(f"Form submitted successfully!\nName: {name}\nEmail: {email}\nMessage: {message}")
        else:
            st.warning("Please fill out all fields and agree to the terms.")