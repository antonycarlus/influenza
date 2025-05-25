import streamlit as st
import pandas as pd


tbsrag = pd.read_json('http://127.0.0.1:5000/srag')
tblocal = pd.read_json('http://127.0.0.1:5000/local')


st.write("testando painel influenza.")


st.write(tbsrag)

st.write(tblocal)
