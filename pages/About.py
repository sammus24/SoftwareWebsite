import streamlit as st

st.markdown("<h1 style='text-align: center;'><u>About Us</u></h1>", unsafe_allow_html=True)

# Introduction
st.header("Welcome to Our Company")
st.write("""
We are a dynamic group of individuals who are enthusiastic about technology and innovation. 
         Our objective is to provide solutions that improve people's lives. 
         We aspire to provide high-quality products and services to our customers by focusing on collaboration and excellence.
""")

# Displaying images with adjusted width to make them side by side
col1, col2 = st.columns(2)

with col1:
   
    st.image("Photos/about1.jpg", width=350)

with col2:
    
    st.image("Photos/about2.png", width=376)

left_column, right_column = st.columns(2)

with left_column: 
    st.header("Our Team")
    
    # First three team members
    team_members_left = [
        {"name": "Allison Okomski", "role": "Project manager with experience in the recruiting industry. She has a degree in C.S and is skilled in planning, managing budgets, producing reports, and ensuring projects are on schedule."},
        {"name": "Shiv Malli", "role": "Back-end developer with over 3 years of experience in developing websites with Python. He is skilled in HTML, CSS, and PHP. Shiv is responsible, creative, open-minded, friendly, and an ambitious developer."},
        {"name": "Sal Hasan", "role": "UX/UI and holds B.A in C.S. He is responsible for the layout of the website and appearance. He is the CEO of UX incorporated."},
    ]
    
    # Displaying first three team members' information
    for member in team_members_left:
        st.write(f"- **{member['name']}**: {member['role']}")

with right_column:
   
    st.write("")
    st.write("")
    
    # Last three team members
    team_members_right = [
        {"name": "Mikail Mahmood", "role": "Business Analyst. He holds a B.S. in C.S and contributor to multiple projects and specializes in Python and p5js, as well as quantitative and qualitative analyses."},
        {"name": "Sammu Suryanarayanan", "role": "Full-stack developer with over 3 years of experience in development. Sammu is skilled in Python, Java, and C. She is dependable, a creative problem solver, and an analytical thinker."},
        {"name": "Toni Marie", "role": "Quality assurance analyst. Toni is a responsible, creative, and a hard-working individual that is passionate about quality and success."},
    ]
    
    # Displaying last three team members' information
    for member in team_members_right:
        st.write(f"- **{member['name']}**: {member['role']}")