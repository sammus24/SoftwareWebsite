import streamlit as st

st.markdown("<h1 style='text-align: center; color: Black;text-decoration:underline; font-face: KODCHASAN;'>Testimonials</h1>", unsafe_allow_html=True)

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
st.write("")
st.write("")
st.write("")

col1, col2 ,col3,col4,col5, col6 ,col7= st.columns(7)

with col1:
    st.image('Photos/T1.png')
    st.image('Photos/stars.png')
    st.markdown("<div style='text-align:Center;font-size: 20px; font-weight: bold; font-face:KADWA ;'>'Easy to find a provider!'</div>", unsafe_allow_html=True)
    
    

with col3:
    st.image('Photos/T2.png')
    st.image('Photos/stars.png')
    st.markdown("<div style='text-align:Center;font-size: 20px; font-weight: bold; font-face:kadwa ;'>'Found great providers for my family!'</div>", unsafe_allow_html=True)
    
    
    
with col5:
    st.image('Photos/T3.png')
    st.image('Photos/stars.png')
    st.markdown("<div style='text-align:Center;font-size: 20px; font-weight: bold; font-face:kadwa ;'>'10/10 recommend!'</div>", unsafe_allow_html=True)
    
    
    
with col7:
    st.image('Photos/T4.png')
    st.image('Photos/stars.png')
    st.markdown("<div style='text-align:Center;font-size: 20px; font-weight: bold; font-face:kadwa ;'>'So glad I became part of the hive!'</div>", unsafe_allow_html=True)
st.session_state.page = 'main'    
    