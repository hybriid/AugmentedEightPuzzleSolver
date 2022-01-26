from queues import PriorityQueue
from heuristics.eight_puzzle.machine_learning import machine_learning
from reporter import Reporter
from .best_first_search import best_first_search

def machine_learning_search(puzzle, h=machine_learning):
    return best_first_search(puzzle, PriorityQueue(), h, Reporter('MLS'))
