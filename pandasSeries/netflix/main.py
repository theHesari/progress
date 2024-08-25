import pandas as pd
from itertools import combinations

# Load the dataset
file_path = 'data/netflix_titles.csv'
netflix_df = pd.read_csv(file_path)

# Filter the data for programs released after 1970
filtered_df = netflix_df[netflix_df['release_year'] > 1970].copy()

# Drop rows where 'cast' is NaN
filtered_df = filtered_df.dropna(subset=['cast'])


# Function to extract actor pairs
def extract_pairs(cast_list):
    actors = [actor.strip() for actor in cast_list.split(',')]
    return list(combinations(sorted(actors), 2))


# Apply the function to create a list of pairs
filtered_df['actor_pairs'] = filtered_df['cast'].apply(extract_pairs)

# Explode the pairs into separate rows for counting
pairs_exploded = filtered_df.explode('actor_pairs')

# Count the frequency of each actor pair
pair_counts = pairs_exploded['actor_pairs'].value_counts().reset_index()
pair_counts.columns = ['Actor Pair', 'Count']

# Save the top 10 most frequent actor pairs as csv
pair_counts.head(10).to_csv('outputs/netflix_actor_pairs_frequency.csv', index=False)
