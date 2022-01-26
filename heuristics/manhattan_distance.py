def manhattan_distance(puzzle):
    state = puzzle.get_state()
    manhattan_distance = 0
    index_to_coord = ((0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2))
    solution = ((2, 2), (0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2))

    for pos in range(len(state)):
        digit = state[pos]
        x_dist = abs(index_to_coord[pos][0] - solution[digit][0])
        y_dist = abs(index_to_coord[pos][1] - solution[digit][1])
        if digit != 0:
            manhattan_distance += x_dist + y_dist

    return manhattan_distance

    
def manhattan_distance_fifteen(puzzle):
    state = puzzle.get_state()
    manhattan_distance = 0
    index_to_coord = ((0, 0), (1, 0), (2, 0), (3, 0),
                      (0, 1), (1, 1), (2, 1), (3, 1),
                      (0, 2), (1, 2), (2, 2), (3, 2),
                      (0, 3), (1, 3), (2, 3), (3, 3))
    solution = ((3, 3), 
                (0, 0), (1, 0), (2, 0), (3, 0), 
                (0, 1), (1, 1), (2, 1), (3, 1),
                (0, 2), (1, 2), (2, 2), (3, 2),
                (0, 3), (1, 3), (2, 3))

    for pos in range(len(state)):
        digit = state[pos]
        x_dist = abs(index_to_coord[pos][0] - solution[digit][0])
        y_dist = abs(index_to_coord[pos][1] - solution[digit][1])
        if digit != 0:
            manhattan_distance += x_dist + y_dist

    return manhattan_distance
