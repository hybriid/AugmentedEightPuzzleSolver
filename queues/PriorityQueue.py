from .Queue import Queue
import heapq

class PriorityQueue(Queue):
    def __init__(self):
        self.queue = []
    
    def push(self, item):
        heapq.heappush(self.queue, item)

    def pop(self):
        return heapq.heappop(self.queue)
    
    def size(self):
        return len(self.queue)