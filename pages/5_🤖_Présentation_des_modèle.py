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

st.header("🤖Présentation des modèles🤖")

background_image = '''
    <style>
    .hidden-checkbox {
        display: none;
    }
    .hiddenText {
        display: none;
    }
    .hidden-checkbox:checked + .hiddenText {
        display: block;
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

st.markdown("""
<div class="box"><h3>Choix du type de modèle :</h3>
    <p>Le choix d'utiliser un modèle de régression plutôt qu'un modèle de classification dans notre projet de prédiction du nombre d'entrées en première semaine en France repose sur la nature continue et quantitative de notre variable cibl</p>
    <p>En effet, le nombre d'entrées en première semaine est une mesure numérique qui peut prendre une gamme de valeurs continues, reflétant la performance d'un film dans les salles de cinéma. Ainsi, plutôt que de catégoriser les films en groupes prédéfinis, notre objectif est de prédire avec précision le nombre réel d'entrées qu'un film réalisera.</p>
    <p>Nous avons donc décidé de tester notre jeu de données sur plusieurs modèles différents :</p>
</div>
""", unsafe_allow_html=True)

df_modele = pd.read_csv('data/score.csv')

for idx, (modèle, r2, MAE) in enumerate(zip(df_modele['modèle'], df_modele['r2'], df_modele['MAE'])):
    unique_id = f"toggleCheckbox_{idx}"
    hidden_text_id = f"hiddenText_{idx}"
    
    st.markdown(f"""
        <div class="box">
            <label for="{unique_id}" style="cursor: pointer;"><h4>{modèle}</h4></label>
            <input type="checkbox" id="{unique_id}" class="hidden-checkbox">
            <p id="{hidden_text_id}" class="hiddenText"><br>R2 : {r2}<br>MAE : {MAE}</p>
        </div>
    """, unsafe_allow_html=True)







    
