import streamlit.components.v1 as components
import streamlit as st

with open('include/carousel.html', 'r', encoding='utf-8') as f:
    carousel_html = f.read()
    
def page1():
    components.html(carousel_html, height=600, width=800)
