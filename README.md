# Streamlit Workshop

## Overview:
This application will utilize the [Rick and Morty API](https://rickandmortyapi.com/) to create visualizations and allow users to query a database of the information from our API.


In order to run this application, you will need to run the following code:

```
python3.11 -m venv venv
```
On Mac:
```
source venv/bin/activate
```

On PC:
```
cd venv/Scripts
activate
```

To install the requirements in your environment, you will need to run the following code in the directory where the file is located:

```
pip install -r requirements.txt
```

The application has two main pages we will be building; ***Visualizations and Query***.

### Visualizations
This page will utilize ElephantSQL and Plotly Express to return visualizations to a user. The user will be able to choose which table they want to view as well as what columns and chart they want to see.

### Query
This page will utilize Elephant SQL to query information from our database to the user, using a date range and table selections.