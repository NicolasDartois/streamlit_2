import streamlit as st
import os
import importlib.util

def load_module(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

pages_dir = os.path.join(os.path.dirname(__file__), 'pages')

pages={
    "page1" : "Présentation du projet",
    "page2" : "Collecte et Exploration des Données",
    "page3" : "Analyse des Données (DataViz)",
    "page4" : "Préparation les données - Preprocessing",
    "page5" : "Présentation du modèle",
    "page6" : "DEMONSTRATION"
    }

page_modules = {}
for i, j in pages.items():
    module = load_module(i, os.path.join(pages_dir, f'{i}.py'))
    page_modules[j] = module
    st.write(page_modules)


st.set_page_config(page_title="Projet Ciné", layout="centered") 

st.title("L'IA au service de la production cinématographique !")
