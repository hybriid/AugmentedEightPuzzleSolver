from eight_puzzle import EightPuzzle, generate_puzzle
from collections import deque
from functools import reduce
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from node.node import Node
from solution import print_solution
from joblib import load
import pprint
import random
import heapq
import numpy as np
import pandas as pd

def to_digit(t):
    # Adapted from: https://stackoverflow.com/a/10062711
    return reduce(lambda rst, d: rst * 10 + d, t)

def machine_learning_2_import(puzzle):
    state = puzzle.get_state()
    reshaped = np.reshape(state, (3, 3))
    reshaped2 = [[to_digit(row) for row in reshaped]]
    model = load('models/imported/machine_learning2.joblib')
    return model.predict(reshaped2)[0]
