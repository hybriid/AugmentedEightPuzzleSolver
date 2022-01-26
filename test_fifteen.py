
from reporter import Reporter
from fifteen_puzzle import generate_puzzle
from search_fifteen_puzzle import a_star_search, machine_learning_search, machine_learning_search_2

puzzle = generate_puzzle()
puzzle.print_state()

print('Running A*')
a_star_search(puzzle)
print('Done')
print('Running MLS')
machine_learning_search(puzzle)
print('Done')
print('Running MLS2')
machine_learning_search_2(puzzle)
print('Done')

Reporter.print_results()
