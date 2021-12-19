from abc import ABC, abstractmethod

class GridProperties(ABC):
    
    def __init__(self):
       self.grid_dict = None
       self.init_grid()
    
    @abstractmethod
    def init_grid(self):
        pass
    
    def get_grid(self):
        return self.grid_dict
