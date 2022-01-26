from abc import abstractmethod, ABC

class Queue(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def push(self, item):
        pass
    
    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def size(self):
        pass
