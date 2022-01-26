from queues import PriorityQueue, FIFOQueue
from heuristics.manhattan_distance import manhattan_distance
from reporter import Reporter
from .best_first_search import best_first_search

def a_star_search(puzzle):
    return best_first_search(puzzle, PriorityQueue(), manhattan_distance, Reporter('A*'))
