from eight_puzzle import EightPuzzle, generate_puzzle
from collections import deque
from functools import reduce
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from node.node import Node
from solution import print_solution
import pprint
import random
import heapq

def to_digit(t):
    # Adapted from: https://stackoverflow.com/a/10062711
    return reduce(lambda rst, d: rst * 10 + d, t)

def generate_data_set(n):
    data_set = {123456780: 0}
    queue = deque()
    explored = set()
    queue.append(EightPuzzle((1, 2, 3, 4, 5, 6, 7, 8, 0)))
    g_val = 1
    for i in range(n):
        curr = queue.popleft()
        for direction in curr.get_legal_moves():
            child = curr.move(direction)
            if child.get_state() not in explored:
                data_set[to_digit(child.get_state())] = g_val
                queue.append(child)
                explored.add(child.get_state())
        g_val += 1
    return [[[key] for key, val in data_set.items()], [val for key,val in data_set.items()]]

def train_model():
    X, Y = generate_data_set(100000)
    model = RandomForestRegressor(5)
    model.fit(X, Y)
    return model
MODEL = train_model()

def machine_learning(puzzle):
    state = puzzle.get_state()
    digit = to_digit(state)
    return MODEL.predict([[digit]])
