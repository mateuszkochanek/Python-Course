import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
from sklearn.preprocessing import normalize
from scipy.sparse import csr_matrix

iter_csv = pd.read_csv('ratings.csv', iterator=True, chunksize=1000)
data_rating = pd.concat([chunk for chunk in iter_csv])
iter_csv = pd.read_csv('movies.csv', iterator=True, chunksize=1000)
data_movie = pd.concat([chunk for chunk in iter_csv])

max_movie_id = (data_movie.max(axis=0))[0]
userId_values = data_rating[["userId"]].values.ravel()
userIds = pd.unique(userId_values)
movieTitles = data_movie[["title", "movieId"]]

rating_matrix = np.zeros((len(userIds), max_movie_id+1))
i = 0
for id in userIds:
    for row in data_rating[(data_rating['userId'] == id)].itertuples():
        rating_matrix[i, row.movieId] = row.rating
    i+=1
rating_matrix = csr_matrix(rating_matrix)
rating_matrix_norm = normalize(rating_matrix, norm='l1', axis=0)

my_ratings = np.zeros((max_movie_id+1,1))
my_ratings[2571] = 5      # 2571 - Matrix
my_ratings[32] = 4        # 32 - Twelve Monkeys
my_ratings[260] = 5       # 260 - Star Wars IV
my_ratings[1097] = 4
my_ratings = csr_matrix(my_ratings)
my_ratings_norm = normalize(my_ratings, norm='l1', axis=0)

our_profile = rating_matrix_norm.dot(my_ratings_norm)
our_profile_norm = normalize(our_profile, norm='l1', axis=0)

result = rating_matrix_norm.T.dot(our_profile_norm)
result = result.todense()
answer = np.array([[row[0], ""] for i, row in enumerate(result)], dtype="object")
for row in movieTitles.itertuples():
    answer[row.movieId][1] = row.title
answer = answer[answer[:, 0].argsort()][::-1]

print(answer[:10])
