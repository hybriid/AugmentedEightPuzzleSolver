from collections import deque

def get_solution(node):
    solution = deque()
    solution.appendleft(node.state)
    curr_node = node
    while curr_node is not None:
        parent = curr_node.parent
        if parent is not None:
            solution.appendleft(parent.state)
        curr_node = parent
    return list(solution)

def print_solution(solution):
    solution_steps = get_solution(solution)
    for step in solution_steps:
        step.print_state()