import streamlit as st

from Nav import search

def main():
    st.title("Home Page")

    result = st.empty()

    if st.button("Naviagate"):
        result.empty()
        
        search()

if __name__ == "__main__":
    main()