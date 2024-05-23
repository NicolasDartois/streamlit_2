import streamlit as st
import joblib as jl
import pandas as pd
from include.css_and_credit import css_and_credit
from datetime import date

css_and_credit()

st.header("🎬Démonstration🎬")

model = jl.load("models/GB.joblib")

df_acteur = pd.read_csv('data/score_acteur.csv')
df_real = pd.read_csv('data/score_real.csv')
df_scenar = pd.read_csv('data/score_scenar.csv')
df_distrib = pd.read_csv('data/score_distrib.csv')

acteur1 = st.selectbox('Choisir l\'acteur principal :', df_acteur['Acteur'])
score_acteur1 = df_acteur[df_acteur['Acteur'] == acteur1]['Score'].values[0]

acteur2 = st.selectbox('Choisir l\'acteur secondaire :', df_acteur['Acteur'])
score_acteur2 = df_acteur[df_acteur['Acteur'] == acteur2]['Score'].values[0]

score_acteur = (score_acteur1*1.125)+(score_acteur2*0.75)

real = st.selectbox('Choisir le réalisateur :', df_real['realisateur'])
score_real = df_real[df_real['realisateur'] == real]['score'].values[0]

scenar = st.selectbox('Choisir le scénariste :', df_scenar['scenariste'])
score_scenar = df_scenar[df_scenar['scenariste'] == scenar]['score'].values[0]

distrib = st.selectbox('Choisir le distributeur :', df_distrib['distributeur'])
score_scenar = df_distrib[df_distrib['distributeur'] == distrib]['score'].values[0]

date_sortie = st.date_input('Choisir la date de sortie', min_value=date(2000, 1, 1), max_value=date(2023, 12, 31))

country = st.selectbox('Sélectionnez le pays', ['USA', 'France', 'Autre'])

genre = st.selectbox('Sélectionnez le genre', ['Comédie', 'Documentaire', 'Action'])

budget = st.slider('Sélectionnez le budget', 1000000, 200000000, step=1000000, value=50000000)

st.write(score_acteur)
st.write(score_real)
st.write(score_scenar)
st.write(date_sortie.day)





