import streamlit as st
from include.css_and_credit import css_and_credit
st.set_page_config(page_title="Exploitation cinématographique", page_icon='🎬', layout="wide")

css_and_credit()

st.header("🛠️Preprocessing du jeu de données🛠️")

st.markdown("""
<div class ="centered-content"><div class="box"><h3>Introduction :</h3>
    <p>Le prétraitement (preprocessing) des données vise à préparer les données brutes pour que notre modèle futur soit le plus performant possible  :</p>
    <p>• Nettoyant les données en éliminant les valeurs aberrantes (réalisé juste avant la modélisation), et en gérant les valeurs manquantes. NB : le dédoublonnage n'était pas nécessaire.</p>
    <p>• Transformant les features en formats compatibles avec les algorithmes d'apprentissage automatique, tels que la normalisation des valeurs et les onehotencoding.</p>
    <p>• En améliorant la qualité des données en calculant des scores afin d'optimiser les performances des modèles et de garantir des résultats plus fiables.</p>
    <p>• Suppression des colonnes n'ayant pas d'intérêt pour notre modèle ou étant composées majoritairement de valeurs manquantes.</p>
</div></div>
""", unsafe_allow_html=True)

st.markdown("""
<div class ="centered-content"><div class="box"><h3>Traitement des valeurs manquantes :</h3>
    <p>In fine, nous avions très peu de valeurs manquantes. Notre choix a été dans la grande majorité des cas de supprimer les lignes avec des valeurs manquantes.</p>
</div></div>
""", unsafe_allow_html=True)

st.markdown("""
<div class ="centered-content"><div class="box"><h3>Formatage des données :</h3>
    <p>Les étapes de formatage des données :</p>
    <p>• Onehotencoding des genres.</p>
    <p>• Onehotencoding de l'origine du pays du film (en ayant retenu que 3 catégories : France ou USA ou autre (si France et USA sont en False).</p>
    <p>• Conversion et reformatage des données budgets : identification de toutes les devises différentes, conversion en euros en utilisant le taux de change à date de chaque devise.</p>
    <p>• Extraction des jours, jours_semaine, mois de la date de sortie des films, puis standardisation cyclique des variables obtenues.</p>
    <p>• Mise en oeuvre d'un score acteurs, d'un score réalisateurs, d'un score scenaristes, d'un score distributeur.</p>
    <p>Description schématique du score Acteurs :</p>
    <img src="https://github.com/NicolasDartois/streamlit_2/blob/main/images/score_acteur.png?raw=true"  class="fit-img"/>
</div></div>
""", unsafe_allow_html=True)

