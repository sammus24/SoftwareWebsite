import streamlit as st
from Nav import Navigation
import base64

st.set_page_config(layout="wide")

def on_image_click():
    st.session_state.page = 'navigation'
    
def main_page():
    with st.container():
        st.image("Photos/Header.png")
        
            
    col1, col2 = st.columns(2)
    
    
    
    with col1:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
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
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")

        # Load your image here
        image_path = "Photos/button.png"  # Replace with your image path

        # Read the image file as bytes
        with open(image_path, "rb") as img_file:
            img_bytes = img_file.read()

        # Encode the image in base64
        encoded_img = base64.b64encode(img_bytes).decode()

        # Create an HTML link with the image and call the function on click
        html = f'<a href="javascript:void(0)" onclick="clickHandler()"><img src="data:image/png;base64,{encoded_img}" /></a>'
        js_script = """
        <script>
        function clickHandler() {
            streamlitComponentDispatcher("image-clicked")
        }
        </script>
        """
        st.markdown(html + js_script, unsafe_allow_html=True)
        
        page_bg_img = '''
        <style>
        .main {
        background: url("https://sa1s3optim.patientpop.com/1280x/filters:format(webp)/assets/production/practices/fc3fcb2fd0732ffac2aec3238492f240f15ea6d1/images/2614581.png") no-repeat center center/cover;
        };
        </style>
        '''
        
        st.markdown(page_bg_img, unsafe_allow_html=True)

        # Listen for the click event
        if st.session_state.get('navigation'):
            on_image_click()
        
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
