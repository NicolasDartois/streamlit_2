import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

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




    
