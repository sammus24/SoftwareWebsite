import streamlit as st


def application_function():
    with st.form("application"):
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
        if st.form_submit_button("Submit", on_click=application_function):
           
            
            # Check if all fields are filled
            if name and email and message and agree:
                # Process the form data (you can add your own processing logic here)
                st.success(f"Form submitted successfully!")

                # Write form data to a file
                with open('Form.txt', 'w') as file:
                    file.write(f"Name: {name}\nEmail: {email}\nMessage: {message}\nAgreed to terms: {agree}")
            else:
                st.warning("Please fill out all fields and agree to the terms.")

