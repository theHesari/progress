import pandas as pd
from sklearn.model_selection import train_test_split


# Load the dataset
file_path = 'data/netflix_titles.csv'
netflix_df = pd.read_csv(file_path)

# Filter out rows with NaN values in 'rating', 'director', or 'cast'
netflix_df = netflix_df.dropna(subset=['rating', 'director', 'cast'])
df = netflix_df[['show_id', 'director', 'cast', 'rating']]
df.set_index('show_id', inplace=True)


def clean_data(dataframe, feature):
    dataframe[feature] = dataframe[feature].apply(lambda x: [y.strip().lower() for y in x.split(',')] if ',' in x else [x])
    return dataframe


df = clean_data(df, 'director').explode('director')
df = clean_data(df, 'cast')


X = df.drop('rating', axis=1)
y = df['rating']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
