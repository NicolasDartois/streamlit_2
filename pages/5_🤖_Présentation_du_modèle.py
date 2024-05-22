import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

for i in range(25):
    st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.subheader("🎥oct23_cda_exploitation-cinématographique🎥")
st.sidebar.markdown("_____________________")
st.sidebar.markdown("Manon FOUQUET")
st.sidebar.markdown("Sylvain BRAIZET")
st.sidebar.markdown("Nicolas DARTOIS")

st.header("🤖Présentation du modèle🤖")

background_image = '''
    <style>
    #hiddenText {
        display: none;
    }
    #toggleCheckbox:checked + #hiddenText {
        display: block;
    }
    .hidden-checkbox {
        display: none;
    }
    .stApp {
        background-color: white;
        background-image: url("https://github.com/NicolasDartois/streamlit_2/blob/main/images/background.jpg?raw=true");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }
    .box {
        background-color: white;
        padding: 20px;
        margin-top: 20px;
        margin-bottom: 20px;
        box-shadow: 0 10px 12px rgba(0, 0, 0, 0.1);
        border-radius: 10px;
        text-align: justify;
    }
    .fit-img {
    width: 100%;
    height: 100%;
    object-fit: cover; /* Peut aussi être 'contain' selon le besoin */
    display: block;
    }
    </style>
    '''
st.markdown(background_image, unsafe_allow_html=True)

df_modele = pd.read_csv('data/score.csv')

for modèle, r2, MAE in zip(df_modele['modèle'], df_modele['r2'], df_modele['MAE']):
    st.markdown(f"""
        <div class="box"> 
        <label for="toggleCheckbox" style="cursor: pointer;">{modèle}</label>
        <input type="checkbox" id="toggleCheckbox" class="hidden-checkbox">
        <p id="hiddenText">R2 : {r2}<br>MAE : {MAE}</p>
        </div>
    """, unsafe_allow_html=True)







    
