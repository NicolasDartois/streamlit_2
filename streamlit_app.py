import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import joblib


df=pd.read_csv("train.csv")

st.set_page_config(page_title="Projet Ciné", layout="centered") 

st.title("L'IA au service de la production cinématographique !")

st.sidebar.title("Sommaire")
pages=["Présentation du projet", "Collecte et Exploration des Données", "Analyse des Données (DataViz)", "Préparation les données - Preprocessing", "Présentation du modèle", "DEMONSTRATION"]
page=st.sidebar.radio("Aller vers", pages)


if page == pages[0] : 
    st.image('cinema.jpg')
    st.write("### Le contexte :")
    st.write("Le projet que nous présentons dans ce document est le fruit de notre propre initiative. Inspiré par une idée originale d'un des membres de notre groupe, ce projet s'est développé autour d'une ambition commune : transformer radicalement l'industrie du cinéma !")
    st.write("Traditionnellement, il est courant que les producteurs et les professionnels du cinéma fassent des paris amicaux sur le nombre de spectateurs qu'un film attirera à la fin de sa première semaine en salle. Cette pratique, à la fois ludique et ancrée dans les mœurs du secteur, a été le catalyseur de notre projet. Notre objectif est de mettre au point un modèle de machine learning capable de prédire avec la plus grande précision possible le nombre d'entrées qu'un film réalisera. Ce modèle s'appuiera sur des données préalablement collectées, alliant des critères quantitatifs et qualitatifs pour établir ses prévisions.")
    
    st.write("### L'objectif du projet :")
    st.write("L'objectif central de notre projet est de développer un outil accessible et convivial, permettant à tout utilisateur de prévoir le nombre de spectateurs d'un film à la fin de sa première semaine en salle. En renseignant des paramètres spécifiques de son choix, l'utilisateur pourra obtenir rapidement une estimation précise des entrées en salle.")
    st.write("### Pourquoi avoir choisi streamlit ?")
    st.write("Au-delà des fonctionnalités de base de cet applicatif, qui contribuent à rendre nos présentations plus dynamiques et visuellement impactantes, il est important de souligner que le choix de Streamlit pour présenter notre projet a également répondu à plusieurs objectifs pédagogiques. En effet, Streamlit est un outil de plus en plus prisé au sein des entreprises.")
    st.write("En intégrant Streamlit, nous avons non seulement amélioré l'interactivité et l'impact visuel de notre présentation, mais aussi enrichi notre expérience d'apprentissage avec une application technologique en pleine expansion. Cette démarche nous a permis de nous approprier efficacement cet outil moderne, en vue de l'utiliser plus tard dans nos futures carrières.")
    

    
    #st.image('199468.jpg')
    #st.dataframe(df.head())
    #st.write(df.shape)
    #st.dataframe(df.describe())

    #if st.checkbox("Afficher les NA") :
        #st.dataframe(df.isna().sum())

if page == pages[1] : 
    st.write("### Notre jeu de donnée lors du démarrage")
    st.write("Au cours de l'analyse initiale de notre jeu de données et à la lumière de nos premiers acquis en matière de formation, nous avons constaté que nos données étaient insuffisantes pour élaborer un modèle de machine learning robuste. Plusieurs défis se sont présentés : d'abord, notre jeu de données contenait un nombre excessif de valeurs manquantes. De plus, nous hésitions encore sur la variable cible à prédire, hésitant entre les revenus générés et les votes des spectateurs. À ce stade, nous n'avions pas accès à suffisament de données sur le marché francais.")       
    st.write("Par ailleurs, notre jeu de données couvrait le marché mondial, ce qui nous a rapidement motivé a nous focaliser sur le marché français, necessitant de trouver de nouvelles sources de données.")  
    st.write("Pour enrichir notre base, nous avons mis en place plusieurs actions :")
    st.write("‣ Nous avons contacté CBO BOX OFFICE, une société fournissant des données aux professionnels du cinéma. Malgré une proposition contractuelle exposant le contexte non lucratif et éducatif de notre projet, notre demande a été refusée.")
    st.write("‣ Nous avons exploré d'autres plateformes telles que KAGGLE pour trouver des bases de données robustes et adaptées à nos besoins, mais sans succès.")
    st.write("‣ Nous avons décidé de procéder au scraping de données sur des sites réputés bien administrés, tels qu'Allociné, IMDB PRO (gratuit le premier mois), et JPBOX Office. Avec le soutien de notre chef de cohorte, qui a débloqué un sprint complet dédié au web scraping, nous avons utilisé Beautiful Soup pour extraire et compléter notre jeu de données pour le marché français. Nous avons ainsi obtenu la liste des films sur Allociné avec leurs box-office et titres originaux, qui nous serviront plus tard comme clés d'indexation. Nous avons enrichi ces films avec des caractéristiques telles que la note des spectateurs, la note de la presse, les acteurs principaux, les réalisateurs, les scénaristes, les distributeurs, la date de sortie, la nationalité, le budget et le genre.")
    st.write("‣ Sur IMDB, nous avons récupéré un fichier global contenant les identifiants IMDB des films, leur durée et leurs titres originaux.")
    st.write("‣ Enfin, nous avons décidé de scraper sur IMDB des données permettant de construire un score de notoriété pour chaque acteur, réalisateur ou scénariste, en nous basant sur le Starmeter, le nombre de récompenses reçues, le nombre de films réalisés et la durée de leur carrière.")
    st.write("Ces démarches nous ont permis de bâtir un jeu de données plus complet et pertinent pour le développement de notre modèle prédictif du nombre d'entrées sur le marché français.")

if page == pages[2] : 
    st.write("### Modélisation")

    df = df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)
    y = df['Survived']
    X_cat = df[['Pclass', 'Sex',  'Embarked']]
    X_num = df[['Age', 'Fare', 'SibSp', 'Parch']]

    for col in X_cat.columns:
        X_cat[col] = X_cat[col].fillna(X_cat[col].mode()[0])
    for col in X_num.columns:
        X_num[col] = X_num[col].fillna(X_num[col].median())

    X_cat_scaled = pd.get_dummies(X_cat, columns=X_cat.columns)
    X = pd.concat([X_cat_scaled, X_num], axis = 1)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)
    
    scaler = StandardScaler()
    X_train[X_num.columns] = scaler.fit_transform(X_train[X_num.columns])
    X_test[X_num.columns] = scaler.transform(X_test[X_num.columns])

    def prediction(classifier):
        if classifier == 'Random Forest':
            clf = joblib.load("clf_rfc")
        elif classifier == 'SVC':
            clf = joblib.load("clf_svc")
        elif classifier == 'Logistic Regression':
            clf = joblib.load("clf_lr")
        clf.fit(X_train, y_train)
        return clf
    
    def scores(clf, choice):
        if choice == 'Accuracy':
            return clf.score(X_test, y_test)
        elif choice == 'Confusion matrix':
            return confusion_matrix(y_test, clf.predict(X_test))
    
    choix = ['Random Forest', 'SVC', 'Logistic Regression']
    option = st.selectbox('Choix du modèle', choix)
    st.write('Le modèle choisi est :', option)

    clf = prediction(option)
    import joblib
    joblib.dump(clf, "model")
    display = st.radio('Que souhaitez-vous montrer ?', ('Accuracy', 'Confusion matrix'))
    if display == 'Accuracy':
        st.write(scores(clf, display))
    elif display == 'Confusion matrix':
        st.dataframe(scores(clf, display))

if page == pages[3] :
    st.write("### Page test")
    code = '''

from concurrent.futures import ThreadPoolExecutor
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

# Démarrage du chronomètre pour calculer la durée d'exécution du script
start_time = time.time()

# Définition de la variable pour intervalle de progression
pourcent = 23

# Définition de la variable du nombre d'id dans l'url d'Allociné
total_film = 350000

# Définition de la fonction pour scraper les données d'Allociné
def allocine_scrap(i):
    global pourcent
    # Initialisation des variables à None
    titre = entree_france = cumul_france = recette_us = cumul_us = year = pays_test = pays_test_1 = pays_test_2 = None
    try:
        # Construction de l'URL pour chaque film basé sur son ID
        url = f'https://www.allocine.fr/film/fichefilm-{i}/box-office/'
        res = session.get(url, allow_redirects=True)

        # Print du % avec une intervalle de 24 tests
        pourcent += 1
        if pourcent == 24:
            print('Execution :', round((i/total_film)*100, 2), '%')
            pourcent = 0
        
        # Vérification du statut de la réponse, retourne des "0" si le code HTTP n'est pas 200 ou si l'URL a été redirigée
        if res.status_code != 200:
            return i, "0", "0", "0", "0", "0", "0"
        if res.url != url:
            return i, "0", "0", "0", "0", "0", "0"
        
        # Utilisation de BeautifulSoup pour parser le contenu HTML
        soup = BeautifulSoup(res.content, 'lxml')
        
        # Extraction des titres de sections pour identifier les sections France et US
        pays_test = soup.find_all('h2', class_= 'titlebar-title titlebar-title-md')
        pays_test_1 = pays_test[0].text.strip()
        
        if pays_test_1:
            pays_test_2 = pays_test[1].text.strip()
        
        # Extraction de l'année et du titre du film
        year = soup.find('span', class_=lambda x: x and 'first-col blue-link' in x)
        titre = soup.find('h1', class_= 'item')
        
        # Extraction des données du box office français si disponible
        if pays_test_1 and pays_test_1 == "Box Office France":
            tables = soup.find_all('table', class_='box-office-table table-3-cell responsive-table responsive-table-lined')
            table_france = tables[0]
            entree_france = table_france.find('td', class_='responsive-table-column second-col col-bg')
            cumul_france = table_france.find_all('td', class_='responsive-table-column third-col')[-1] 
            
            # Extraction des données du box office américain si box office français + box office américain sont disponibles
            if pays_test_2 and pays_test_2 == "Box Office US":
                table_us = tables[1]
                recette_us = table_us.find('td', class_='responsive-table-column second-col col-bg')
                cumul_us = table_us.find_all('td', class_='responsive-table-column third-col')[-1]
                
        # Extraction des données du box office américain si disponible et si il n'y a pas de box office francais
        elif pays_test_1 and pays_test_1 == "Box Office US":
            table_us = soup.find('table', class_='box-office-table table-3-cell responsive-table responsive-table-lined')
            recette_us = table_us.find('td', class_='responsive-table-column second-col col-bg')
            cumul_us = table_us.find_all('td', class_='responsive-table-column third-col')[-1]
    
    # Retourne des "0" en cas d'exception (Pas de box office par exemple)
    except requests.exceptions.RequestException:
        return i, "0", "0", "0", "0", "0", "0"
    
    # Retourne les données extraites ou des "0" si les données ne sont pas disponibles
    return (
        i,
        titre.text.strip()[:-13] if titre else "0",
        entree_france.text.strip() if entree_france else "0",
        cumul_france.text.strip() if cumul_france else "0",
        recette_us.text.strip() if recette_us else "0",
        cumul_us.text.strip() if cumul_us else "0",
        year.text.strip()[-4:] if year else "0"
    )

# Initialisation d'un DataFrame pour stocker les données extraites
df = pd.DataFrame(columns=['ID', 'titre', 'premiere_semaine_france', 'cumul_france', 'premiere_semaine_US', 'cumul_US', 'year'])
session = requests.Session()

# Utilisation d'un ThreadPoolExecutor pour exécuter les scrapings en parallèle et utiliser les differents coeurs logique du PC.
with ThreadPoolExecutor(max_workers=6) as executor:
    # Soumission des tâches de scraping pour chaque ID de film entre 1 et la variable total_film
    tests = [executor.submit(allocine_scrap, i) for i in range(1, total_film)]
    for test in tests:
        # Récupération des résultats et ajout au DataFrame si le titre est différent de "0"
        i, titre, entree_france, cumul_france, recette_us, cumul_us, year = test.result()
        if titre != "0":
            df.loc[i] = [i, titre, entree_france, cumul_france, recette_us, cumul_us, year]

# Arrêt du chronomètre et affichage de la durée d'exécution
end_time = time.time()
execution_time = end_time - start_time
print(f"Le script a pris {execution_time} secondes pour s'exécuter.")

# Sauvegarde des résultats dans un fichier CSV
df.to_csv('allocine_BO.csv', index=False)

# Affichage du DataFrame final
display(df)    
    '''
    st.code(code, language='python')
