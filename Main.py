import streamlit as st
from Nav import Navigation
import base64

st.set_page_config(layout="wide")


def main_page():
    st.image("Photos/Header.png")
    st.image("Photos/main.jpg")
        
            
    col1, col2 = st.columns(2)
   
    
    with col1:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        
        st.image('Photos/paragraph.png')
    with col2:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
       

        # Load your image here
        st.image("Photos/button.png")  # Replace with your image path
        col1 ,col2 = st.columns(2)

        
        with col2:
            if st.button('Navigate'):
                st.session_state.page = 'navigation'
                st.session_state.rerun_flag = True  # Set a flag to indicate rerun           


def clear_page():
    if st.session_state.get('rerun_flag'):
        st.session_state.rerun_flag = False  # Reset the flag to prevent further reruns
        st.rerun()


def main():
    # Initialize session_state variables
    if 'page' not in st.session_state:
        st.session_state.page = 'main'

    if st.session_state.page == 'main':
        # Render your main_page function here
        clear_page()
        main_page()

    if st.session_state.page == 'navigation':
        # Render Navigation function here
        clear_page()
        Navigation()
        if st.button('Back'):
            st.session_state.page = 'main'
            st.session_state.rerun_flag = True  # Set a flag to indicate rerun
            st.rerun()


# Call the main function to start the app
if __name__ == '__main__':
    main()
