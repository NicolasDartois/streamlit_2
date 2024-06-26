import streamlit as st
from include.css_and_credit import css_and_credit
st.set_page_config(page_title="Exploitation cinématographique", page_icon='🎬', layout="wide")

css_and_credit()

st.header("🛠️ Preprocessing du jeu de données")

st.markdown("""
<div class ="centered-content"><div class="box"><h3>Introduction :</h3>
    <p>Le prétraitement (preprocessing) des données vise à préparer les données brutes pour que notre modèle futur soit le plus performant possible  :</p>
    <p>• Nous avons nettoyé les données en éliminant les valeurs aberrantes (ce qui a été réalisé juste avant la phase de modélisation) et géré les valeurs manquantes. À noter que le dédoublonnage n'était pas nécessaire dans ce contexte.</p>
    <p>• Nous avons transformé les features en formats compatibles avec les algorithmes d'apprentissage automatique, tels que la normalisation des valeurs et les onehotencoding.</p>
    <p>• Nous avons amélioré la qualité des données en calculant des scores afin d'optimiser les performances des modèles et de garantir des résultats plus fiables.</p>
    <p>• Nous avons supprimé les colonnes n'ayant pas d'intérêt pour notre modèle ou étant composées majoritairement de valeurs manquantes.</p>
    </div></div>
""", unsafe_allow_html=True)

st.markdown("""
<div class ="centered-content"><div class="box"><h3>Traitement des valeurs manquantes :</h3>
    <p>En fin de compte, nous avons constaté que nous avions très peu de valeurs manquantes. Dans la grande majorité des cas, nous avons décidé de supprimer les lignes comportant des valeurs manquantes, car cela nous semblait être l'approche la plus appropriée.</p>
</div></div>
""", unsafe_allow_html=True)

st.markdown("""
<div class ="centered-content"><div class="box"><h3>Formatage des données :</h3>
    <p>Les étapes de formatage des données :</p>
    <p>• Nous avons procédé au Onehotencoding des genres.</p>
    <p>• Nous avons procédé au Onehotencoding de l'origine du pays du film (en ayant retenu que 3 catégories : France ou USA ou autre (si France et USA sont en False).</p>
    <p>• Nous avons converti et reformaté les données budgétaires : identification de toutes les devises différentes (et devises identiques mais renseignées différemment), conversion en euros en utilisant le taux de change à date de chaque devise.</p>
    <p>• Nous avons extrait les jours, jours_semaine, mois de la date de sortie des films, puis nous les avons standardisé en variables cycliques.</p>
    <p>• Nous avons mis en oeuvreun score acteurs, un score réalisateurs, un score scenaristes, un score distributeur.</p>
    <p>Description schématique du score Acteurs :</p>
    <img src="https://github.com/NicolasDartois/streamlit_2/blob/main/images/score_acteur.png?raw=true"  class="fit-img"/>
</div></div>
""", unsafe_allow_html=True)

