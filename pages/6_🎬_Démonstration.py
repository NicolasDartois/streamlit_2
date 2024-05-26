import streamlit as st
import joblib as jl
import pandas as pd
import numpy as np
from include.css_and_credit import css_and_credit
from datetime import date
import openai

openai.api_key = 'votre_cle_api_openai'

def generate_text(prompt):
    response = openai.Completion.create(
        engine="gpt-4", # Utilisez "text-davinci-003" si "gpt-4" n'est pas disponible pour vous
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    return response['data'][0]['url']

st.set_page_config(page_title="Exploitation cinématographique", page_icon='🎬', layout="wide")

css_and_credit()
st.header("🎬Démonstration🎬")
            
st.markdown("<br><br><br>", unsafe_allow_html=True)
model = jl.load("models/GB.joblib")

df_acteur = pd.read_csv('data/score_acteur.csv')
df_real = pd.read_csv('data/score_real.csv')
df_scenar = pd.read_csv('data/score_scenar.csv')
df_distrib = pd.read_csv('data/score_distrib.csv')

col1, col2, col3, col4, col5, col6 = st.columns([1,2,2,2,2,1])
with col2:
    acteur1 = st.selectbox('Acteur principal :', df_acteur['Acteur'])
    score_acteur1 = df_acteur[df_acteur['Acteur'] == acteur1]['Score'].values[0]
with col3:    
    acteur2 = st.selectbox('Acteur secondaire :', df_acteur['Acteur'])
    score_acteur2 = df_acteur[df_acteur['Acteur'] == acteur2]['Score'].values[0]
    score_acteur = (score_acteur1*1.125)+(score_acteur2*0.75)   
with col4:    
    real = st.selectbox('Réalisateur :', df_real['realisateur'])
    score_real = df_real[df_real['realisateur'] == real]['score'].values[0]
with col5:
    scenar = st.selectbox('Scénariste :', df_scenar['scenariste'])
    score_scenar = df_scenar[df_scenar['scenariste'] == scenar]['score'].values[0]

col1, col2, col3, col4, col5, col6 = st.columns([1,2,2,2,2,1])
with col2:    
    distrib = st.selectbox('Distributeur :', df_distrib['distributeur'])
    score_distrib  = df_distrib[df_distrib['distributeur'] == distrib]['score'].values[0]
with col3:    
    date_sortie = st.date_input('Date de sortie', min_value=date(2000, 1, 1), max_value=date(2023, 12, 31))
with col4:
    pays = st.selectbox('Sélectionnez le pays', ['USA', 'France', 'Autre'])
with col5:     
    genre = st.selectbox('Sélectionnez le genre', ['Comédie', 'Documentaire', 'Action'])

col1, col2, col3, col4 = st.columns([1,4,4,1])
with col2:
    budget = st.slider('Sélectionnez le budget en millions d\'euros', 10, 200, step=10, value=50)
with col3:    
    duree = st.slider('Sélectionnez la duree', 40, 200, step=20, value=100)

df_predict = pd.DataFrame(columns = ['budget_euro', 'acteur', 'realisateur', 'scenariste', 'distributeur', 'duree', 'USA', 'France', 'Famille', 'Comédie musicale', 'Musical', 'Comédie dramatique', 'Action', 'Aventure', 'Historique', 'Biopic', 'Guerre', 'Drame', 'Documentaire', 'Fantastique', 'Espionnage', 'Animation', 'Romance', 'Comédie', 'Policier', 'Epouvante-horreur', 'Thriller', 'Science Fiction', 'cos_jour_mois', 'sin_jour_mois', 'cos_mois', 'sin_mois', 'cos_jour_semaine', 'sin_jour_semaine'])

col1, col2, col3 = st.columns([1, 8, 1])
with col2: 
            if st.button('Scotty, lance la prédiction !'):
                data_predict = {
                    'budget_euro': int(budget*1000000),
                    'acteur': score_acteur,
                    'realisateur': score_real,
                    'scenariste': score_scenar,
                    'distributeur': score_distrib,
                    'duree': int(duree),
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
                st.dataframe(df_predict[['budget_euro','acteur','realisateur','scenariste','distributeur','duree','USA','France','Action','Documentaire','Comédie','cos_jour_mois','sin_jour_mois','cos_mois','sin_mois','cos_jour_semaine','sin_jour_semaine']])
                st.write(f'Le modèle predit <span style="font-size:20px; color:#27AE60;"><b>{str(round(prediction[0]))}</b></span> entrées la première semaine en france.', unsafe_allow_html=True)
                if st.button('Mais que fait John Connor ?!'):
                    st.dataframe(df_predict[['budget_euro','acteur','realisateur','scenariste','distributeur','duree','USA','France','Action','Documentaire','Comédie','cos_jour_mois','sin_jour_mois','cos_mois','sin_mois','cos_jour_semaine','sin_jour_semaine']])
                    st.write(f'Le modèle predit <span style="font-size:20px; color:#27AE60;"><b>{str(round(prediction[0]))}</b></span> entrées la première semaine en france.', unsafe_allow_html=True)
                
# Utiliser l'état de session pour suivre l'interaction avec les boutons
if 'button1_clicked' not in st.session_state:
    st.session_state.button1_clicked = False
if 'button2_clicked' not in st.session_state:
    st.session_state.button2_clicked = False

# Premier bouton
if st.button('Scotty ?!'):
    st.session_state.button1_clicked = True

if st.session_state.button1_clicked:
    data_predict = {
        'budget_euro': int(budget*1000000),
        'acteur': score_acteur,
        'realisateur': score_real,
        'scenariste': score_scenar,
        'distributeur': score_distrib,
        'duree': int(duree),
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
    st.dataframe(df_predict[['budget_euro','acteur','realisateur','scenariste','distributeur','duree','USA','France','Action','Documentaire','Comédie','cos_jour_mois','sin_jour_mois','cos_mois','sin_mois','cos_jour_semaine','sin_jour_semaine']])
    st.write(f'Le modèle predit <span style="font-size:20px; color:#27AE60;"><b>{str(round(prediction[0]))}</b></span> entrées la première semaine en france.', unsafe_allow_html=True)
    
    # Deuxième bouton
    if st.button('Mais que fait John Connor ?!'):
        st.session_state.button2_clicked = True

if st.session_state.button2_clicked:
    st.dataframe(df_predict[['budget_euro', 'acteur', 'realisateur', 'scenariste', 'distributeur', 'duree', 'USA', 'France', 'Action', 'Documentaire', 'Comédie', 'cos_jour_mois', 'sin_jour_mois', 'cos_mois', 'sin_mois', 'cos_jour_semaine', 'sin_jour_semaine']])
    st.write(f'Le modèle prédit <span style="font-size:20px; color:#27AE60;"><b>{str(round(prediction[0]))}</b></span> entrées la première semaine en France.', unsafe_allow_html=True)


