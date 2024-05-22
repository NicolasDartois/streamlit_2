import streamlit as st

for i in range(25):
    st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.subheader("🎥oct23_cda_exploitation-cinématographique🎥")
st.sidebar.markdown("_____________________")
st.sidebar.markdown("Manon FOUQUET")
st.sidebar.markdown("Sylvain BRAIZET")
st.sidebar.markdown("Nicolas DARTOIS")

st.header("🛠️Préparation les données-Preprocessing🛠️")

background_image = '''
    <style>
    .stApp {
        background-color: white;
        background-image: url("https://github.com/NicolasDartois/streamlit_2/blob/main/images/background.jpg?raw=true");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }
    .box {
        background-color: white;
        padding: 20px;
        margin-top: 20px;
        margin-bottom: 20px;
        box-shadow: 0 10px 12px rgba(0, 0, 0, 0.1);
        border-radius: 10px;
        text-align: justify;
    }
    .fit-img {
    width: 100%;
    height: 100%;
    object-fit: cover; /* Peut aussi être 'contain' selon le besoin */
    display: block;
    }
    </style>
    '''
st.markdown(background_image, unsafe_allow_html=True)

st.markdown("""
<div class="box"><h3>Introduction :</h3>
    <p>Le prétraitement (preprocessing) des données vise à préparer les données brutes pour que notre modèle futur soit le plus performant possible  :</p>
    <p>• Nettoyant les données en éliminant les valeurs aberrantes (réalisé juste avant la modélisation), et en gérant les valeurs manquantes. NB : le dédoublonnage n'était pas nécessaire.</p>
    <p>• Transformant les features en formats compatibles avec les algorithmes d'apprentissage automatique, tels que la normalisation des valeurs et les onehotencoding.</p>
    <p>• En améliorant la qualité des données en calculant des scores afin d'optimiser les performances des modèles et de garantir des résultats plus fiables.</p>
    <p>• Nettoyant les données en éliminant les valeurs aberrantes (réalisé juste avant la modélisation), et en gérant les valeurs manquantes. NB : le dédoublonnage n'était pas nécessaire.</p>
    <p>• Transformant les features en formats compatibles avec les algorithmes d'apprentissage automatique, tels que la normalisation des valeurs et les onehotencoding.</p>
    <p>• En améliorant la qualité des données en calculant des scores afin d'optimiser les performances des modèles et de garantir des résultats plus fiables.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="box"><h3>Traitement des valeurs manquantes :</h3>
    <p>Exemple de texte</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="box"><h3>Formatage des données :</h3>
    <p>Les étapes de formatage des données :</p>
    <p>• Onehotencoding des genres.</p>
    <p>• Onehotencoding de l'origine du pays du film (en ayant retenu que 3 catégories : France ou USA ou autre (si France et USA sont en False).</p>
    <p>• Conversion et reformatage des données budgets : identification de toutes les devises différentes, conversion en euros en utilisant le taux de change à date de chaque devise.</p>
    <p>• Extraction des jours, jours_semaine, mois de la date de sortie des films, puis standardisation cyclique des variables obtenues.</p>
    <p>• Mise en oeuvre d'un score acteurs, d'un score réalisateurs, d'un score scenaristes, d'un score distributeur.</p>
    <p>Description schématique du score Acteurs :</p>
    <img src="https://github.com/NicolasDartois/streamlit_2/blob/main/images/score_acteur.png?raw=true"  class="fit-img"/>
</div>
""", unsafe_allow_html=True)

st.image('images/score_acteur.png')
