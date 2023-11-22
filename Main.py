import streamlit as st
from Nav import Navigation

def main_page():
    st.title("Main Page")
    if st.button('Navigate'):
        st.session_state.page = 'navigation'
        st.session_state.rerun_flag = True  # Set a flag to indicate rerun

def clear_page():
    if st.session_state.get('rerun_flag'):
        st.session_state.rerun_flag = False  # Reset the flag to prevent further reruns
        st.experimental_rerun()

# Initialize session_state variables
if 'page' not in st.session_state:
    st.session_state.page = 'main'
    
if st.session_state.page == 'main':
    main_page()

# Render pages based on session_state
if st.session_state.page == 'navigation':
    clear_page()
    Navigation()
