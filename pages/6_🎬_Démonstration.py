import streamlit as st
import joblib as jl
import pandas as pd
import numpy as np
from include.css_and_credit import css_and_credit
from datetime import date
from openai import OpenAI
import os

#client = OpenAI(api_key=os.environ['API_KEY_OPENAI'])

def generate_text(prompt):
    response = openai.Completion.create(
        engine="gpt-4",
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
st.header("🎬 Démonstration")
            
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
                
                #prompt_synopsis = f"""Génère un synopsis en français pour un film {pays} sorti en {date_sortie.year}, réalisé par {real}, distribué par {distrib}, dans le genre {genre}, avec {acteur1} en acteur principal et {acteur2} en acteur secondaire.(Attention, ne donne pas le titre dans ta reponse)"""
                #response_synopsis = client.chat.completions.create(
                #    model="gpt-4",
                #    messages=[{"role": "user", "content": prompt_synopsis}],
                #)
        
                #prompt_titre = f"""Génère un titre en français pour ce synopsis (Attention, uniquement le titre dans ta reponse, rien d'autre) : {response_synopsis}"""
                #response_titre = client.chat.completions.create(
                #    model="gpt-4",
                #    messages=[{"role": "user", "content": prompt_titre}],
                #)
                
                #prompt_affiche = f"""Génère une affiche en français pour ce synopsis (Aucun acteur sur l'affiche ne doit ressembler à une personne réelle) : {response_synopsis}"""
                #response_affiche = client.images.generate(
                #    model="dall-e-3", 
                #    prompt=prompt_affiche, 
                #    n=1, 
                #    size="1024x1792"
                #)
              
                col1, col2, col3, col4 = st.columns([2, 3, 13, 2])
                st.markdown(f"""
                    <div class="wrapper2">
                        <div class="box">
                            <img src="https://github.com/NicolasDartois/streamlit_2/blob/main/images/test.png?raw=true" class="fit-img"/>
                        </div>
                        <div class="box">
                            <h3>"Double Jeu à Manhattan : Variations sur un Thème de Woody Allen"</h3>
                            <h8>Le <b>{date_sortie}</b> en salle</h8>
                            <h8>Par <b>{real}</b></h8>
                            <h8> Avec <b>{acteur1}</b> et <b>{acteur2}</b></h8>
                            <p>Dans un quartier chic de Manhattan, vit un ancien professeur d'université aux talents musicaux remarquables mais dont la carrière artistique n'a jamais décollé, joué par Woody Allen. Sa vie ordinaire et quelque peu morose s'anime un jour où un double mystérieux le remplace subitement dans sa vie quotidienne. Ce double, aussi joué par Woody Allen, est tout ce qu'il n'a jamais réussi à être : confiant, séduisant, et incroyablement talentueux. Notre professeur comprend rapidement que son double est une version améliorée de lui-même et accepte sa présence, espérant tirer des leçons de son comportement.Cependant, alors que le double commence à prendre une place de plus en plus importante, créant des complications hilarantes, l'ancien professeur se trouve dans une position délicate : il doit à la fois gérer sa jalousie envers cette version de lui-même plus réussie et essayer de reprendre sa place dans sa propre vie. Il concocte un plan pour se débarrasser de son alter ego, mais les choses ne se passent pas comme prévu. S'ensuit une série de péripéties irrésistiblement drôles qui mettront en lumière le vrai visage du professeur.Le film, réalisé par Roman Polanski, emprunte à la fois à la comédie, au fantastique et au drame, jouant habilement sur les différentes tonalités pour faire avancer l'histoire. Entre situations cocasses, reparties cinglantes et moments d'émotion, on suit avec délice le combat existentiel de cet homme contre lui-même, dans une mise en abîme teintée d'ironie et de tendresse. Il sera question d'identité, de quête du soi, d'acceptation de soi et d'accomplissement personnel à travers cette comédie inattendue et délicieusement absurde.</p>
                        </div>
                    </div>""", unsafe_allow_html=True)

                
                

