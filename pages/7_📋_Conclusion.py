import streamlit as st
from include.css_and_credit import css_and_credit
st.set_page_config(page_title="Exploitation cinématographique", page_icon='🎬', layout="wide")

css_and_credit()
st.header("📋 Conclusion")

st.markdown("""<div class ="centered-content"><div class="box"><h3>Notre jeu de donnée lors du démarrage et son évolution</h3>
    <p>Malgré les défis rencontrés, notre projet de prédiction du nombre d’entrées en première semaine dans les cinémas français a abouti à des résultats prometteurs. 
        Nous avons démontré qu’il était possible de développer un modèle prédictif en utilisant des techniques avancées d’analyse de données et de machine learning.</p>
    <br>
    <p>Pour aller plus loin, plusieurs pistes pourront être explorées: </p>
    <p>• L’expansion de notre modèle pour inclure un plus large éventail de variables pourrait améliorer sa capacité prédictive. Par exemple, l’utilisation de techniques de text mining pour analyser les critiques de films pourraient fournir des informations supplémentaires précieuses.</p>
    <p>• Comme évoqué plus haut, l’intégration de données sur les budgets marketing des films pourraient bénéficier au modèle.</p>
    <p>• L’ajout de données temporelles cohérentes par rapport à la date de sortie des films (évaluation de la notoriété des acteurs au moment de la sortie de chacun de ses films…) permettrait d’affiner notre scoring.</p>
    <p>• Les tendances culturelles, bien que difficiles à transformer en data, peuvent parfois influer sur un succès ou un échec.</p>
    <p>• L’actualisation des budgets en fonction de l’érosion monétaire permettrait d’obtenir des budgets plus précis.</p>
    <p>NB: nous aurions pu avoir accès à des données plus riches, mais cela impliquait des abonnements payants, ce qui était contraire à l’esprit du projet.</p>
    <img src= class="https://github.com/NicolasDartois/streamlit_2/blob/main/images/end.jpg?raw=true"/>""", unsafe_allow_html=True)
