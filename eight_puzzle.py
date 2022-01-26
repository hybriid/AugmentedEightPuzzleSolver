from enum import Enum
import random

class Direction(Enum):
    LEFT = -1
    UP = -3
    RIGHT = 1
    DOWN = 3

class EightPuzzle:
    def __init__(self, state):
        """
        Our 'grid' is represented as a one dimensional tuple for simplicity
        Hence self.goal is really:
          123
          456
          780
        Each index that is divisable by 3 signals a new row
        """
        self.goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
        self.state = state

    def get_blank(self):
        return self.state.index(0)

    def get_state(self):
        return self.state

    def is_legal(self, direction):
        if direction == Direction.RIGHT and self.get_blank() in [2, 5, 8]:
            return False
        if direction == Direction.UP and self.get_blank() in [0, 1, 2]:
            return False
        if direction == Direction.LEFT and self.get_blank() in [0, 3, 6]:
            return False
        if direction == Direction.DOWN and self.get_blank() in [6, 7, 8]:
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
        return EightPuzzle(tuple(new_state))

    def print_state(self):
        res = [str(val) + '\n' if i in [2, 5, 8] else str(val) for i, val in enumerate(self.state)]
        print(''.join(res))

def generate_puzzle():
    # Start with the goal state
    def check_solvability(state):
        """ 
        Checks if the given state is solvable 
        From: https://github.com/aimacode/aima-python/blob/master/search.py
        """
        inversion = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if (state[i] > state[j]) and state[i] != 0 and state[j] != 0:
                    inversion += 1
        return inversion % 2 == 0

    puzzle = EightPuzzle((1, 2, 3, 4, 5, 6, 7, 8, 0))
    for i in range(1000):
        direction = random.choice(puzzle.get_legal_moves())
        puzzle = puzzle.move(direction)
    assert check_solvability(puzzle.get_state()) == True
    return puzzle

if __name__ == '__main__':
    x = generate_puzzle()
    x.print_state()

