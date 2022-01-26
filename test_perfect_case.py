from search import breadth_first_search, depth_first_search, a_star_search, iterative_deepening_search, machine_learning_search, machine_learning_search_2, machine_learning_search_2_imported
from reporter import Reporter
from eight_puzzle import generate_puzzle, EightPuzzle

puzzle = EightPuzzle((6,1,0,5,3,2,4,8,7))
puzzle.print_state()
print('Running BFS')
breadth_first_search(puzzle)
print('Done')
print('Running DFS')
depth_first_search(puzzle)
print('Done')
print('Running A*')
a_star_search(puzzle)
print('Done')
print('Running IDFS')
iterative_deepening_search(puzzle)
print('Done')
print('Running MLS')
machine_learning_search(puzzle)
print('Done')
print('Running MLS2')
machine_learning_search_2_imported(puzzle)
print('Done')

Reporter.print_results()
