import streamlit as st

st.title('Streamlit Workshop: Bonfire 129')
st.write(
    '''Our second Streamlit app we will build together! Our app will consist of two pages:
    1. Visualization Page
    2. User Query Page
    '''
    )

st.subheader('Visualizations')
st.write(
    '''
    On this page, we will create visualizations for a user to view.
    This will allow a user to view columns of our dataset through multiple visualization options.
    All visualizations will be created using Plotly.Express!
    '''
    )

st.subheader('User Query')
st.write(
    '''
    This page will allow users to directly query our ElephantSQL instance.
    This will return data back to our users matching whatever they decide to 
    try and query.
    '''
)
