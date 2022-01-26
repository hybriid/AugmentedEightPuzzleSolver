from dataclasses import dataclass

@dataclass
class Node:
    state: None
    parent: None
    f_val: None
    h_val: None
    depth: 0

    def __lt__(self, other):
        return self.f_val < other.f_val

    def __gt__(self, other):
        return self.f_val > other.f_val

    def __eq__(self, other):
        if self.h_val != other.h_val: # Tie-breaking prioritizes goal node if found
            return self.h_val < other.h_val
        return self.f_val == other.f_val