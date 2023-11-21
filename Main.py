import streamlit as st
from Nav import Navigation

def main_page():
    st.title("Main Page")
    if st.button('Navigate'):
        st.session_state.page = 'navigation'

# Initialize session_state variables
if 'page' not in st.session_state:
    st.session_state.page = 'main'
    
if st.session_state.page == 'main':
    main_page()

# Render pages based on session_stat
if st.session_state.page == 'navigation':
    Navigation()
    
