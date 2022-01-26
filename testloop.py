from search import breadth_first_search, depth_first_search, a_star_search, iterative_deepening_search, machine_learning_search, machine_learning_search_2, machine_learning_search_2_imported
from reporter import Reporter
from eight_puzzle import generate_puzzle, EightPuzzle
import tracemalloc
import numpy as np
import sys

bfs_mem = []
dfs_mem = []
astar_mem = []
# idfs_mem = []
mls_mem = []
mls2_mem = []

bfs_sol_length = []
dfs_sol_length = []
astar_sol_length = []
# idfs_sol_length = []
mls_sol_length = []
mls2_sol_length = []

bfs_expanded_nodes = []
dfs_expanded_nodes = []
astar_expanded_nodes = []
# idfs_expanded_nodes = []
mls_expanded_nodes = []
mls2_expanded_nodes = []

bfs_stored_nodes = []
dfs_stored_nodes = []
astar_stored_nodes = []
# idfs_stored_nodes = []
mls_stored_nodes = []
mls2_stored_nodes = []


def run_solver(algo_name, puzzle):
    print('Running', algo_name)
    tracemalloc.start()
    if algo_name == "BFS":
        breadth_first_search(puzzle)
    elif algo_name == "DFS":
        depth_first_search(puzzle)
    elif algo_name == "A*":
        a_star_search(puzzle)
    # elif algo_name == "idfs":
    #     iterative_deepening_search(puzzle)
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

        #BFS
        memory_usage, solution_len, expansions, nodes_stored = run_solver("BFS", puzzle)
        bfs_mem.append(memory_usage)
        bfs_sol_length.append(solution_len)
        bfs_expanded_nodes.append(expansions)
        bfs_stored_nodes.append(nodes_stored)

        #DFS
        memory_usage, solution_len, expansions, nodes_stored = run_solver("DFS", puzzle)
        dfs_mem.append(memory_usage)
        dfs_sol_length.append(solution_len)
        dfs_expanded_nodes.append(expansions)
        dfs_stored_nodes.append(nodes_stored)

        #A-star
        memory_usage, solution_len, expansions, nodes_stored = run_solver("A*", puzzle)
        astar_mem.append(memory_usage)
        astar_sol_length.append(solution_len)
        astar_expanded_nodes.append(expansions)
        astar_stored_nodes.append(nodes_stored)

        # IDFS
        # memory_usage, solution_len, expansions, nodes_stored = run_solver("idfs", puzzle)
        # idfs_mem.append(memory_usage)
        # idfs_sol_length.append(solution_len)
        # idfs_expanded_nodes.append(expansions)
        # idfs_stored_nodes.append(nodes_stored)

        #MLS mem
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
    print('bfs_mem', np.average(bfs_mem))
    print('dfs_mem', np.average(dfs_mem))
    print('astar_mem', np.average(astar_mem))
    # print('idfs_mem', np.average(idfs_mem))
    print('mls_mem', np.average(mls_mem))
    print('mls2_mem', np.average(mls2_mem))

    print('bfs_sol_length',np.average(bfs_sol_length))
    print('dfs_sol_length', np.average(dfs_sol_length))
    print('astar_sol_length',np.average(astar_sol_length))
    # print('idfs_sol_length', np.average(idfs_sol_length))
    print('mls_sol_length', np.average(mls_sol_length))
    print('mls2_sol_length', np.average(mls2_sol_length))

    print('bfs_expanded_nodes',np.average(bfs_expanded_nodes))
    print('dfs_expanded_nodes',np.average(dfs_expanded_nodes))
    print('astar_expanded_nodes',np.average(astar_expanded_nodes))
    # print('idfs_expanded_nodes',np.average(idfs_expanded_nodes))
    print('mls_expanded_nodes',np.average(mls_expanded_nodes))
    print('mls2_expanded_nodes',np.average(mls2_expanded_nodes))

    print('bfs_stored_nodes',np.average(bfs_stored_nodes)) 
    print('dfs_stored_nodes',np.average(dfs_stored_nodes))
    print('astar_stored_nodes',np.average(astar_stored_nodes)) 
    # print('idfs_stored_nodes',np.average(idfs_stored_nodes)) 
    print('mls_stored_nodes',np.average(mls_stored_nodes)) 
    print('mls2_stored_nodes',np.average(mls2_stored_nodes)) 

if __name__ == '__main__':
    if len(sys.argv) < 1:
        number_of_runs = 100
    else:
        number_of_runs = sys.argv[1]
    run_test(number_of_runs)
    print_stats()