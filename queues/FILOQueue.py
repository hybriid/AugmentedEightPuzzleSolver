from .Queue import Queue
from collections import deque

class FILOQueue(Queue):
    def __init__(self):
        self.queue = deque()
    
    def push(self, item):
        self.queue.append(item)

    def pop(self):
        return self.queue.pop()
    
    def size(self):
        return len(self.queue)
