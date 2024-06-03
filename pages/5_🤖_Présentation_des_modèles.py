import streamlit as st
import pandas as pd
from include.css_and_credit import css_and_credit
st.set_page_config(page_title="Exploitation cinématographique", page_icon='🎬', layout="wide")

css_and_credit()

st.header("🤖 Présentation des modèles")

st.markdown("""
<div class ="centered-content"><div class="box"><h3>Choix du type de modèle :</h3>
    <p>Le choix d'utiliser un modèle de régression plutôt qu'un modèle de classification dans notre projet de prédiction du nombre d'entrées en première semaine en France repose sur la nature continue et quantitative de notre variable cible.</p>
    <p>En effet, le nombre d'entrées en première semaine est une mesure numérique qui peut prendre une gamme de valeurs continues, reflétant la performance d'un film dans les salles de cinéma. Ainsi, plutôt que de catégoriser les films en groupes prédéfinis, notre objectif est de prédire avec précision le nombre réel d'entrées qu'un film réalisera.</p>
    <p>Nous avons donc décidé de tester notre jeu de données sur plusieurs modèles différents :</p>
</div></div>
""", unsafe_allow_html=True)

df_modele = pd.read_csv('data/score.csv')

st.markdown(f"""
        <div class ="centered-content">
            <div class="box2">
                <label for="5" style="cursor: pointer;"><h4>---------- Modèles basiques : ----------</h4></label>
                <input type="checkbox" id="5" class="hidden-checkbox">
                <img src="https://github.com/NicolasDartois/streamlit_2/blob/main/images/Modeles_basiques.png?raw=true" id="H5" class="hiddenText"/>
            </div>
        </div>
        <div class ="centered-content">
            <div class="box2">
                <label for="6" style="cursor: pointer;"><h4>---------- Modèles complexes : ----------</h4></label>
                <input type="checkbox" id="6" class="hidden-checkbox">
                <img src="https://github.com/NicolasDartois/streamlit_2/blob/main/images/Modeles_complexes.png?raw=true" id="6" class="hiddenText"/>
            </div>
        </div>
""", unsafe_allow_html=True)

st.markdown("""
<div class ="centered-content"><div class="box"><h3>Modèle retenu :</h3>
    <p>Nous avons d'abord testé trois modèles simples différents (RandomForest, Régression linéaire, DecisionTree). Nous avons constaté que le modèle random forest était le plus prometteur (au niveau de la MAE et du score R2). Nous avons donc décidé de tester deux autres modèles similaires au random forest, le gradient boosting et le XGBoost, en utilisant GridSearchCV et RandomizedSearchCV pour trouver les meilleurs hyperparamètres.</p>
    <p>Nous avons retenu le gradient boosting avec les meilleurs hyperparamètres car c'est le modèle avec lequel nous avons obtenu les meilleures performances.</p>
</div></div>
""", unsafe_allow_html=True)

st.markdown("""
<div class ="centered-content"><div class="box"><h3>Modèle retenu :</h3>
    <p>Nous avons d'abord testé trois modèles simples différents (RandomForest, Régression linéaire, DecisionTree). Nous avons constaté que le modèle random forest était le plus prometteur (au niveau de la MAE et du score R2). Nous avons donc décidé de tester deux autres modèles similaires au random forest, le gradient boosting et le XGBoost, en utilisant GridSearchCV et RandomizedSearchCV pour trouver les meilleurs hyperparamètres.</p>
    <p>Nous avons retenu le gradient boosting avec les meilleurs hyperparamètres car c'est le modèle avec lequel nous avons obtenu les meilleures performances.</p>
    <img src="https://github.com/NicolasDartois/streamlit_2/blob/main/images/Modeles_complexes.png?raw=true" id="6" class="hiddenText"/>
</div></div>
""", unsafe_allow_html=True)








    
