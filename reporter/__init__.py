from solution import get_solution
import pprint

pp = pprint.PrettyPrinter(indent=4)
results = {}

class Reporter:
    def __init__(self, algo_name):
        self.name = algo_name
        results[self.name] = {'expansions': 0, 'solution_len': 0, 'nodes_stored': 0, 'num_times_heuristic_inconsistent': 0}
    
    def increment_expansion(self):
        results[self.name]['expansions'] += 1

    def increment_stored(self):
        results[self.name]['nodes_stored'] += 1

    def reset_expansion(self):
        results[self.name]['expansions'] = 0

    def reset_stored(self):
        results[self.name]['nodes_stored'] = 0

    def set_solution_length(self, node):
        results[self.name]['solution_len'] = len(get_solution(node))

    def increment_if_h_inconsistent(self, child, parent, h):
        if abs(h(child.state) - h(parent.state)) > 1:
            results[self.name]['num_times_heuristic_inconsistent'] += 1

    def get_algorithm_stats(algo_name):
        return results[algo_name]

    @staticmethod
    def print_results():
        pp.pprint(results)
