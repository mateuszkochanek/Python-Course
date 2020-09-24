import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
#np.set_printoptions(threshold=sys.maxsize)

iter_csv = pd.read_csv('ratings.csv', iterator=True, chunksize=1000)
data_rating = pd.concat([chunk[chunk['movieId'] < 10000] for chunk in iter_csv])
iter_csv = pd.read_csv('movies.csv', iterator=True, chunksize=1000)
data_movie = pd.concat([chunk[chunk['movieId'] < 10000] for chunk in iter_csv])

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
rating_matrix_norm = np.nan_to_num(rating_matrix/np.linalg.norm(rating_matrix, axis=0)) #znormalizowana macież ocen
my_ratings = np.zeros((9019,1))
my_ratings[2571] = 5      # 2571 - Matrix
my_ratings[32] = 4        # 32 - Twelve Monkeys
my_ratings[260] = 5       # 260 - Star Wars IV
my_ratings[1097] = 4
my_ratings_norm = np.nan_to_num(my_ratings/np.linalg.norm(my_ratings)) #znormalizowany profli filmowy
our_profile = np.dot(rating_matrix_norm, my_ratings_norm)
our_profile_norm = our_profile/np.linalg.norm(our_profile)
our_profile_norm = np.nan_to_num(our_profile_norm)

our_profile_norm = np.nan_to_num(our_profile_norm/np.linalg.norm(our_profile_norm))
result = np.nan_to_num(np.dot(rating_matrix_norm.T, our_profile_norm))

answer = np.array([[row[0], ""] for i, row in enumerate(result)], dtype="object")
for row in movieTitles.itertuples():
    answer[row.movieId][1] = row.title
answer = answer[answer[:, 0].argsort()][::-1]


print(answer[:10])