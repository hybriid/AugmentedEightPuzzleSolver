from queues import PriorityQueue
from reporter import Reporter
from search import best_first_search
from heuristics.fifteen_puzzle.machine_learning import machine_learning

def machine_learning_search(puzzle):
    return best_first_search(puzzle, PriorityQueue(), machine_learning, Reporter('MLS'))
