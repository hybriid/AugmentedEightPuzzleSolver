from search_fifteen_puzzle import a_star_search, machine_learning_search ,machine_learning_search_2
from reporter import Reporter
from fifteen_puzzle import generate_puzzle
import tracemalloc
import numpy as np
import sys

astar_mem = []
mls_mem = []
mls2_mem = []

astar_sol_length = []
mls_sol_length = []
mls2_sol_length = []

astar_expanded_nodes = []
mls_expanded_nodes = []
mls2_expanded_nodes = []

astar_stored_nodes = []
mls_stored_nodes = []
mls2_stored_nodes = []

def run_solver(algo_name, puzzle):
    print('Running', algo_name)
    tracemalloc.start()
    if algo_name == "A*":
        a_star_search(puzzle)
    elif algo_name == "MLS":
        machine_learning_search(puzzle)
    elif algo_name == "MLS2":
        machine_learning_search_2(puzzle)
    else:
        return None
    _, memory_usage = tracemalloc.get_traced_memory()
    memory_usage = round(memory_usage / (1024 ** 2), 6)
    tracemalloc.stop()
    print('Done')
    reporter = Reporter.get_algorithm_stats(algo_name)
    return memory_usage, reporter["solution_len"], reporter["expansions"], reporter["nodes_stored"]

def run_test(number_of_runs):
    for i in range(int(number_of_runs)):
        puzzle = generate_puzzle()
        puzzle.print_state()

        #A-star
        memory_usage, solution_len, expansions, nodes_stored = run_solver("A*", puzzle)
        astar_mem.append(memory_usage)
        astar_sol_length.append(solution_len)
        astar_expanded_nodes.append(expansions)
        astar_stored_nodes.append(nodes_stored)

        #MLS
        memory_usage, solution_len, expansions, nodes_stored = run_solver("MLS", puzzle)
        mls_mem.append(memory_usage)
        mls_sol_length.append(solution_len)
        mls_expanded_nodes.append(expansions)
        mls_stored_nodes.append(nodes_stored)

        #MLS2
        memory_usage, solution_len, expansions, nodes_stored = run_solver("MLS2", puzzle)
        mls2_mem.append(memory_usage)
        mls2_sol_length.append(solution_len)
        mls2_expanded_nodes.append(expansions)
        mls2_stored_nodes.append(nodes_stored)

        Reporter.print_results()

def print_stats():
    print('astar_mem', np.average(astar_mem))
    print('mls_mem', np.average(mls_mem))
    print('mls2_mem', np.average(mls2_mem))

    print('astar_sol_length',np.average(astar_sol_length))
    print('mls_sol_length', np.average(mls_sol_length))
    print('mls2_sol_length', np.average(mls2_sol_length))

    print('astar_expanded_nodes',np.average(astar_expanded_nodes))
    print('mls_expanded_nodes',np.average(mls_expanded_nodes))
    print('mls2_expanded_nodes',np.average(mls2_expanded_nodes))

    print('astar_stored_nodes',np.average(astar_stored_nodes)) 
    print('mls_stored_nodes',np.average(mls_stored_nodes))
    print('mls2_stored_nodes',np.average(mls2_stored_nodes)) 

if __name__ == '__main__':
    if len(sys.argv) < 1:
        number_of_runs = 10
    else:
        number_of_runs = sys.argv[1]
    run_test(number_of_runs)
    print_stats()