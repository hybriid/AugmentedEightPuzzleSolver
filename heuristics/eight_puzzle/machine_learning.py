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
import pandas as pd
import pprint
import random
import heapq

def to_digit(t):
    # Adapted from: https://stackoverflow.com/a/10062711
    return reduce(lambda rst, d: rst * 10 + d, t)

def train_model():
    ds = pd.read_csv('data/eight-puzzle/method_1.csv')
    X = [[row[0]] for row in ds.values.tolist()]
    Y = ds['ans'].tolist()
    model = GradientBoostingRegressor(n_estimators=1000)
    model.fit(X, Y)
    return model
MODEL = train_model()

def machine_learning(puzzle):
    state = puzzle.get_state()
    digit = to_digit(state)
    return MODEL.predict([[digit]])
