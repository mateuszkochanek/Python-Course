import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
np.set_printoptions(threshold=sys.maxsize)

toy_story_userId_rating = list()
data = pd.read_csv("../zad2/ratings.csv")
for row in data[data['movieId'] == 1].itertuples():
    toy_story_userId_rating.append((row.userId, row.rating))
toy_story_ratings = np.array([rate for id, rate in toy_story_userId_rating])

def create_rating_matrix(data,y,m): # m-(1,2,..,m) id filmow, y-id uzytkownikow, data-data csv
    rating_matrix = np.zeros((215, m))
    i = 0
    for id,rating in y:
        for row in data[(data['userId'] == id) & (data['movieId'] <= m) & (data['movieId'] > 1)].itertuples():
            rating_matrix[i, row.movieId - 2] = row.rating
        i+=1
    return rating_matrix

def calculalte_error(x_matrix,y_vector):
    results = list()
    errors = list()
    x_matrix = [np.append(row, 1, axis=None) for row in x_matrix]
    x_matrix = np.array(x_matrix)
    parameters = np.linalg.lstsq(x_matrix,y_vector,rcond=None)[0]
    for row in x_matrix:
        sum = 0
        for xi, p in zip(row, parameters):
            sum += xi*p
        results.append(sum)
    errors = [ value-result for result, value in zip(results, y_vector)]
    print(errors)
    plt.plot(range(1,216), y_vector, 'r', label='Original data', markersize=5)
    plt.plot(range(1,216), results, 'o', label='Fitted line')
    plt.legend()
    plt.show()

def zad1a_10():
    m10 = create_rating_matrix(data, toy_story_userId_rating, 10)
    calculalte_error(m10,toy_story_ratings)

def zad1a_1000():
    m1000 = create_rating_matrix(data, toy_story_userId_rating, 1000)
    calculalte_error(m1000,toy_story_ratings)

def zad1a_10000():
    m10000 = create_rating_matrix(data, toy_story_userId_rating, 10000)
    calculalte_error(m10000,toy_story_ratings)


