import streamlit as st
import base64
from Nav import Navigation

def main_page():
    st.markdown(        
    "<h1 style='text-align: Center; color: #FFD361;font-face: kodchasan; margin-botton: 0;'>Hive Health</h1>"
    "<h1 style='text-align: Center; color:black ;font-face: kodchasan; padding-top: 0;'>Providers</h1>",
    unsafe_allow_html=True)
    st.image('Photos/Mainpage.jpg')
    
    col1,col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(        
        "<h2 style='text-align: Center; color: #FFD361;font-face: kodchasan; margin-botton: 0;'>Join the Hive today!</h2>"
        "<p style=' color:black ;font-face: kadwa; padding-top: 0;'>Hive Health Providers specializes in finding the perfect Health Care professionals for you and your loved ones -- With our tailored primary care, you can focus on staying healthy and doing the things you love.</p>",
        unsafe_allow_html=True)
   
    with col3:
        # Replace this with your image loading logic
        with open("Photos/arrow.png", "rb") as img_file:
            arrow_bytes = img_file.read()
            arrow = base64.b64encode(arrow_bytes).decode()

        # Display the image
        st.image(arrow_bytes)

        # Add a separate text element for navigation
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
