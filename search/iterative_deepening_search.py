from collections import deque
import itertools
from eight_puzzle import EightPuzzle, generate_puzzle
from node.node import Node
from solution import print_solution
from reporter import Reporter
from solution import print_solution

explored = set()

def dls(node, depth, reporter):
    '''
    Based on: https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search
    '''
    curr_state = node.state
    if depth == 0:
        if curr_state.is_goal():
            reporter.set_solution_length(node)
            return (node, True)
        else:
            return (None, True)
    
    else:
        any_remaining = False
        reporter.increment_expansion()
        for direction in curr_state.get_legal_moves():
            new_state = curr_state.move(direction)
            if new_state.get_state() not in explored:
                child_node = Node(state=curr_state.move(direction), parent=node, h_val=0 ,f_val=0, depth=0)
                explored.add(child_node.state.get_state())
                reporter.increment_stored()
                found, remaining = dls(child_node, depth - 1, reporter)
                if found is not None:
                    return (found, True)
                if remaining:
                    any_remaining = True

    return (None, any_remaining)

def iterative_deepening_search(puzzle: EightPuzzle, reporter = Reporter('idfs')):
    root = Node(state=puzzle, parent=None, h_val=0, f_val=0, depth=0)
    for i in itertools.count():
        reporter.reset_expansion()
        reporter.reset_stored()
        result, _ = dls(root, i, reporter)
        explored.clear()
        if result is not None:
            return result
