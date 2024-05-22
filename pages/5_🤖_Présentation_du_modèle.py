import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

for i in range(25):
    st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.subheader("🎥oct23_cda_exploitation-cinématographique🎥")
st.sidebar.markdown("_____________________")
st.sidebar.markdown("Manon FOUQUET")
st.sidebar.markdown("Sylvain BRAIZET")
st.sidebar.markdown("Nicolas DARTOIS")

st.header("🤖Présentation du modèle🤖")

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
df_modele = pd.DataFrame(columns=["modèle", "r2", "MAE"])

for i in choix:
    clf = prediction(i)
    r2 = scores(clf, 'R²')
    MAE = scores(clf, 'MAE')
    df_modele = df_modele.append({'modèle': i, 'r2': r2, 'MAE': MAE}, ignore_index=True)

st.dataframe(df_modele)
    
    




test = "bien"
st.markdown(f"""<p>{test}</p>""", unsafe_allow_html=True)






    
