import streamlit as st
from joblib import load

clf = joblib.load("models/GB.joblib")
df = pd.read_csv('data/score_acteur.csv')
st.dataframe(df)



