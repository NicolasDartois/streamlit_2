import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title="Projet Ciné", layout="centered") 
st.title("🎥 L'IA au service de la production cinématographique ! 🎥")

for i in range(25):
    st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.subheader("🎥oct23_cda_exploitation-cinématographique🎥")
st.sidebar.markdown("_____________________")
st.sidebar.markdown("Manon FOUQUET")
st.sidebar.markdown("Sylvain BRAIZET")
st.sidebar.markdown("Nicolas DARTOIS")

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
        text-align: justified;
    }
    </style>
    '''
st.markdown(background_image, unsafe_allow_html=True)


st.markdown('<div class="box"><h3>Le contexte :</h3><p>Le projet que nous présentons dans ce document est le fruit de notre propre initiative. Inspiré par une idée originale d\'un des membres de notre groupe, ce projet s\'est développé autour d\'une ambition commune : transformer radicalement l\'industrie du cinéma !</p><p>Traditionnellement, il est courant que les producteurs et les professionnels du cinéma fassent des paris amicaux sur le nombre de spectateurs qu\'un film attirera à la fin de sa première semaine en salle. Cette pratique, à la fois ludique et ancrée dans les mœurs du secteur, a été le catalyseur de notre projet. Notre objectif est de mettre au point un modèle de machine learning capable de prédire avec la plus grande précision possible le nombre d\'entrées qu\'un film réalisera. Ce modèle s\'appuiera sur des données préalablement collectées, alliant des critères quantitatifs et qualitatifs pour établir ses prévisions.</p></div>', unsafe_allow_html=True)

st.markdown('<div class="box"><h3>L\'objectif du projet :</h3><p>L\'objectif central de notre projet est de développer un outil accessible et convivial, permettant à tout utilisateur de prévoir le nombre de spectateurs d\'un film à la fin de sa première semaine en salle. En renseignant des paramètres spécifiques de son choix, l\'utilisateur pourra obtenir rapidement une estimation précise des entrées en salle.</p></div>', unsafe_allow_html=True)

st.markdown('<div class="box"><h3>Pourquoi avoir choisi Streamlit ?</h3><p>Au-delà des fonctionnalités de base de cet applicatif, qui contribuent à rendre nos présentations plus dynamiques et visuellement impactantes, il est important de souligner que le choix de Streamlit pour présenter notre projet a également répondu à plusieurs objectifs pédagogiques. En effet, Streamlit est un outil de plus en plus prisé au sein des entreprises.</p><p>En intégrant Streamlit, nous avons non seulement amélioré l\'interactivité et l\'impact visuel de notre présentation, mais aussi enrichi notre expérience d\'apprentissage avec une application technologique en pleine expansion. Cette démarche nous a permis de nous approprier efficacement cet outil moderne, en vue de l\'utiliser plus tard dans nos futures carrières.</p></div>', unsafe_allow_html=True)

