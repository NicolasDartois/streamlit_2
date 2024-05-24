import streamlit as st
import pandas as pd
from include.css_and_credit import css_and_credit
st.set_page_config(page_title="Exploitation cinématographique", page_icon='🎬', layout="wide")

css_and_credit()

st.header("🤖Présentation des modèles🤖")

st.markdown("""
<div class ="centered-content"><div class="box"><h3>Choix du type de modèle :</h3>
    <p>Le choix d'utiliser un modèle de régression plutôt qu'un modèle de classification dans notre projet de prédiction du nombre d'entrées en première semaine en France repose sur la nature continue et quantitative de notre variable cible.</p>
    <p>En effet, le nombre d'entrées en première semaine est une mesure numérique qui peut prendre une gamme de valeurs continues, reflétant la performance d'un film dans les salles de cinéma. Ainsi, plutôt que de catégoriser les films en groupes prédéfinis, notre objectif est de prédire avec précision le nombre réel d'entrées qu'un film réalisera.</p>
    <p>Nous avons donc décidé de tester notre jeu de données sur plusieurs modèles différents :</p>
</div></div>
""", unsafe_allow_html=True)

df_modele = pd.read_csv('data/score.csv')

i = 1
cols = st.columns(5)
for idx, (modèle, r2, MAE) in enumerate(zip(df_modele['modèle'], df_modele['r2'], df_modele['MAE'])):
    unique_id = f"toggleCheckbox_{idx}"
    hidden_text_id = f"hiddenText_{idx}"
    with cols[(i-1) % 5]: 
        st.markdown(f"""
            <div class ="centered-content"><div class="box">
                <label for="{unique_id}" style="cursor: pointer;"><h4>{modèle}</h4></label>
                <input type="checkbox" id="{unique_id}" class="hidden-checkbox">
                <p id="{hidden_text_id}" class="hiddenText"><br>R2 : {r2}<br>MAE : {MAE}</p>
            </div></div>
        """, unsafe_allow_html=True)
    i += 1







    
