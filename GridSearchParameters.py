from abc import ABC, abstractmethod

class GridSearchParameters(ABC):
    def __init__(self):
        self.gs_params = None
        self.init_gs_params()
    
    @abstractmethod
    def init_gs_params(self):
        pass
    
    def get_gs_params(self):
        return self.gs_params