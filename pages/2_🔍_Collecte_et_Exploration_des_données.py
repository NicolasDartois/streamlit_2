import streamlit as st

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
