from queues import PriorityQueue
from heuristics.eight_puzzle.machine_learning_2 import machine_learning_2
from reporter import Reporter
from .best_first_search import best_first_search

def machine_learning_search_2(puzzle, h=machine_learning_2):
    return best_first_search(puzzle, PriorityQueue(), h, Reporter('MLS2'))
