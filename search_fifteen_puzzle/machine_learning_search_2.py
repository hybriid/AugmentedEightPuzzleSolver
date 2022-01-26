from queues import PriorityQueue
from reporter import Reporter
from search import best_first_search
from heuristics.fifteen_puzzle.machine_learning_2 import machine_learning_2

def machine_learning_search_2(puzzle):
    return best_first_search(puzzle, PriorityQueue(), machine_learning_2, Reporter('MLS2'))
