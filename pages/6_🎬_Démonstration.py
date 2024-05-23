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

pays = st.selectbox('Sélectionnez le pays', ['USA', 'France', 'Autre'])

genre = st.selectbox('Sélectionnez le genre', ['Comédie', 'Documentaire', 'Action'])

budget = st.slider('Sélectionnez le budget en millions d\'euros', 10, 200, step=10, value=50)

duree = st.slider('Sélectionnez la duree', 40, 200, step=20, value=100)

df_predict = pd.DataFrame(columns = ['budget_euro', 'acteur', 'realisateur', 'scenariste', 'distributeur', 'duree', 'USA', 'France', 'Famille', 'Comédie musicale', 'Musical', 'Comédie dramatique', 'Action', 'Aventure', 'Historique', 'Biopic', 'Guerre', 'Drame', 'Documentaire', 'Fantastique', 'Espionnage', 'Animation', 'Romance', 'Comédie', 'Policier', 'Epouvante-horreur', 'Thriller', 'Science Fiction', 'cos_jour_mois', 'sin_jour_mois', 'cos_mois', 'sin_mois', 'cos_jour_semaine', 'sin_jour_semaine'])


if st.button('Scotty, lance la prédiction !'):
    data_predict = {
        'budget_euro': budget*1000000,
        'acteur': score_acteur,
        'realisateur': score_real,
        'scenariste': score_scenar,
        'distributeur': score_distrib,
        'duree': duree,
        'USA': True if pays == 'USA' else False,
        'France': True if pays == 'France' else False,
        'Famille': False,
        'Comédie musicale': False,
        'Musical': False,
        'Comédie dramatique': False,
        'Action': True if genre == 'Action' else False,
        'Aventure': False,
        'Historique': False,
        'Biopic': False,
        'Guerre': False,
        'Drame': False,
        'Documentaire': True if genre == 'Documentaire' else False,
        'Fantastique': False,
        'Espionnage': False,
        'Animation': False,
        'Romance': False,
        'Comédie': True if genre == 'Comédie' else False,
        'Policier': False,
        'Epouvante-horreur': False,
        'Thriller': False,
        'Science Fiction': False,
        'cos_jour_mois': np.cos(date_sortie.day),
        'sin_jour_mois': np.sin(date_sortie.day),
        'cos_mois': np.cos(date_sortie.month),
        'sin_mois': np.sin(date_sortie.month),
        'cos_jour_semaine': np.cos(date_sortie.weekday()),
        'sin_jour_semaine': np.sin(date_sortie.weekday())
    }
    df_predict.loc[0] = data_predict
    input_data = df_predict
    prediction = model.predict(input_data)
    st.dataframe(df_predict)
    st.write('La prédiction est:', prediction[0])




