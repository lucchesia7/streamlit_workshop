import ramapi
import pandas as pd
from dotenv import load_dotenv
from os import getenv
from sklearn.pipeline import make_pipeline
from category_encoders import OrdinalEncoder
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from pathlib import Path
import pickle

folder_dir = f'{Path(__file__).parents[0]}\\data'
# Create character dataframe
char_df = pd.DataFrame(ramapi.Character.get_all()['results'])
char_df.head()

# Fix origin and location columns
char_df['origin'] = [char_df['origin'][x]['name'] for x in range(len(char_df))]
char_df['location'] = [char_df['location'][x]['name'] for x in range(len(char_df))]
char_df.head()

# Create locations dataframe
loc_df = pd.DataFrame(ramapi.Location.get_all()['results'])
loc_df.head()

# Change residents column to follow SQL atomicity needs
loc_df['num_residents_in_location'] = [len(x) for x in loc_df['residents']]
loc_df['residents'] = loc_df['residents'].astype(str)
loc_df.head()

# Create episodes dataframe
ep_df = pd.DataFrame(ramapi.Episode.get_all()['results'])
ep_df.head()

# Feature engineer num_char column
ep_df['num_characters_in_episode'] = [len(x) for x in ep_df['characters']]
# Change characters column to follow SQL atomicity needs
ep_df['characters'] = ep_df['characters'].astype(str)
ep_df.head(30)


# Upload data to SQL instance
load_dotenv()
sql_url = getenv('SQL_URL')

loc_df.to_sql('locations', con=sql_url, if_exists='replace')
char_df.to_sql('characters', con=sql_url, if_exists='replace')
ep_df.to_sql('episodes', con=sql_url, if_exists='replace')

# Create X,y splits
X = loc_df['type']
y = loc_df['num_residents_in_location']

X_train, X_test, y_train, y_test = train_test_split(X,y, train_size=.8)

# Create a basic model pipeline:
lm = make_pipeline(
    OrdinalEncoder(),
    SimpleImputer(),
    LinearRegression()
)

# Fit pipeline
lm.fit(X_train, y_train)

# Dump model
pickle.dump(lm, open(f'{folder_dir}\\model.pk', 'wb'))