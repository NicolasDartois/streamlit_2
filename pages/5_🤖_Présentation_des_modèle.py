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

st.markdown(f"""
        <div class ="centered-content">
            <div class="wrapper">
                <div class="box">
                    <label for="1" style="cursor: pointer;"><h4>{df_modele['modèle'][0]}</h4></label>
                    <input type="checkbox" id="1" class="hidden-checkbox">
                    <p id="H1" class="hiddenText"><br>R2 : {df_modele['r2'][0]}<br>MAE : {df_modele['MAE'][0]}</p>
                </div><div class="box">
                    <label for="2" style="cursor: pointer;"><h4>{df_modele['modèle'][0]}</h4></label>
                    <input type="checkbox" id="2" class="hidden-checkbox">
                    <p id="H2" class="hiddenText"><br>R2 : {df_modele['r2'][0]}<br>MAE : {df_modele['MAE'][0]}</p>
                </div><div class="box">
                    <label for="3" style="cursor: pointer;"><h4>{df_modele['modèle'][0]}</h4></label>
                    <input type="checkbox" id="3" class="hidden-checkbox">
                    <p id="H3" class="hiddenText"><br>R2 : {df_modele['r2'][0]}<br>MAE : {df_modele['MAE'][0]}</p>
                </div><div class="box">
                    <label for="4" style="cursor: pointer;"><h4>{df_modele['modèle'][0]}</h4></label>
                    <input type="checkbox" id="4" class="hidden-checkbox">
                    <p id="H4" class="hiddenText"><br>R2 : {df_modele['r2'][0]}<br>MAE : {df_modele['MAE'][0]}</p>
                </div><div class="box">
                    <label for="5" style="cursor: pointer;"><h4>{df_modele['modèle'][0]}</h4></label>
                    <input type="checkbox" id="5" class="hidden-checkbox">
                    <p id="H5" class="hiddenText"><br>R2 : {df_modele['r2'][0]}<br>MAE : {df_modele['MAE'][0]}</p>
                </div>
            </div>
        </div>
""", unsafe_allow_html=True)








    
