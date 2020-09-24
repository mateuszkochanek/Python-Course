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

def calculalte_prediction(x_matrix_training,y_vector_training,x_matrix_test,y_vector_test):
    results = list()
    errors = list()
    x_matrix_training = [np.append(row, 1, axis=None) for row in x_matrix_training]
    x_matrix_test = [np.append(row, 1, axis=None) for row in x_matrix_test]
    x_matrix_training = np.array(x_matrix_training)
    parameters = np.linalg.lstsq(x_matrix_training, y_vector_training, rcond=None)[0]
    for row in x_matrix_test:
        sum = 0
        for xi, p in zip(row, parameters):
            sum += xi*p
        results.append(sum)
    errors = [ value-result for result, value in zip(results, y_vector_test)]
    print(errors)
    plt.plot(range(1,16), y_vector_test, 'r', label='Original data', markersize=5)
    plt.plot(range(1,16), results, 'o', label='Fitted line')
    plt.legend()
    plt.show()

def zad1b_10():
    m10 = create_rating_matrix(data, toy_story_userId_rating, 10)
    m10_training = m10[:200]
    m10_test = m10[200:]
    toy_story_ratings_training = toy_story_ratings[:200]
    toy_story_ratings_test = toy_story_ratings[200:]
    calculalte_prediction(m10_training,toy_story_ratings_training,m10_test,toy_story_ratings_test)

def zad1b_1000():
    m1000 = create_rating_matrix(data, toy_story_userId_rating, 1000)
    m1000_training = m1000[:200]
    m1000_test = m1000[200:]
    toy_story_ratings_training = toy_story_ratings[:200]
    toy_story_ratings_test = toy_story_ratings[200:]
    calculalte_prediction(m1000_training, toy_story_ratings_training, m1000_test, toy_story_ratings_test)

def zad1b_10000():
    m10000 = create_rating_matrix(data, toy_story_userId_rating, 10000)
    m10000_training = m10000[:200]
    m10000_test = m10000[200:]
    toy_story_ratings_training = toy_story_ratings[:200]
    toy_story_ratings_test = toy_story_ratings[200:]
    calculalte_prediction(m10000_training, toy_story_ratings_training, m10000_test, toy_story_ratings_test)

def zad1b(c):
    m = create_rating_matrix(data, toy_story_userId_rating, c)
    m_training = m[:200]
    m_test = m[200:]
    toy_story_ratings_training = toy_story_ratings[:200]
    toy_story_ratings_test = toy_story_ratings[200:]
    calculalte_prediction(m_training, toy_story_ratings_training, m_test, toy_story_ratings_test)


zad1b(500)