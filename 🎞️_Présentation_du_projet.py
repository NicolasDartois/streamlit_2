import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Projet Ciné", layout="wide") 

st.title("L'IA au service de la production cinématographique !")

with open('include/carousel.html', 'r', encoding='utf-8') as f:
    carousel_html = f.read()
    
components.html(carousel_html, height=600, width=800)
