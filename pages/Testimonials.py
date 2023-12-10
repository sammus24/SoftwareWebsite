import streamlit as st

st.markdown("<h1 style='text-align: center; color: Black;text-decoration:underline font-face: KODCHASAN;'>Testimonials</h1>", unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

col1, col2 ,col3,col4= st.columns(4)

with col1:
    st.image('Photos/T1.png')
    st.image('Photos/stars.png')
    st.markdown("<div style='text-align:Center;font-size: 20px; font-weight: bold; font-face:KADWA ;'>'Easy to find a provider!'</div>", unsafe_allow_html=True)
    
    

with col2:
    st.image('Photos/T2.png')
    st.image('Photos/stars.png')
    st.markdown("<div style='text-align:Center;font-size: 20px; font-weight: bold; font-face:kadwa ;'>'Found great providers for my family!'</div>", unsafe_allow_html=True)
    
    
    
with col3:
    st.image('Photos/T3.png')
    st.image('Photos/stars.png')
    st.markdown("<div style='text-align:Center;font-size: 20px; font-weight: bold; font-face:kadwa ;'>'10/10 recommend!'</div>", unsafe_allow_html=True)
    
    
    
with col4:
    st.image('Photos/T4.png')
    st.image('Photos/stars.png')
    st.markdown("<div style='text-align:Center;font-size: 20px; font-weight: bold; font-face:kadwa ;'>'So glad I became part of the hive!'</div>", unsafe_allow_html=True)
    
    