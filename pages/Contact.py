import streamlit as st

# Embedding the CSS directly into the Streamlit app
page_background = '''
<style>
[data-testid = "stAppViewContainer"] {
    background-image: url('Photos/Behive.png');
    background-size: cover;
            
}
</style>
'''

st.title("Contact page")
st.write("")
st.write("")

top_col1, top_col2 ,col2,col4= st.columns(4)

with top_col1:
    st.image('Photos/headphones.png', use_column_width=True)
    st.header("24hr Chat")

with col4:
    st.image('Photos/phone.png', use_column_width=True)
    st.header("1-800-HIVE")
    st.markdown("<div style='text-align: left;font-size: 35px; font-weight: bold;'>HHProviders@yahoo.com</div>", unsafe_allow_html=True)


st.write("")  # Adding space between top images and email symbol

center_col = st.columns(5)

with center_col[0]:
    pass  # This empty column will help center the email symbol

with center_col[2]:
    st.image('Photos/@symbol.png', use_column_width=True)
    st.markdown("<div style='text-align: left;font-size: 35px; font-weight: bold;'>HHProviders@yahoo.com</div>", unsafe_allow_html=True)

with center_col[3]:
    pass  # Another empty column for centering

