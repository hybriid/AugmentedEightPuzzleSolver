from queues import FIFOQueue
from heuristics.constant import constant
from reporter import Reporter
from .best_first_search import best_first_search

def breadth_first_search(puzzle):
    return best_first_search(puzzle, FIFOQueue(), constant, Reporter('BFS'))