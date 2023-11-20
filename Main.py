import streamlit as st
from Nav import Navigation

st.write(st.session_state)
st.title("Main Page")
if st.button('Navigate'):
    st.session_state.page = 'navigation'

# Initialize session_state variables
if 'page' not in st.session_state:
    st.session_state.page = 'main'


# Render pages based on session_stat
if st.session_state.page == 'navigation':
    Navigation()
    st.write(st.session_state)
