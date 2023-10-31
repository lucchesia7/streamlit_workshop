import streamlit as st 
from dotenv import load_dotenv
from os import getenv
import pandas as pd

st.header('Date Query Page')
load_dotenv()
sql_url = getenv('SQL_URL')


date = st.date_input('Pick a Date to View!')
date = str(date)
table = st.selectbox(label='Choose which table to query', options=['characters', 'episodes', 'locations'])


sql_query = f"""SELECT * FROM {table} WHERE air_date = '{date}'"""
if st.button('Submit Date and Table'):
    if len(pd.read_sql_query(sql_query, sql_url)) >=1:
        st.dataframe(pd.read_sql_query(sql_query, sql_url))
    else:
        st.error('The date selected did not return any information. Try another date instead!')
