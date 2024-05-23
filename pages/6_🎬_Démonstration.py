import streamlit as st
import joblib as jl
import pandas as pd
from include.css_and_credit import css_and_credit

css_and_credit()

st.header("🎬Démonstration🎬")

model = jl.load("models/GB.joblib")

df_acteur = pd.read_csv('data/score_acteur.csv')
df_real = pd.read_csv('data/score_real.csv')
df_scenar = pd.read_csv('data/score_scenar.csv')

acteur1 = st.selectbox('Choisir l\'acteur principal :', df_acteur['Acteur'])
score_acteur1 = df_acteur[df_acteur['Acteur'] == acteur1]['Score'].values[0]

acteur2 = st.selectbox('Choisir l\'acteur secondaire :', df_acteur['Acteur'])
score_acteur2 = df_acteur[df_acteur['Acteur'] == acteur2]['Score'].values[0]

score_acteur = (score_acteur1*1.125)+(score_acteur2*0.75)

real = st.selectbox('Choisir le réalisateur :', df_real['realisateur'])
score_real = df_real[df_real['realisateur'] == real]['score'].values[0]

scenar = st.selectbox('Choisir le scénariste :', df_scenar['scenariste'])
score_scenar = df_scenar[df_scenar['scenariste'] == scenar]['score'].values[0]

date_sortie = st.date_input('Choisir la date de sortie', min_value=date(2000, 1, 1), max_value=datedate(2024, 1, 1))


st.write(score_acteur)
st.write(score_real)
st.write(score_scenar)
st.write(date_sortie)




