import streamlit as st
import statsmodels.api as sm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from xgboost import XGBRegressor
import joblib

st.set_page_config(page_title="Projet Ciné", layout="wide") 

st.title("L'IA au service de la production cinématographique !")

st.sidebar.title("Sommaire")
pages=["Présentation du projet", "Collecte et Exploration des Données", "Analyse des Données (DataViz)", "Préparation les données - Preprocessing", "Présentation du modèle", "DEMONSTRATION"]
page=st.sidebar.radio("Aller vers", pages)

#########################################################
if page == pages[0] : 

    col1, col2 = st.columns(2)

    with col1:
        st.image('images/cinema.jpg')

    with col2:
        st.write("### Le contexte :")
        st.write("Le projet que nous présentons dans ce document est le fruit de notre propre initiative. Inspiré par une idée originale d'un des membres de notre groupe, ce projet s'est développé autour d'une ambition commune : transformer radicalement l'industrie du cinéma !")
        st.write("Traditionnellement, il est courant que les producteurs et les professionnels du cinéma fassent des paris amicaux sur le nombre de spectateurs qu'un film attirera à la fin de sa première semaine en salle. Cette pratique, à la fois ludique et ancrée dans les mœurs du secteur, a été le catalyseur de notre projet. Notre objectif est de mettre au point un modèle de machine learning capable de prédire avec la plus grande précision possible le nombre d'entrées qu'un film réalisera. Ce modèle s'appuiera sur des données préalablement collectées, alliant des critères quantitatifs et qualitatifs pour établir ses prévisions.")
    
        st.write("### L'objectif du projet :")
        st.write("L'objectif central de notre projet est de développer un outil accessible et convivial, permettant à tout utilisateur de prévoir le nombre de spectateurs d'un film à la fin de sa première semaine en salle. En renseignant des paramètres spécifiques de son choix, l'utilisateur pourra obtenir rapidement une estimation précise des entrées en salle.")
        st.write("### Pourquoi avoir choisi streamlit ?")
        st.write("Au-delà des fonctionnalités de base de cet applicatif, qui contribuent à rendre nos présentations plus dynamiques et visuellement impactantes, il est important de souligner que le choix de Streamlit pour présenter notre projet a également répondu à plusieurs objectifs pédagogiques. En effet, Streamlit est un outil de plus en plus prisé au sein des entreprises.")
        st.write("En intégrant Streamlit, nous avons non seulement amélioré l'interactivité et l'impact visuel de notre présentation, mais aussi enrichi notre expérience d'apprentissage avec une application technologique en pleine expansion. Cette démarche nous a permis de nous approprier efficacement cet outil moderne, en vue de l'utiliser plus tard dans nos futures carrières.")
    
#########################################################
if page == pages[1] : 
    st.write("### Notre jeu de donnée lors du démarrage et son évolution")
    st.write("Au cours de l'analyse initiale de notre jeu de données et à la lumière de nos premiers acquis en matière de formation, nous avons constaté que nos données étaient insuffisantes pour élaborer un modèle de machine learning robuste. Plusieurs défis se sont présentés : d'abord, notre jeu de données contenait un nombre excessif de valeurs manquantes. De plus, nous hésitions encore sur la variable cible à prédire, hésitant entre les revenus générés et les votes des spectateurs.")       
    st.write("Par ailleurs, notre jeu de données couvrait le marché mondial, ce qui nous a rapidement motivé a nous focaliser sur le marché français, necessitant de trouver de nouvelles sources de données.")
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image('images/Heatmap_NaN.png')
    st.write("Pour enrichir notre base, nous avons mis en place plusieurs actions :")
    st.write("‣ Nous avons contacté CBO BOX OFFICE, une société fournissant des données aux professionnels du cinéma. Malgré une proposition contractuelle exposant le contexte non lucratif et éducatif de notre projet, notre demande est restée sans réponse.")
    st.write("‣ Nous avons exploré d'autres plateformes telles que KAGGLE pour trouver des jeux de données robustes et adaptées à nos besoins, mais sans succès.")
    st.write("‣ Nous avons décidé de procéder au Webscraping de données sur des sites réputés bien administrés, tels qu'Allociné, IMDB PRO (gratuit le premier mois), et JPBOX Office. Avec le soutien de notre chef de cohorte, qui a débloqué un sprint complet dédié au web scraping, nous avons utilisé Beautiful Soup pour extraire et compléter notre jeu de données pour le marché français. Nous avons ainsi obtenu la liste des films sur Allociné avec leurs box-office et titres originaux, qui nous serviront plus tard comme clés d'indexation. Nous avons enrichi ces films avec des caractéristiques telles que la note des spectateurs, la note de la presse, les acteurs principaux, les réalisateurs, les scénaristes, les distributeurs, la date de sortie, la nationalité, le budget et le genre.")
    st.write("‣ Sur IMDB, nous avons récupéré un fichier global contenant les identifiants IMDB des films, leur durée et leurs titres originaux (toujours dans l'optique de l'utiliser comme clé d'indexation).")
    st.write("‣ Enfin, nous avons décidé de scraper sur IMDB et Allociné des données permettant de construire un score de notoriété pour chaque acteur, réalisateur ou scénariste, en nous basant sur le Starmeter, le nombre de récompenses reçues, le nombre de films réalisés et la durée de leur carrière.")
    st.write("Ces démarches nous ont permis de bâtir un jeu de données plus complet et pertinent pour le développement de notre modèle prédictif du nombre d'entrées sur le marché français.")
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.image('images/Schema_budget.png')

#########################################################    
if page == pages[2] :
    allocine = pd.read_csv('data/allocine.csv')
    

    #---------------#
    pays_counts = allocine['pays'].value_counts()
    top_pays = pays_counts[:8]
    autres = pays_counts[8:].sum()
    top_pays['Autres'] = autres    
    fig1 = go.Figure(data=[go.Pie(labels=top_pays.index, values=top_pays.values, hole=.3)])
    fig1.update_traces(textposition='inside', textinfo='percent+label')
    fig1.update_layout(
    width=800,
    height=600,
    title_text='Répartition des films par pays',
    annotations=[dict(text='Pays', x=0.5, y=0.5, font_size=20, showarrow=False)],
    legend_title="Pays"
    )
    st.plotly_chart(fig1)
    
    #---------------#
    fig2 = px.box(allocine, x="premiere_semaine_france",
             hover_data=['titre_original'],
             title='Analyse de la distribution de notre target: première semaine en France',
             labels={'premiere_semaine_france': 'Première semaine en France'})
    fig2.update_layout(width=1200, height=500)
    fig2.update_layout(xaxis=dict(showgrid=True, gridwidth=1, gridcolor='lightgrey'))
    st.plotly_chart(fig2)
    
    #---------------#
    filtered_data = allocine[(allocine['annee'] > 2000) & (allocine['annee'] <= 2023)]
    film_counts = filtered_data['annee'].value_counts().sort_index()
    colorscale = [[0, 'blue'], [1, 'orange']]
    fig3 = go.Figure(data=[go.Bar(x=film_counts.index, y=film_counts, marker=dict(color=film_counts, colorscale=colorscale, cmin=0, cmax=film_counts.max()))])
    fig3.update_layout(title='Nombre de films sortis par année en France (après 2000)', xaxis_title='Année de sortie', yaxis_title='Nombre de films')
    st.plotly_chart(fig3)

    #---------------#
    correlation = allocine['cumul_france'].corr(allocine['premiere_semaine_france'])
    fig4 = px.scatter(
    allocine, 
    x='cumul_france', 
    y='premiere_semaine_france',
    hover_data=['titre_original'],
    title=f'Corrélation entre le cumul en France et la première semaine en France: {correlation:.2f}',
    labels={'cumul_france': 'Cumul en France', 'premiere_semaine_france': 'Première semaine en France'},
    opacity=0.5,
    trendline='ols'
    )
    fig4.data[1].line.color = 'red'
    fig4.update_layout(margin={'l': 40, 'b': 40, 't': 80, 'r': 40}, hovermode='closest')
    fig4.update_xaxes(showgrid=True, title='Cumul en France')
    fig4.update_yaxes(showgrid=True, title='Première semaine en France')
    st.plotly_chart(fig4)

    #---------------#
    plt.figure(figsize=(16, 6))
    fig5 = sns.lmplot(x='cumul_france',y='premiere_semaine_france',data=allocine, ci=90, line_kws={'color': 'red'});
    st.pyplot(fig5)
    #---------------#

    #---------------#

    #---------------#

    #---------------#

    #---------------#

    #---------------#

    #---------------#

    #---------------#
    
#########################################################
if page == pages[3] :
    st.write("### Introduction :")
    st.write("Le prétraitement (preprocessing) des données vise à préparer les données brutes pour que notre modèle futur soit le plus performant possible  :")
    st.markdown("""
    <ul>
        <li>Nettoyant les données en éliminant les valeurs aberrantes (réalisé juste avant la modélisation), et en gérant les valeurs manquantes. NB : le dédoublonnage n'était pas nécessaire.</li>
        <li>Transformant les features en formats compatibles avec les algorithmes d'apprentissage automatique, tels que la normalisation des valeurs et les onehotencoding.</li>
        <li>En améliorant la qualité des données en calculant des scores afin d'optimiser les performances des modèles et de garantir des résultats plus fiables.</li>
    </ul>
    """, unsafe_allow_html=True)
    st.write("### Traitement des valeurs manquantes :")
    st.write("Exemple de texte")
    st.write("### Formatage des données :")
    st.write("Les étapes de formatage des données :")
    st.markdown("""
    <ul>
        <li>Onehotencoding des genres</li>
        <li>Onehotencoding de l'origine du pays du film (en ayant retenu que 3 catégories : France ou USA ou autre (si France et USA sont en False)</li>
        <li>conversion et reformatage des données budgets : identification de toutes les devises différentes, conversion en euros en utilisant le taux de change à date de chaque devise</li>
        <li>extraction des jours, jours_semaine, mois de la date de sortie des films, puis standardisation cyclique des variables obtenues</li>
        <li>Mise en oeuvre d'un score acteurs, d'un score réalisateurs, d'un score scenaristes, d'un score distributeur</li>
        <li>Description schématique du score Acteurs :</li>
    </ul>
    <br>
    <br>
    """, unsafe_allow_html=True)
    st.image('images/score_acteur.png')
    
#########################################################
if page == pages[4] :  
    st.write("### Modélisations :")
    
    df = pd.read_csv('data/Allocine_v3.csv')
    
    X = df.drop(columns=['premiere_semaine_france'])
    y = df['premiere_semaine_france']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    scaler = StandardScaler()
    X_train[['budget_euro', 'acteur', 'realisateur', 'scenariste', 'distributeur', 'note_presse', 'duree']] = scaler.fit_transform(X_train[['budget_euro', 'acteur', 'realisateur', 'scenariste', 'distributeur', 'note_presse', 'duree']])
    X_test[['budget_euro', 'acteur', 'realisateur', 'scenariste', 'distributeur', 'note_presse', 'duree']] = scaler.transform(X_test[['budget_euro', 'acteur', 'realisateur', 'scenariste', 'distributeur', 'note_presse', 'duree']])

    def prediction(classifier):
        if classifier == 'Random Forest':
            clf = joblib.load("models/RF.joblib")
        elif classifier == 'Linear Regression':
            clf = joblib.load("models/LR.joblib")
        elif classifier == 'Decision Tree':
            clf = joblib.load("models/DT.joblib")
        elif classifier == 'Gradient Boosting':
            clf = joblib.load("models/GB.joblib")
        elif classifier == 'XGBoost':
            clf = joblib.load("models/XGB.joblib")
        clf.fit(X_train, y_train)
        return clf
    
    def scores(clf, choice):
        if choice == 'R²':
            return r2_score(y_test, clf.predict(X_test))
        elif choice == 'MAE':
            return mean_absolute_error(y_test, clf.predict(X_test))
    
    choix = ['Random Forest', 'Linear Regression', 'Decision Tree', 'Gradient Boosting', 'XGBoost']
    option = st.selectbox('Choix du modèle', choix)
    st.write('Le modèle choisi est :', option)

    clf = prediction(option)
    display = st.radio('Que souhaitez-vous montrer ?', ('R²', 'MAE'))
    if display == 'R²':
        st.write(scores(clf, display))
    elif display == 'MAE':
        st.write(scores(clf, display))

#########################################################
if page == pages[5] : 
    st.write("### Modélisations :")




    
