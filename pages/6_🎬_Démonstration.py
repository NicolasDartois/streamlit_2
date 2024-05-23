import streamlit as st
import joblib as jl
import pandas as pd
from include.css_and_credit import css_and_credit

css_and_credit()

st.header("🎬Démonstration🎬")

clf = jl.load("models/GB.joblib")
df = pd.read_csv('data/score_acteur.csv')
st.dataframe(df)



