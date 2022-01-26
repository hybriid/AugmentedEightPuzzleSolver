from collections import deque
from .Queue import Queue

class FIFOQueue(Queue):
    def __init__(self):
        self.queue = deque()
    
    def push(self, item):
        self.queue.append(item)

    def pop(self):
        return self.queue.popleft()
    
    def size(self):
        return len(self.queue)
