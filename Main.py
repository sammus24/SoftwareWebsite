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
        st.rerun()



def main():
    # Initialize session_state variables
    if 'page' not in st.session_state:
        st.session_state.page = 'main'

    if st.session_state.page == 'main':
        # Render your main_page function here
        main_page()
    
    if st.session_state.page == 'navigation':
        # Render Navigation function here
        clear_page()
        Navigation()
 
# Call the main function to start the app
if __name__ == '__main__':
    main()
