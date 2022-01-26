from enum import Enum
import random

class Direction(Enum):
    LEFT = -1
    UP = -4
    RIGHT = 1
    DOWN = 4

class FifteenPuzzle:
    def __init__(self, state):
        """
        Our 'grid' is represented as a one dimensional tuple for simplicity
        Hence self.goal is really:
          1  2  3  4
          5  6  7  8
          9  10 11 12
          13 14 15 0
        """
        self.goal = (1, 2, 3, 4,    \
                     5, 6, 7, 8,    \
                     9, 10, 11, 12, \
                     13, 14, 15, 0)
        self.state = state

    def get_blank(self):
        return self.state.index(0)

    def get_state(self):
        return self.state

    def is_legal(self, direction):
        if direction == Direction.RIGHT and self.get_blank() in [3, 7, 11, 15]:
            return False
        if direction == Direction.UP and self.get_blank() in [0, 1, 2, 3]:
            return False
        if direction == Direction.LEFT and self.get_blank() in [0, 4, 8, 12]:
            return False
        if direction == Direction.DOWN and self.get_blank() in [12, 13, 14, 15]:
            return False
        return True

    def get_legal_moves(self):
        directions = [Direction.LEFT, Direction.UP, Direction.RIGHT, Direction.DOWN]
        return [direction for direction in directions if self.is_legal(direction)]
    
    def is_goal(self):
        return self.state == self.goal

    def move(self, direction):
        assert(isinstance(direction, Direction))
        if not self.is_legal(direction):
            raise BaseException('Out of Bounds!')

        # Get our state as a list so that we can swap elements later
        new_state = list(self.state)
        blank_loc = self.get_blank()
        swap_loc = self.get_blank() + direction.value
        
        # Swap our values
        new_state[blank_loc], new_state[swap_loc] = new_state[swap_loc], new_state[blank_loc]
        return FifteenPuzzle(tuple(new_state))

    def print_state(self):
        res = [str(val) + '\n' if i in [3, 7, 11, 15] else str(val) + ' ' for i, val in enumerate(self.state)]
        print(''.join(res))

def generate_puzzle():
    # Start with the goal state
    puzzle = FifteenPuzzle((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0))
    for i in range(100):
        direction = random.choice(puzzle.get_legal_moves())
        puzzle = puzzle.move(direction)
        # puzzle.print_state()
    return puzzle

if __name__ == '__main__':
    x = generate_puzzle()
    x.print_state()

