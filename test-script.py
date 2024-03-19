import streamlit as st


with open("document.txt") as file:
    for line in file:

        st.markdown(line)