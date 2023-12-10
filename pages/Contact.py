import streamlit as st

# Embedding the CSS directly into the Streamlit app
page_background = '''
<style>
[data-testid="stAppContainer"]  {
    background-image: url('Photos/Behive.png');
    background-size: cover;
            
}
</style>
'''
st.markdown(page_background,unsafe_allow_html=True )
st.markdown("<h1 style='text-align: center; color: Black;text-decoration:underline'>Contact Page</h1>", unsafe_allow_html=True)



st.write("")
st.write("")
st.write("")


top_col1, top_col2 ,col2,col4= st.columns(4)

with top_col1:
    st.image('Photos/headphones.png')
    st.markdown("<div style='text-align:Center;font-size: 35px; font-weight: bold;'>24hr Chat</div>", unsafe_allow_html=True)

with col4:
    st.image('Photos/phone2.png')
    st.markdown("<div style='text-align:Center;font-size: 35px; font-weight: bold;'>1-800HIVE</div>", unsafe_allow_html=True)


st.write("")  # Adding space between top images and email symbol

center_col = st.columns(5)

with center_col[0]:
    pass  # This empty column will help center the email symbol

with center_col[1]:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.markdown("<div style='text-align:Right;font-size: 35px; font-weight: bold;'>HHProviders@yahoo.com</div>", unsafe_allow_html=True)


with center_col[2]:
    st.image('Photos/@symbol.png', use_column_width=True)
    
with center_col[3]:
    pass  # Another empty column for centering

