from search import best_first_search
from heuristics.manhattan_distance import manhattan_distance_fifteen
from queues import PriorityQueue
from reporter import Reporter

def a_star_search(puzzle):
    return best_first_search(puzzle, PriorityQueue(), manhattan_distance_fifteen, Reporter('A*'))
