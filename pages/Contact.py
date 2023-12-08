import streamlit as st

# Embedding the CSS directly into the Streamlit app
page_background = """
<style>
[data-testid = "stAppViewContainer"] {
    background-image: url('Photos/Behive.png');
    background-size: cover;
            
}
</style>
"""
st.markdown(page_background,unsafe_allow_html=True)
st.title("Contact page")
  