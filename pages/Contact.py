import streamlit as st

st.markdown("<h1 style='text-align: center; color: Black;text-decoration:underline'>Contact Page</h1>", unsafe_allow_html=True)

page_bg_img = '''
        <style>
        .main {
        background: url("https://sa1s3optim.patientpop.com/1280x/filters:format(webp)/assets/production/practices/fc3fcb2fd0732ffac2aec3238492f240f15ea6d1/images/2614581.png") no-repeat center center/cover;
        };
        </style>
        '''
        
st.markdown(page_bg_img, unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")


top_col1, top_col2 ,col2,col4,col5,col6,col7= st.columns(7)

with top_col2:
    st.image('Photos/headphones.png')
    st.markdown("<div style='text-align:Center;font-size: 35px; font-weight: bold;'>24hr Chat</div>", unsafe_allow_html=True)
    
with col4:
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
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.image('Photos/@symbol.png', use_column_width=True)
    st.markdown("<div style='text-align:Center;font-size: 35px; font-weight: bold;'>HHProviders@yahoo.com</div>", unsafe_allow_html=True)
    
    

with col6:
    st.image('Photos/phone2.png')
    st.markdown("<div style='text-align:Left;font-size: 35px; font-weight: bold;'>1-800HIVE</div>", unsafe_allow_html=True)
st.session_state.page = 'main'    
