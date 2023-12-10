import streamlit as st

st.title("About Us")

# Introduction
st.header("Welcome to Our Company")
st.write("""
We are a dynamic team passionate about technology and innovation. Our mission is to create solutions 
that make a difference in people's lives. With a focus on collaboration and excellence, we strive to 
deliver high-quality products and services to our customers.
""")

# Team Members
st.header("Our Team")
st.write("""
Meet our talented team of individuals dedicated to our company's success. 
Here are some of the key members:
""")

# Displaying team members' information
team_members = [
    {"name": "John Doe", "role": "CEO"},
    {"name": "Jane Smith", "role": "CTO"},
    {"name": "Alice Johnson", "role": "Lead Developer"},
    # Add more team members here
]

for member in team_members:
    st.write(f"- **{member['name']}**: {member['role']}")

# Contact Information
st.header("Contact Us")
st.write("""
We're always happy to hear from you! Feel free to reach out to us:
- **Email**: contact@company.com
- **Phone**: +1 123-456-7890
""")