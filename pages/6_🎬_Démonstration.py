import streamlit as st
import joblib as jl

clf = jl.load("models/GB.joblib")
df = pd.read_csv('data/score_acteur.csv')
st.dataframe(df)



