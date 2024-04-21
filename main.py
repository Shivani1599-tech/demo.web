import streamlit as st
import pandas as pd
st.title("Bioinformatics tools and software list")

dataset = pd.read_csv("titanic_submission.csv")
st.dataframe (dataset)


