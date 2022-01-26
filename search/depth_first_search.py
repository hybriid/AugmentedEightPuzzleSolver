from queues import FILOQueue
from heuristics.constant import constant
from reporter import Reporter
from .best_first_search import best_first_search

def depth_first_search(puzzle):
    return best_first_search(puzzle, FILOQueue(), constant, Reporter('DFS'))