import streamlit as st
import joblib as jl
import pandas as pd
import numpy as np
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
score_distrib  = df_distrib[df_distrib['distributeur'] == distrib]['score'].values[0]

date_sortie = st.date_input('Choisir la date de sortie', min_value=date(2000, 1, 1), max_value=date(2023, 12, 31))

country = st.selectbox('Sélectionnez le pays', ['USA', 'France', 'Autre'])

genre = st.selectbox('Sélectionnez le genre', ['Comédie', 'Documentaire', 'Action'])

budget = st.slider('Sélectionnez le budget en millions d\'euros', 10, 200, step=10, value=50)

duree = st.slider('Sélectionnez la duree', 40, 200, step=20, value=100)

df_predict = pd.DataFrame(columns = ['budget_euro', 'acteur', 'realisateur', 'scenariste', 'distributeur', 'duree', 'USA', 'France', 'Famille', 'Comédie musicale', 'Musical', 'Comédie dramatique', 'Action', 'Aventure', 'Historique', 'Biopic', 'Guerre', 'Drame', 'Documentaire', 'Fantastique', 'Espionnage', 'Animation', 'Romance', 'Comédie', 'Policier', 'Epouvante-horreur', 'Thriller', 'Science Fiction', 'cos_jour_mois', 'sin_jour_mois', 'cos_mois', 'sin_mois', 'cos_jour_semaine', 'sin_jour_semaine'])

data_predict = {
    'budget_euro': budget,
    'acteur': score_acteur,
    'realisateur': score_real,
    'scenariste': score_scenar,
    'distributeur': score_distrib,
    'duree': duree,
    'USA': False,
    'France': False,
    'Famille': False,
    'Comédie musicale': False,
    'Musical': False,
    'Comédie dramatique': False,
    'Action': False,
    'Aventure': False,
    'Historique': False,
    'Biopic': False,
    'Guerre': False,
    'Drame': False,
    'Documentaire': False,
    'Fantastique': False,
    'Espionnage': False,
    'Animation': False,
    'Romance': False,
    'Comédie': False,
    'Policier': False,
    'Epouvante-horreur': False,
    'Thriller': False,
    'Science Fiction': False,
    'cos_jour_mois': cos(date_sortie.day),
    'sin_jour_mois': sin(date_sortie.day),
    'cos_mois': None,
    'sin_mois': None,
    'cos_jour_semaine': None,
    'sin_jour_semaine': None
}


st.write(score_acteur)
st.write(score_real)
st.write(score_scenar)
st.write(date_sortie.day*2)
st.write(date_sortie.month*2)
st.write(date_sortie.year*2)





