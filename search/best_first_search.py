from node.node import Node

def best_first_search(puzzle, q, h, reporter):
    queue, explored = q, set()
    init_node = Node(state=puzzle, parent=None, f_val=0 + h(puzzle), h_val=h(puzzle), depth=0)
    queue.push(init_node)
    while q.size() > 0:
        curr_node = queue.pop()
        curr_puzzle = curr_node.state
        if curr_puzzle.is_goal():
            reporter.set_solution_length(curr_node)
            return curr_node
        reporter.increment_expansion() # Not part of the algorithm -- for logging / metrics only
        for direction in curr_puzzle.get_legal_moves():
            child_puzzle = curr_puzzle.move(direction)
            if child_puzzle.get_state() not in explored:
                explored.add(child_puzzle.get_state())
                depth = curr_node.depth + 1
                f_val = depth + h(child_puzzle)
                child_node = Node(state=child_puzzle, parent=curr_node, f_val=f_val, h_val=h(child_puzzle), depth=depth)
                reporter.increment_stored() # Not part of the algorithm -- for logging / metrics only
                reporter.increment_if_h_inconsistent(child_node, curr_node, h)
                queue.push(child_node)
    return False
