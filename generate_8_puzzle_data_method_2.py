import concurrent.futures
import time
import pandas as pd
import numpy as np

from functools import reduce
from search import best_first_search
from heuristics.manhattan_distance import manhattan_distance
from queues import PriorityQueue
from reporter import Reporter
from eight_puzzle import generate_puzzle

def to_digit(t):
    # Adapted from: https://stackoverflow.com/a/10062711
    as_string = ''.join([str(i) for i in t])
    return int(as_string)


def generate_data_set_2(solved_puzzles):
    print('Generating DS')
    data_set = {'col1': [123], 'col2': [456], 'col3': [780], 'ans': [0]}

    for node in solved_puzzles:
        g_cost, curr_node = 0, node
        while curr_node is not None:
            new_state = np.reshape(curr_node.state.get_state(), (3, 3))
            curr_node.state.print_state()
            data_set['col1'].append(to_digit(new_state[0]))
            data_set['col2'].append(to_digit(new_state[1]))
            data_set['col3'].append(to_digit(new_state[2]))
            data_set['ans'].append(g_cost)

            g_cost += 1
            curr_node = curr_node.parent
        print('DONE')

    print('Done generating data')
    df = pd.DataFrame(data=data_set)
    df.to_csv('data/eight-puzzle/method_2.csv', index=False)
    return df
    
def solve_puzzle(puzzle):
    x =  best_first_search(puzzle, PriorityQueue(), manhattan_distance, Reporter('Placeholder'))
    return x

if __name__ == '__main__':
    print('Solving puzzles')
    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
        puzzles = [generate_puzzle() for _ in range(1000)]
        results = executor.map(solve_puzzle, puzzles)

        print(generate_data_set_2(list(results)))
        for result in results:
            print(result.state.get_state())
