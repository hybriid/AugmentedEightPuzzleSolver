from fifteen_puzzle import FifteenPuzzle, generate_puzzle
from collections import deque
from functools import reduce
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.cluster import KMeans
from sklearn.svm import SVR
from sklearn.ensemble import GradientBoostingRegressor
from search import best_first_search
from queues import PriorityQueue
from node.node import Node
from solution import print_solution
from fifteen_puzzle import generate_puzzle
from heuristics.manhattan_distance import manhattan_distance_fifteen
from reporter import Reporter
from math import floor
import pprint
import random
import heapq
import numpy as np
import pandas as pd

def to_digit(t):
    # Adapted from: https://stackoverflow.com/a/10062711
    as_string = ''.join([str(i) for i in t])
    return int(as_string)


def train_model():
    ds = pd.read_csv('data/fifteen-puzzle/method_2.csv', index_col=False).drop_duplicates()
    X = [[row[1], row[2], row[3], row[4]] for row in ds.values.tolist()]
    # print(X[0])
    Y = ds['ans'].tolist()
    model = GradientBoostingRegressor(n_estimators=1000)
    model.fit(X, Y)
    return model
MODEL = train_model()

def machine_learning_2(puzzle):
    state = puzzle.get_state()
    reshaped = np.reshape(state, (4, 4))
    reshaped2 = [[to_digit(row) for row in reshaped]]
    return floor(MODEL.predict(reshaped2)[0])
