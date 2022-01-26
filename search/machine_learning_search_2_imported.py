from queues import PriorityQueue
from heuristics.eight_puzzle.machine_learning_2_import import machine_learning_2_import
from reporter import Reporter
from .best_first_search import best_first_search

def machine_learning_search_2_imported(puzzle, h=machine_learning_2_import):
    return best_first_search(puzzle, PriorityQueue(), h, Reporter('MLS2_imported'))
