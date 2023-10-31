import streamlit as st 
import pandas as pd
import plotly.express as px 
from dotenv import load_dotenv
from os import getenv

load_dotenv()
sql_url = getenv('SQL_URL')

st.title('Visualizations')
st.write('Here, you can visualize some features from our data! Try taking a look at the episodes and number of characters in each!')

vis_to_use = ['scatterplot', 'histogram', 'bar chart']
vis = st.selectbox('What type of visualization would you like to choose?', options=vis_to_use)

frame = st.selectbox('Which table would you like to view?',options=['episodes', 'locations', 'characters'])
sql_query = f'''SELECT * FROM {frame}'''
df = pd.read_sql_query(sql_query, con=sql_url)

if vis == 'scatterplot':
    x = st.selectbox('Select the column for the X-Axis:', options = list(df.columns))
    y = st.selectbox('Select the column for the Y-Axis:', options = list(df.columns))
    if x and y:
        try:
            st.plotly_chart(px.scatter(df, x, y))
        except BaseException:
            st.error('Error visualizing that selection of columns!')
            
elif vis == 'bar chart':
    x = st.selectbox('Select the column for the X-Axis:', options = list(df.columns))
    y = st.selectbox('Select the column for the Y-Axis:', options = list(df.columns))
    if x and y:
        try:
            st.plotly_chart(px.bar(df, x, y))
        except BaseException:
            st.error('Error visualizing that selection of columns!')
    
elif vis == 'histogram':
    x = st.selectbox('Select the column for the X-Axis:', options = list(df.columns))
    if x:
        try:
            st.plotly_chart(px.histogram(df, x))
        except BaseException:
            st.error('Error visualizing that selection of columns!')