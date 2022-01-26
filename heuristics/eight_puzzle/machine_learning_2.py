from eight_puzzle import EightPuzzle, generate_puzzle
from collections import deque
from functools import reduce
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import GradientBoostingRegressor
from node.node import Node
from solution import print_solution
import pprint
import random
import heapq
import numpy as np
import pandas as pd

def to_digit(t):
    # Adapted from: https://stackoverflow.com/a/10062711
    return reduce(lambda rst, d: rst * 10 + d, t)

def train_model():
    ds = pd.read_csv('data/eight-puzzle/method_2.csv')
    X = [[row[0], row[1], row[2]] for row in ds.values.tolist()]
    Y = ds['ans'].tolist()
    model = GradientBoostingRegressor(n_estimators=1000)
    model.fit(X, Y)
    return model
MODEL = train_model()

def machine_learning_2(puzzle):
    state = puzzle.get_state()
    reshaped = np.reshape(state, (3, 3))
    reshaped2 = [[to_digit(row) for row in reshaped]]
    return MODEL.predict(reshaped2)[0]
